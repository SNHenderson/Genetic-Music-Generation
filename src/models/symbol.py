import random 
from Levenshtein import distance

from utils.convert import convert_to_float
from utils.pitch import distance as pitch_dist

class Symbol():
    """docstring for symbol"""
    def __init__(self, note = "", length = "1", prefix = "", suffix = "", string = None):
        self.prefix = prefix
        self.note = note
        self.suffix = suffix
        self.length = length
        self.locked = False

        if string:
            self.parse_string(string)  

    def __repr__(self):
        return self.prefix + self.note + self.suffix + self.length

    def __str__(self):
        return self.__repr__()    
        
    def __copy__(self):
        copy_object = Symbol(note = self.note, length = self.length, prefix = self.prefix, suffix = self.suffix)
        return copy_object

    def __deepcopy__(self, memodict={}):
        copy_object = Symbol(note = self.note, length = self.length, prefix = self.prefix, suffix = self.suffix)
        return copy_object                   

    def parse_string(self, string):
        idx = 0
        
        if string[0].isalpha():
            self.note = string[idx]
            idx += 1
        else:
            self.prefix = string[idx]
            idx += 1
            self.note = string[idx]
            idx += 1
        
        if idx < len(string):
            try:
                convert_to_float(string[idx:])
                self.length = string[idx:]
            except Exception as e:
                self.suffix = string[idx]
                idx += 1
                self.length = string[idx:]

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

    def gen_note(self, note_weights, NOTE_NAMES = ["a", "b", "c", "d", "e", "f", "g", "A", "B", "C", "D", "E", "F", "G", "z"]):
        return random.choices(NOTE_NAMES, weights=note_weights)[0]

    def gen(self, WEIGHTS, note_weights, beats_left):
        self.note = self.gen_note(note_weights)
        self.length = self.gen_length(WEIGHTS, beats_left)
        if self.note != 'z':
            self.prefix = self.gen_prefix(WEIGHTS)
            self.suffix = self.gen_suffix(WEIGHTS, self.note.isupper())
        return self.length

    def dist(self, other):
        return distance(self.prefix, other.prefix) + pitch_dist(self.note, other.note) + distance(self.suffix, other.suffix) + round(2*abs(convert_to_float(self.length) - convert_to_float(other.length)))

    def lock_symbol(self, other):
        if self.dist(other) == 0:
            self.locked = True

    def mutate(self, WEIGHTS, note_weights, beats_left):
        if random.randint(1, 100) < 50:
            self.note = self.gen_note(note_weights)
            if self.note == 'z':
                self.prefix = ""
                self.suffix = ""
        else:
            self.length = self.gen_length(WEIGHTS, beats_left)
        
        if self.note != 'z' and random.randint(1, 100) < 50:
            self.prefix = self.gen_prefix(WEIGHTS)
            self.suffix = self.gen_suffix(WEIGHTS, self.note.isupper())
        return self.length
