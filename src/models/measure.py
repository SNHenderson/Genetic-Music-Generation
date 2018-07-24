import random 
from copy import copy, deepcopy
from Levenshtein import distance

from models.symbol import Symbol
from utils.convert import convert_to_float

class Measure():
    """docstring for measure"""
    def __init__(self, chord, symbols = None, string = None):
        self.chord = chord
        if symbols:
            self.symbols = symbols
        else:
            self.symbols = []
        self.locked = False

        if string:
            self.parse_string(string) 

    def parse_string(self, string):
        self.chord = string[1]
        self.symbols = [Symbol(string = s) for s in string[4:].split(" ")]            

    def set_weights(self, WEIGHTS, chords):
        root = chords.index(self.chord)
        
        note_weights = copy(WEIGHTS['CHORD'])
        for i in range(len(chords)):
            if i == root:
                note_weights[i] += 500
            elif i == (root + 2) % len(chords):
                note_weights[i] += 400   
            elif i == (root + 4) % len(chords):
                note_weights[i] += 500
            elif i == (root + 6) % len(chords):
                note_weights[i] += 100
            elif i == (root + 8) % len(chords):
                note_weights[i] += 50
            elif i == (root + 10) % len(chords):
                note_weights[i] += 25
            elif i == (root + 12) % len(chords):
                note_weights[i] += 10

        note_weights.extend(note_weights)
        note_weights.append(sum(note_weights)/len(note_weights))
        return note_weights

    def gen(self, WEIGHTS, chords, key, note_count, note_bar, bars):
        self.symbols = []
        beats_left = (note_count * 1/bars) * note_bar
        note_weights = self.set_weights(WEIGHTS, chords)
        
        while beats_left > 0:
            s = Symbol()
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
        return 2*distance(self.chord, other.chord) + sum([symbol1.dist(symbol2) for (symbol1, symbol2) in zip(self.symbols, other.symbols)]) + 2*abs(len(self.symbols) - len(other.symbols))

    def lock_measure(self, other):
        if self.dist(other) == 0:
            self.locked = True

    def mutate(self, WEIGHTS, chords, count = 1):
        for _ in range(count):        
            i = random.randint(1, len(self.symbols)) - 1
            beats_left = convert_to_float(self.symbols[i].length)
            note_weights = self.set_weights(WEIGHTS, chords)
            
            if random.randint(1, 100) < 50: 
                self.pop(i)
            else:
                beats_left -= convert_to_float(self.symbols[i].mutate(WEIGHTS, note_weights, beats_left))
            
            while beats_left > 0:
                s = Symbol()
                beats_left -= convert_to_float(s.gen(WEIGHTS, note_weights, beats_left))
                if len(self.symbols) > 0:
                    i = random.randint(1, len(self.symbols)) - 1
                self.insert(i, s)
