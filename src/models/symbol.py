import random

from Levenshtein import distance
from utils.convert import convert_to_float


class Symbol():
    """Class for representing a symbol """

    def __init__(self, note="", length="1", prefix="", suffix="", string=None):
        """Initialize the class

        Arguments:
        note -- the note of the symbol
        length -- the length of the symbol
        prefix -- the prefix of the symbol
        suffix -- the suffix of the symbol
        string -- a string to initialize the symbol
        """
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
        copy_object = Symbol(
            note=self.note,
            length=self.length,
            prefix=self.prefix,
            suffix=self.suffix)
        return copy_object

    def __deepcopy__(self, memodict={}):
        copy_object = Symbol(
            note=self.note,
            length=self.length,
            prefix=self.prefix,
            suffix=self.suffix)
        return copy_object

    def parse_string(self, string):
        """Parse and convert a string into a list of measures

        Arguments:
        string -- the string to parse
        """
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

    def gen_prefix(self, WEIGHTS, PITCH_PREFIXES=['', '^', '=', '_']):
        """Return a random prefix weighted with WEIGHTS

        Arguments:
        WEIGHTS -- the default weights
        PITCH_PREFIXES -- optional prefixes for pitches
        """
        return random.choices(PITCH_PREFIXES, weights=WEIGHTS['PITCH_P'])[0]

    def gen_suffix(self, WEIGHTS, upper=True, PITCH_LOWER_SUFFIXES=[
                   '', '\''], PITCH_UPPER_SUFFIXES=['', ',']):
        """Return a random suffix weighted with WEIGHTS

        Arguments:
        WEIGHTS -- the default weights
        PITCH_LOWER_SUFFIXES -- optional suffixes for lowercase pitches
        PITCH_UPPER_SUFFIXES -- optional suffixes for uppercase pitches
        """
        if upper:
            return random.choices(PITCH_UPPER_SUFFIXES,
                                  weights=WEIGHTS['PITCH_S'])[0]
        else:
            return random.choices(PITCH_LOWER_SUFFIXES,
                                  weights=WEIGHTS['PITCH_S'])[0]

    def gen_length(self, WEIGHTS, beats_left, LENGTH_SUFFIXES=[
                   '1', '2', '3', '4', '6', '8', '12', '1/2', '3/2', '1/4']):
        """Return a random length weighted with WEIGHTS that's less than beats_left

        Arguments:
        WEIGHTS -- the default weights
        beats_left -- number of beats left in the measure
        LENGTH_SUFFIXES -- optional suffixes for lengths
        """
        lengths_left = [
            suffix for suffix in LENGTH_SUFFIXES if
            convert_to_float(suffix) <= beats_left]
        weights_left = WEIGHTS['LENGTH'][:len(lengths_left)]
        return random.choices(lengths_left, weights=weights_left)[0]

    def gen_note(self, note_weights, NOTE_NAMES=[
            "a", "b", "c", "d", "e", "f", "g",
            "A", "B", "C", "D", "E", "F", "G", "z"]):
        """Return a random note weighted with note_weights

        Arguments:
        note_weights -- weights that have been modified according to a chord
        NOTE_NAMES -- optional options for notes
        """
        return random.choices(NOTE_NAMES, weights=note_weights)[0]

    def gen(self, WEIGHTS, note_weights, beats_left):
        """Generates a random symbol with prefix, suffix, and length

        Arguments:
        note_weights -- weights that have been modified according to a chord
        beats_left -- number of beats left in the measure
        """
        self.note = self.gen_note(note_weights)
        self.length = self.gen_length(WEIGHTS, beats_left)
        if self.note != 'z':
            self.prefix = self.gen_prefix(WEIGHTS)
            self.suffix = self.gen_suffix(WEIGHTS, self.note.isupper())
        return self.length

    def dist(self, other):
        """Returns the distance (or cost) from one tune to another"""
        prefix_dist = distance(self.prefix, other.prefix)
        note_dist = distance(self.note, other.note)
        suffix_dist = distance(self.suffix, other.suffix)
        length_dist = distance(self.length, other.length)
        return prefix_dist + note_dist + suffix_dist + length_dist

    def lock_symbol(self, other):
        """Locks symbol if it is equal to other"""
        if self.dist(other) == 0:
            self.locked = True

    def mutate(self, WEIGHTS, note_weights, beats_left):
        """Mutates a random prefix/suffix/name/length

        Arguments:
        WEIGHTS - the default weights
        note_weights -- the modified weights for note names
        beats_left -- number of beats left in the measure
        """
        if random.randint(1, 100) < 50:
            self.note = self.gen_note(note_weights)
            if self.note == 'z':
                self.prefix = ""
                self.suffix = ""
        else:
            self.length = self.gen_length(WEIGHTS, beats_left)

        if self.suffix != "":
            self.suffix = self.gen_suffix(WEIGHTS, self.note.isupper())

        if self.note != 'z' and random.randint(1, 100) < 50:
            self.prefix = self.gen_prefix(WEIGHTS)

        return self.length
