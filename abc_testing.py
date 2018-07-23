import random 
import string
from fractions import Fraction
from copy import copy, deepcopy
from Levenshtein import distance
import cProfile

ABC_PREFIX = ("X:1\n"
              "T:{}\n"
              "M:{}/{}\n"
              "L:{}/{}\n"
              "K:{}\n"
              "{}")

def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        return float(num) / float(denom)

class symbol():
    """docstring for symbol"""
    def __init__(self, note = "", length = "", prefix = "", suffix = ""):
        self.prefix = prefix
        self.note = note
        self.suffix = suffix
        self.length = length

    def gen_prefix(self, WEIGHTS, PITCH_PREFIXES = ['', '^', '=', '_']):
        return random.choices(PITCH_PREFIXES, weights=WEIGHTS['PITCH_P'])[0]

    def gen_suffix(self, WEIGHTS, upper = True, PITCH_LOWER_SUFFIXES = ['', '\''], PITCH_UPPER_SUFFIXES = ['', ',']):
        if upper:
            return random.choices(PITCH_UPPER_SUFFIXES, weights=WEIGHTS['PITCH_S'])[0]
        else:
            return random.choices(PITCH_LOWER_SUFFIXES, weights=WEIGHTS['PITCH_S'])[0]

    def gen_length(self, WEIGHTS, beats_left, LENGTH_SUFFIXES = ['1', '2', '3', '4', '6', '8', '12', '1/2', '3/2']):
        lengths_left = [suffix for suffix in LENGTH_SUFFIXES if convert_to_float(suffix) <= beats_left]
        weights_left = WEIGHTS['LENGTH'][:len(lengths_left)]
        return random.choices(lengths_left, weights=weights_left)[0]

    def gen_note(self, note_weights, NOTE_NAMES = ["A", "B", "C", "D", "E", "F", "G", "z"]):
        return random.choices(NOTE_NAMES, weights=note_weights)[0]

    def gen(self, WEIGHTS, note_weights, beats_left):
        self.note = self.gen_note(note_weights[:-1], NOTE_NAMES = ["A", "B", "C", "D", "E", "F", "G"])
        self.length = self.gen_length(WEIGHTS, beats_left, LENGTH_SUFFIXES = ['1', '2', '1/2', '3/2'])
        if self.note != 'z':
            self.prefix = self.gen_prefix(WEIGHTS)
            self.suffix = self.gen_suffix(WEIGHTS, self.note.isupper())
        return self.length

    def __repr__(self):
        return self.prefix + self.note + self.suffix + self.length

    def __str__(self):
        return self.__repr__()

    def dist(self, other):
        return distance(self.prefix, other.prefix) + distance(self.note, other.note) + distance(self.suffix, other.suffix) + distance(self.length, other.length)

    def mutate(self, WEIGHTS, note_weights, beats_left):
        i = random.randint(1, 100)
        if i < 50:
            self.note = self.gen_note(note_weights[:-1], NOTE_NAMES = ["A", "B", "C", "D", "E", "F", "G"])
        else:
            self.length = self.gen_length(WEIGHTS, beats_left, LENGTH_SUFFIXES = ['1', '2', '1/2', '3/2'])
        return self.length

