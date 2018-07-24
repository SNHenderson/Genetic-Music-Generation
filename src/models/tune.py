import random 
from copy import copy, deepcopy
from Levenshtein import distance

from models.measure import Measure

class Tune():
    def __init__(self, key = None, note_count = None, note_bar = None, bars = None, measures = None, gen = False, count = 10, WEIGHTS = None, string = None):
        self.WEIGHTS = deepcopy(WEIGHTS)
        self.key = key
        self.note_count = note_count
        self.note_bar = note_bar
        self.bars = bars
        if measures:
            self.measures = measures
        else: 
            self.measures = []
            if gen:
                self.gen(count)
        if string:
            self.parse_string(string)

    def parse_string(self, string):
        self.measures = [Measure(chord = None, string = s) for s in string.split("|")]            

    def gen_chord(self, chords, chord_weights):
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
            m = Measure(self.gen_chord(self.chords, chord_weights))
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
        return sum([measure.dist(other_measure) for (measure, other_measure) in zip(self.measures, other.measures)])

    def lock_measures(self, other):
        [measure.lock_measure(other_measure) for (measure, other_measure) in zip(self.measures, other.measures)]

    def mutate(self, count = 1):
        for _ in range(count): 
            i = random.randint(1, len(self.measures)) - 1
            while(self.measures[i].locked):
                i = random.randint(1, len(self.measures)) - 1
            if random.randint(1, 100) < 50: 
                self.pop(i)
                m = Measure(self.gen_chord(self.chords, self.WEIGHTS['CHORD']))
                m.gen(self.WEIGHTS, self.chords, key = self.key, note_count = self.note_count, note_bar = self.note_bar, bars = self.bars)
                self.insert(i, m)
            else:
                if random.randint(1, 100) < 50: 
                    self.measures[i].chord = self.gen_chord(self.chords, self.WEIGHTS['CHORD'])
                self.measures[i].mutate(self.WEIGHTS, self.chords, count = random.randint(1, 2))
