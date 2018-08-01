import random 
from copy import copy, deepcopy
from Levenshtein import distance

from models.symbol import Symbol
from utils.convert import convert_to_float
from utils.pitch import distance as pitch_dist

class Measure():
    """Class for representing a measure, a list of symbols """
    def __init__(self, chord, symbols = None, string = None):
        """Initialize the class
    
        Arguments:
        chord -- the chord of the measure
        symbols -- an optional list of symbols to set for the measure
        string -- a string to initialize the measure
        """
        self.chord = chord
        if symbols:
            self.symbols = symbols
        else:
            self.symbols = []
        self.locked = False

        if string:
            self.parse_string(string) 

    def __repr__(self):
        return '"' + self.chord + '" ' + ' '.join((str(symbol) for symbol in self.symbols)) 

    def __str__(self):
        return self.__repr__()  

    def __copy__(self):
        copy_object = Measure(chord = self.chord, symbols = copy(self.symbols))
        return copy_object

    def __deepcopy__(self, memodict={}):
        copy_object = Measure(self.chord)
        copy_object.symbols = [deepcopy(symbol) for symbol in self.symbols]        
        return copy_object            

    def parse_string(self, string):
        end = string[1:].index('"')
        self.chord = string[1:end + 1]
        self.symbols = [Symbol(string = s) for s in string[end + 3:].split(" ")]            

    def set_weights(self, WEIGHTS, chords):
        """Returns the note weights modified based off the chord of the measure
    
        Arguments:
        WEIGHTS -- the default weights
        chords -- the possible chords
        """
        root = chords.index(self.chord)
        
        note_weights = copy(WEIGHTS['CHORD'])
        for i in range(len(chords)):
            if i == root:
                note_weights[i] += 100
            elif i == (root + 2) % len(chords):
                note_weights[i] += 80  
            elif i == (root + 4) % len(chords):
                note_weights[i] += 100
            elif i == (root + 6) % len(chords):
                note_weights[i] += 60
            elif i == (root + 8) % len(chords):
                note_weights[i] += 40
            elif i == (root + 10) % len(chords):
                note_weights[i] += 20
            elif i == (root + 12) % len(chords):
                note_weights[i] += 10

        note_weights.extend(note_weights)
        note_weights.append(sum(note_weights)/len(note_weights))
        return note_weights

    def gen(self, WEIGHTS, chords, key, note_count, note_bar, bars):
        """Generate a random list of symbols for the measure that fit in the necessary time signature

        Arguments:
        WEIGHTS -- the default weights
        chords -- the possible chords
        key -- the tune's key
        note_count -- needed for time signature
        note_bar -- needed for time signature
        bars -- needed for time signature
        """
        self.symbols = []
        beats_left = (note_count * 1/bars) * note_bar
        note_weights = self.set_weights(WEIGHTS, chords)
        
        while beats_left > 0:
            s = Symbol()
            beats_left -= convert_to_float(s.gen(WEIGHTS, note_weights, beats_left))
            self.append(s)

    def pop(self, index):
        """Helper function for removing a symbol"""
        self.symbols.pop(index)

    def append(self, symbol):
        """Helper function for appending a symbol"""
        self.symbols.append(symbol)

    def insert(self, index, symbol):
        """Helper function for inserting a symbol"""
        self.symbols.insert(index, symbol)    

    def dist(self, other):
        """Returns the distance (or cost) from one measure to another"""        
        return pitch_dist(self.chord, other.chord) + sum([symbol1.dist(symbol2) for (symbol1, symbol2) in zip(self.symbols, other.symbols)]) + 2*abs(len(self.symbols) - len(other.symbols))

    def lock_measure(self, other):
        """Locks measure if it is equal to other"""
        if self.dist(other) == 0:
            self.locked = True
        #[symbol.lock_symbol(other_symbol) for (symbol, other_symbol) in zip(self.symbols, other.symbols)]

    def select(self):
        """Returns a random unlocked symbol"""        
        i = random.randint(1, len(self.symbols))
        while(self.symbols[i - 1].locked):
            i = random.randint(1, len(self.symbols))
        return i

    def mutate(self, WEIGHTS, chords, count = 1):
        """Mutates a random symbol

        Arguments:
        WEIGHTS - the default weights
        chords -- the possible chords
        count -- the number of symbols to mutate        
        """
        for _ in range(count):  
            i = self.select()      
            beats_left = convert_to_float(self.symbols[i - 1].length)
            note_weights = self.set_weights(WEIGHTS, chords)
            
            if random.randint(1, 100) < 50: 
                self.pop(i - 1)
            else:
                beats_left -= convert_to_float(self.symbols[i - 1].mutate(WEIGHTS, note_weights, beats_left))
            
            while beats_left > 0:
                if random.randint(1, 100) < 50 or len(self.symbols) == 0: 
                    s = Symbol()
                    beats_left -= convert_to_float(s.gen(WEIGHTS, note_weights, beats_left))
                    if len(self.symbols) > 0:
                        i = self.select()
                    self.insert(i - 1, s)
                else:
                    i = self.select()
                    beats_left += convert_to_float(self.symbols[i - 1].length)
                    beats_left -= convert_to_float(self.symbols[i - 1].mutate(WEIGHTS, note_weights, beats_left))

            #i = (i + 1) % len(self.symbols)