class measure():
    """docstring for measure"""
    def __init__(self, chord, symbols = None):
        self.chord = chord
        if symbols:
            self.symbols = symbols
        else:
            self.symbols = []

    def set_weights(self, WEIGHTS, chords):
        root = chords.index(self.chord)
        
        note_weights = copy(WEIGHTS['CHORD'])
        for i in range(len(chords)):
            if i == root:
                note_weights[i] += 500
            elif i == (root + 2) % len(chords):
                note_weights[i] += 400   
            elif i == (root + 4) % len(chords):
                note_weights[i] += 300
            elif i == (root + 6) % len(chords):
                note_weights[i] += 50
            elif i == (root + 8) % len(chords):
                note_weights[i] += 25
            elif i == (root + 10) % len(chords):
                note_weights[i] += 10
            elif i == (root + 12) % len(chords):
                note_weights[i] += 5
        note_weights.append(sum(note_weights)/len(note_weights))
        return note_weights

    def gen(self, WEIGHTS, chords, key = 'C', note_count = 4, note_bar = 4, bars = 4):
        self.symbols = []
        beats_left = (note_count * 1/bars) * note_bar
        note_weights = self.set_weights(WEIGHTS, chords)
        
        while beats_left > 0:
            s = symbol()
            beats_left -= convert_to_float(s.gen(WEIGHTS, note_weights, beats_left))
            self.append(s)

    def pop(self, index):
        self.symbols.pop(index)

    def append(self, symbol):
        self.symbols.append(symbol)

    def insert(self, index, symbol):
        self.symbols.insert(index, symbol)    

    def __repr__(self):
        return '"' + self.chord + '" ' + ' '.join((str(symbol) for symbol in self.symbols)) 

    def __str__(self):
        return self.__repr__()

    def dist(self, other):
        return distance(self.chord, other.chord) + sum([symbol1.dist(symbol2) for (symbol1, symbol2) in zip(self.symbols, other.symbols)])

    def mutate(self, WEIGHTS, chords, key = 'C', note_count = 4, note_bar = 4, bars = 4, count = 1):
        for _ in range(count):        
            i = random.randint(1, len(self.symbols)) - 1
            beats_left = convert_to_float(self.symbols[i].length)
            note_weights = self.set_weights(WEIGHTS, chords)
            
            split = random.randint(1, 100)
            if split < 50: 
                self.pop(i)
            else:
                beats_left -= convert_to_float(self.symbols[i].mutate(WEIGHTS, note_weights, beats_left))
            
            while beats_left > 0:
                s = symbol()
                beats_left -= convert_to_float(s.gen(WEIGHTS, note_weights, beats_left))
                self.insert(i, s)

class measure_list():
    def __init__(self, key = 'C', note_count = 4, note_bar = 4, bars = 4, measures = None, gen = False, count = 10, WEIGHTS = None, chords = None):
        self.WEIGHTS = WEIGHTS
        self.key = key
        self.note_count = note_count
        self.note_bar = note_bar
        self.bars = bars
        self.chords = chords
        if measures:
            self.measures = measures
        else: 
            self.measures = []
            if gen:
                self.gen(count)

    def gen_chord(self, chords, chord_weights, key = 'C'):
        return random.choices(chords, weights=chord_weights)[0]

    def gen(self, count = 10, CHORDS = ["A", "B", "C", "D", "E", "F", "G"]):
        self.measures = []
        root = CHORDS.index(self.key)
        self.chords = copy(CHORDS)
        chord_weights = self.WEIGHTS['CHORD']
        for i in range(len(CHORDS)):
            if i == root:
                chord_weights[i] += 500
            elif i in ((root + 1) % len(self.chords), (root + 2) % len(self.chords)):
                self.chords[i] += "m"
            elif i in ((root + 3) % len(self.chords), (root + 4) % len(self.chords)):
                chord_weights[i] += 250
            elif i == (root + 5) % len(self.chords):
                chord_weights[i] += 200 
                self.chords[i] += "m"
            elif i == (root + 6) % len(self.chords):
                self.chords[i] += "dim"    

        for _ in range(count):
            m = measure(self.gen_chord(self.chords, chord_weights, key = self.key))
            m.gen(self.WEIGHTS, self.chords, key = self.key, note_count = self.note_count, note_bar = self.note_bar, bars = self.bars)
            self.measures.append(m)

    def pop(self, index):
        self.measures.pop(index)

    def append(self, measure):
        self.measures.append(measure)

    def insert(self, index, measure):
        self.measures.insert(index, measure)    

    def __repr__(self):
        return " | ".join((str(measure) for measure in self.measures))

    def __str__(self):
        return self.__repr__()    

    def dist(self, other):
        return sum([measure1.dist(measure2) for (measure1, measure2) in zip(self.measures, other.measures)])

    def mutate(self, count = 1):
        for _ in range(count): 
            i = random.randint(1, len(self.measures)) - 1
            split = random.randint(1, 100)
            if split < 50: 
                self.pop(i)
                m = measure(self.gen_chord(self.chords, self.WEIGHTS['CHORD'], key = self.key))
                m.gen(self.WEIGHTS, self.chords, key = self.key, note_count = self.note_count, note_bar = self.note_bar, bars = self.bars)
                self.insert(i, m)
            else:
                self.measures[i].mutate(self.WEIGHTS, self.chords, key = self.key, note_count = self.note_count, note_bar = self.note_bar, bars = self.bars, count = 1)

