import random
from copy import copy, deepcopy

from models.measure import Measure


class Tune():
    """Class for representing a tune, a list of measures """

    def __init__(self, key, note_count, bars, note_duration,
                 note_bar, title="", measures=None, gen=False,
                 count=10, WEIGHTS=None, string=None):
        """Initialize the class

        Arguments:
        key -- the key of the tune
        note_count -- the number of crotchets in the measure (in 3/4, 3)
        bars -- the number of bars per measure (in 3/4, 4)
        note_duration -- the starting duration of a note in ABC notation
        note_bar -- the number of bars for a note in ABC notation
        title -- the title of the tune
        measures -- a list of measures to init the song with, optional
        gen -- an optional parameter, if true
            immediately generate a random list of measures
        count -- the number of measures to generate if gen is true
        WEIGHTS -- the WEIGHTS to set for generating random songs
        string -- a string to initialize the tune
        """
        self.WEIGHTS = deepcopy(WEIGHTS)
        self.key = key
        self.note_count = note_count
        self.note_bar = note_bar
        self.note_duration = note_duration
        self.bars = bars
        self.title = title

        if measures:
            self.measures = measures
        else:
            self.measures = []
            if gen:
                self.gen(count)

        if string:
            self.parse_string(string)

    def __getitem__(self, key):
        return self.measures[key]

    def __setitem__(self, key, value):
        self.measures[key] = value

    def __delitem__(self, key):
        del self.measures[key]

    def __iter__(self):
        return iter(self.measures)

    def __reversed__(self):
        return reversed(self.measures)

    def __contains__(self, item):
        return item in self.measures

    def __repr__(self):
        return " | ".join((str(measure) for measure in self.measures))

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        return self.dist(other) == 0

    def __len__(self):
        return len(self.measures)

    def __copy__(self):
        copy_object = Tune(
            title=self.title,
            key=self.key,
            note_count=self.note_count,
            note_duration=self.note_duration,
            note_bar=self.note_bar,
            bars=self.bars,
            measures=copy(
                self.measures),
            WEIGHTS=self.WEIGHTS)
        return copy_object

    def __deepcopy__(self, memodict={}):
        copy_object = Tune(
            title=self.title,
            key=self.key,
            note_count=self.note_count,
            note_duration=self.note_duration,
            note_bar=self.note_bar,
            bars=self.bars,
            WEIGHTS=self.WEIGHTS)
        copy_object.measures = [deepcopy(measure) for measure in self.measures]
        copy_object.chords = self.chords
        return copy_object

    def parse_string(self, string):
        """Parse and convert a string into a list of measures

        Arguments:
        string -- the string to parse
        """
        self.measures = [Measure(chord=None, string=s)
                         for s in string.split("|")]

    def gen_chord(self, chords, chord_weights):
        """Returns a randomly generated chord

        Arguments:
        chords -- the chords, modified to fit the key
        chord_weighs -- the chord weights, modified to fit the key
        """
        return random.choices(chords, weights=chord_weights)[0]

    def gen(self, count=10, CHORDS=["A", "B", "C", "D", "E", "F", "G"]):
        """Generates a random list of n measures

        Arguments:
        count -- the number of measures to generate
        CHORDS -- the unmodified chords, default A through G
        """
        self.measures = []
        root = CHORDS.index(self.key)
        self.chords = copy(CHORDS)
        chord_weights = self.WEIGHTS['CHORD']
        for i in range(len(CHORDS)):
            if i == root:
                chord_weights[i] += 100
            elif i in ((root + 1) % len(self.chords),
                       (root + 2) % len(self.chords)):
                self.chords[i] += "m"
            elif i in ((root + 3) % len(self.chords),
                       (root + 4) % len(self.chords)):
                chord_weights[i] += 75
            elif i == (root + 5) % len(self.chords):
                chord_weights[i] += 50
                self.chords[i] += "m"
            elif i == (root + 6) % len(self.chords):
                self.chords[i] += "dim"

        for _ in range(count):
            m = Measure(self.gen_chord(self.chords, chord_weights))
            m.gen(
                self.WEIGHTS,
                self.chords,
                key=self.key,
                note_count=self.note_count,
                note_bar=self.note_bar,
                bars=self.bars)
            self.measures.append(m)

    def pop(self, index):
        """Helper function for removing a measure"""
        self.measures.pop(index)

    def append(self, measure):
        """Helper function for appending a measure"""
        self.measures.append(measure)

    def insert(self, index, measure):
        """Helper function for inserting a measure"""
        self.measures.insert(index, measure)

    def dist(self, other):
        """Returns the distance (or cost) from one tune to another"""
        return sum([measure.dist(other_measure) for (
            measure, other_measure) in zip(self.measures, other.measures)])

    def lock_measures(self, other):
        """Call the lock measure function for each measure"""
        [measure.lock_measure(other_measure) for (
            measure, other_measure) in zip(self.measures, other.measures)]

    def select(self):
        """Returns a random unlocked measure"""
        i = random.randint(1, len(self.measures)) - 1
        while(self.measures[i].locked):
            i = random.randint(1, len(self.measures)) - 1
        return i

    def mutate(self, count=1):
        """Mutates a random measure

        Arguments:
        count -- the number of measures to mutate
        """
        for _ in range(count):
            i = self.select()
            if random.randint(1, 100) < 25:
                self.pop(i)
                m = Measure(self.gen_chord(self.chords, self.WEIGHTS['CHORD']))
                m.gen(
                    self.WEIGHTS,
                    self.chords,
                    key=self.key,
                    note_count=self.note_count,
                    note_bar=self.note_bar,
                    bars=self.bars)
                self.insert(i, m)
            else:
                if random.randint(1, 100) < 50:
                    self.measures[i].chord = self.gen_chord(
                        self.chords, self.WEIGHTS['CHORD'])
                else:
                    self.measures[i].mutate(
                        self.WEIGHTS, self.chords, count=random.choices(
                            [1, 2, 3], [60, 30, 10])[0])

    def crossover(self, other, double_point=False):
        """ Returns two children that are combinations of self
                and other at a random point or points
            Retuns None if self = other or self only has one measure

        Arguments:
        other -- the tune to combine with
        double_point -- true if the crossover happens twice
        """
        if len(self.measures) > 1 and self != other:
            if double_point:
                split = random.randint(1, round(len(self.measures) / 2))
            else:
                split = random.randint(1, len(self.measures) - 1)
            child1 = deepcopy(self)
            child2 = deepcopy(other)

            for i in range(split):
                child1[i], child2[i] = child2[i], child1[i]

            if double_point:
                split = random.randint(
                    round(len(self.measures) / 2), len(self.measures) - 1)
                for i in range(split, len(self.measures)):
                    child1[i], child2[i] = child2[i], child1[i]
            return child1, child2
        return None
