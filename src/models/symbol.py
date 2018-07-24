import random 
from Levenshtein import distance

from utils.convert import convert_to_float

class Symbol():
    """docstring for symbol"""
    def __init__(self, note = "", length = "1", prefix = "", suffix = ""):
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

    def gen_length(self, WEIGHTS, beats_left, LENGTH_SUFFIXES = ['1', '2', '3', '4', '6', '8', '12', '1/2', '3/2', '1/4']):
        lengths_left = [suffix for suffix in LENGTH_SUFFIXES if convert_to_float(suffix) <= beats_left]
        weights_left = WEIGHTS['LENGTH'][:len(lengths_left)]
        return random.choices(lengths_left, weights=weights_left)[0]

    def gen_note(self, note_weights, NOTE_NAMES = ["A", "B", "C", "D", "E", "F", "G", "z"]):
        return random.choices(NOTE_NAMES, weights=note_weights)[0]

    def gen(self, WEIGHTS, note_weights, beats_left):
        self.note = self.gen_note(note_weights)
        self.length = self.gen_length(WEIGHTS, beats_left)
        if self.note != 'z':
            self.prefix = self.gen_prefix(WEIGHTS)
            self.suffix = self.gen_suffix(WEIGHTS, self.note.isupper())
        return self.length

    def __repr__(self):
        return self.prefix + self.note + self.suffix + self.length

    def __str__(self):
        return self.__repr__()

    def dist(self, other):
        return distance(self.prefix, other.prefix) + distance(self.note, other.note) + distance(self.suffix, other.suffix) + 2*distance(self.length, other.length)

    def mutate(self, WEIGHTS, note_weights, beats_left):
        self.prefix = self.gen_prefix(WEIGHTS)
        self.suffix = self.gen_suffix(WEIGHTS)
        if random.randint(1, 100) < 50:
            self.note = self.gen_note(note_weights)
        else:
            self.length = self.gen_length(WEIGHTS, beats_left)
        return self.length