def main():
    WEIGHTS = {}
    CHOICES = {}
    WEIGHTS['NOTE'] = random.sample(list(range(100)), 8)

    #WEIGHTS['CHORD'] = [x + y for x, y in zip(WEIGHTS['NOTE'][:7], WEIGHTS['NOTE'][7:-1])]
    WEIGHTS['CHORD'] = WEIGHTS['NOTE'][:-1]
    WEIGHTS['PITCH_P'] = [60, 0, 0, 0]
    WEIGHTS['PITCH_S'] = [90, 0]
    WEIGHTS['LENGTH'] = [55, 34, 21, 13, 8, 5, 3, 2, 2, 1]

    title = "Test"
    note_count = 4
    note_duration = 1
    note_bar = bars = 4
    key = 'C'
    measures = 8
    compare_measure_list = measure_list(WEIGHTS, measures = [
        measure(chord = "C", symbols = [
            symbol("E"), symbol("E"), symbol("F"), symbol("G")]),
        measure(chord = "C", symbols = [
            symbol("G"), symbol("F"), symbol("E"), symbol("D")]),
        measure(chord = "C", symbols = [
            symbol("C"), symbol("C"), symbol("D"), symbol("E")]),
        measure(chord = "G", symbols = [
            symbol("E", "3/2"), symbol("D", "1/2"), symbol("D", "2")]),
        measure(chord = "C", symbols = [
            symbol("E"), symbol("E"), symbol("F"), symbol("G")]),
        measure(chord = "C", symbols = [
            symbol("G"), symbol("F"), symbol("E"), symbol("D")]),
        measure(chord = "C", symbols = [
            symbol("C"), symbol("C"), symbol("D"), symbol("E")]),
        measure(chord = "C", symbols = [
            symbol("D", "3/2"), symbol("C", "1/2"), symbol("C", "2")]),
    ])
    m1 = measure(chord = "C", symbols = [symbol("E"), symbol("E"), symbol("F"), symbol("G")])
    m2 = measure(chord = "C", symbols = [symbol("E2"), symbol("E2")])
    print(m1.dist(m2))
    exit()
    # m_list = measure_list(WEIGHTS, note_count = note_count, note_bar = note_bar, bars = bars, key = key, gen = True)
    #measure_list_list = [gen_measure_list(WEIGHTS, note_count = note_count, note_bar = note_bar, bars = bars, key = key, measures = measures) for _ in range(1000)]
    measure_list_list = [measure_list(note_count = note_count, note_bar = note_bar, bars = bars, key = key, gen = True, count = measures, WEIGHTS = WEIGHTS) for _ in range(1000)]
    best = min([measure_list for measure_list in measure_list_list], key = lambda x: x.dist(compare_measure_list))
    
    big_tune = str(best)
    best_dist = best.dist(compare_measure_list)
    
    print("best: ", best_dist)

    while(best_dist > 20):
        best_children = [deepcopy(best) for _ in range(1000)]

        [best.mutate(count = 1) for best in best_children]
        best_child = min([best for best in best_children], key = lambda x: x.dist(compare_measure_list))

        #print("best child: \n", best)
        if best_dist > best_child.dist(compare_measure_list):
            best_dist = best_child.dist(compare_measure_list)
            best = best_child
            big_tune += "| " + str(best)
            print("best: ", best_dist)
            print("best child:", best)
        #else:
            #print("All children worse :/")
                
    tune = big_tune + " |]"
    best = ABC_PREFIX.format(title, note_count, bars, note_duration, note_bar, key, tune)

    with open('best.abc', 'w') as file:
        file.write(best)
    
    print('\n')
    print(best)

if __name__ == "__main__":
    main()
