import random 
import string
from fractions import Fraction
from copy import copy

ABC_PREFIX = ("X:1\n"
              "T:{}\n"
              "M:{}/{}\n"
              "L:{}/{}\n"
              "K:{}\n"
              "{}")

NOTE_NAMES = ["a", "b", "c", "d", "e", "f", "g", "A", "B", "C", "D", "E", "F", "G", "z"]
NOTE_WEIGHTS = random.sample(list(range(100)), 15)
CHORDS = ["A", "B", "C", "D", "E", "F", "G"]
CHORD_WEIGHTS = [x + y for x, y in zip(NOTE_WEIGHTS[:7], NOTE_WEIGHTS[7:-1])]
PITCH_PREFIXES = ['', '^', '=', '_']
PITCH_PWEIGHTS = [60, 0,0,0]
PITCH_LOWER_SUFFIXES = ['', '\'']
PITCH_UPPER_SUFFIXES = ['', ',']
PITCH_SWEIGHTS = [90, 10]
LENGTH_SUFFIXES = ['1', '2', '3', '4', '6', '8', '12', '1/2', '3/2' ] #, '1/4']
LENGTH_WEIGHTS = [55, 34, 21, 13, 8, 5, 3, 2, 2, 1]
CROTCHETS = [4, 2, 3, 6, 5, 7]
CROTCHET_WEIGHTS = [13, 8, 5, 3, 2, 2]
BARS = [4, 2, 8]
BAR_WEIGHTS = [2, 2, 1]

def main():
    title = "Test"
    note_count = 6
    note_duration = 1
    note_bar = bars = 8
    key = 'C'
    measures = 10
    measure_list = []
    
    root = CHORDS.index(key)
    chord_weights = copy(CHORD_WEIGHTS)
    for i in range(len(CHORDS)):
        if i == root:
            chord_weights[i] += 500
        elif i in ((root + 1) % len(CHORDS), (root + 2) % len(CHORDS)):
            CHORDS[i] += "m"
        elif i in ((root + 3) % len(CHORDS), (root + 4) % len(CHORDS)):
            chord_weights[i] += 250
        elif i == (root + 5) % len(CHORDS):
            chord_weights[i] += 200 
            CHORDS[i] += "m"
        elif i == (root + 6) % len(CHORDS):
            CHORDS[i] += "dim"    

    tune = ""
    for _ in range(measures):
        beats_left = (note_count * 1/bars) * note_bar
        chord = random.choices(CHORDS, weights=chord_weights)[0]
        measure = '"' + chord + '"'
        root = CHORDS.index(chord)
        note_weights = copy(CHORD_WEIGHTS)
        for i in range(len(CHORDS)):
            if i == root:
                note_weights[i] += 500
            elif i == (root + 2) % len(CHORDS):
                note_weights[i] += 400   
            elif i == (root + 4) % len(CHORDS):
                note_weights[i] += 300
            elif i == (root + 6) % len(CHORDS):
                note_weights[i] += 50
            elif i == (root + 8) % len(CHORDS):
                note_weights[i] += 25
            elif i == (root + 10) % len(CHORDS):
                note_weights[i] += 10
            elif i == (root + 12) % len(CHORDS):
                note_weights[i] += 5
        note_weights.extend(note_weights)
        note_weights.append(sum(note_weights)/len(note_weights))
        while beats_left > 0:
            note = random.choices(NOTE_NAMES, weights=note_weights)[0]
            if note != 'z':
                measure += ' ' + random.choices(PITCH_PREFIXES, weights=PITCH_PWEIGHTS)[0]
                measure += note
                if note.isupper():
                    measure += random.choices(PITCH_UPPER_SUFFIXES, weights=PITCH_SWEIGHTS)[0]
                else:
                    measure += random.choices(PITCH_LOWER_SUFFIXES, weights=PITCH_SWEIGHTS)[0]
            else:
                measure += note
            lengths_left = [suffix for suffix in LENGTH_SUFFIXES if float(Fraction(suffix)) <= beats_left]
            weights_left = LENGTH_WEIGHTS[:len(lengths_left)]
            multiplier = random.choices(lengths_left, weights=weights_left)[0]
            measure += multiplier
            beats_left -= float(Fraction(multiplier))
        measure_list.append(measure)
    tune = " | ".join(measure_list) + " |]"
    song = ABC_PREFIX.format(title, note_count, bars, note_duration, note_bar, key, tune)

    with open('song.abc', 'w') as file:
        file.write(song)
    print(song)

if __name__ == "__main__":
    main()
