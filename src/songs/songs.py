from models.tune import Tune
from models.measure import Measure
from models.symbol import Symbol

Lichfield = Tune(title = "Lichfield", note_count = 4, bars = 4, note_duration = 1, note_bar = 8, key = 'G', string = '"G" G2 G A B2 G2|"C" E2 c c c4|"D" D2 D E F2 c2|"D" B4 A4|"G" G2 G A B2 G2|"C" E2 c c c4|"D" D2 D E F2 G A|"G" A4 G4|"G" d2 d d c2 c2|"D" B c d B A4|"G" d2 d d c2 c c|"D" B4 A4|"G" G2 G A B2 G2|"C" E2 c c c4|"D" D2 D E F2 G A|"G" A4 G4')

Mazurka = Tune(title = "Mazurka : Boite de Jazz", note_count = 9, bars = 8, note_duration = 1, note_bar = 8, key = 'C', string = '"Am" z4 z E A2 B|"Am" c3 B2 A B2 A|"G" G2 B E2 E A2 B|"F" c3 B2 c d2 G|"C" e3 z2 d c2 B|"Am" c3 B2 A B2 A|"G" G2 B E2 E A2 B|"F" c3 B2 A G2 B|"Am" A3 z2 A A2 B|"Am" c3 B2 A B2 A|"G" G2 B E2 E A2 B|"F" c3 B2 c d2 G|"C" e3 z2 d c2 B|"Am" c3 B2 A B2 A|"G" G2 B E2 E A2 B|"F" c3 B2 A G2 B|"Am" A3 z2 A A2 c|"Am" e3 ^d3 B2 =d|"G" c3 B3 A2 B|"F" c3 B2 c d2 G|"C" e2 d c2 B c2 d|"Am" e3 ^d3 B2 =d|"G" c3 B3 A2 B|"F" c3 B2 A G2 B|"Am" A3 z2 A A2 c|"Am" e3 ^d3 B2 =d|"G" c3 B3 A2 B|"F" c3 B2 c d2 G|"C" e2 d c2 B c2 d|"Am" e3 ^d3 B2 =d|"G" c3 B3 A2 B|"F" c3 B2 A G2 B|"Am" A3 A,6')

Ode_to_joy = Tune(title = "Ode to Joy", note_count = 4, bars = 4, note_duration = 1, note_bar = 4, key = 'C', 
    measures = [
        Measure(chord = "C", symbols = [
            Symbol("E"), Symbol("E"), Symbol("F"), Symbol("G")]),
        Measure(chord = "C", symbols = [
            Symbol("G"), Symbol("F"), Symbol("E"), Symbol("D")]),
        Measure(chord = "C", symbols = [
            Symbol("C"), Symbol("C"), Symbol("D"), Symbol("E")]),
        Measure(chord = "G", symbols = [
            Symbol("E", "3/2"), Symbol("D", "1/2"), Symbol("D", "2")]),
        Measure(chord = "C", symbols = [
            Symbol("E"), Symbol("E"), Symbol("F"), Symbol("G")]),
        Measure(chord = "C", symbols = [
            Symbol("G"), Symbol("F"), Symbol("E"), Symbol("D")]),
        Measure(chord = "C", symbols = [
            Symbol("C"), Symbol("C"), Symbol("D"), Symbol("E")]),
        Measure(chord = "C", symbols = [
            Symbol("D", "3/2"), Symbol("C", "1/2"), Symbol("C", "2")]),
])

Twinkle = Tune(title = "Twinkle", note_count = 2, bars = 4, note_duration = 1, note_bar = 4, key = 'C',
    measures = [
        Measure(chord = "C", symbols = [
            Symbol("C"), Symbol("C")]),
        Measure(chord = "C", symbols = [
            Symbol("G"), Symbol("G")]),
        Measure(chord = "F", symbols = [
            Symbol("A"), Symbol("A")]),
        Measure(chord = "C", symbols = [
            Symbol("G", "2")]),
        Measure(chord = "F", symbols = [
            Symbol("F"), Symbol("F")]),
        Measure(chord = "C", symbols = [
            Symbol("E"), Symbol("E")]),
        Measure(chord = "G", symbols = [
            Symbol("D"), Symbol("D")]),
        Measure(chord = "C", symbols = [
            Symbol("C", "2")]),
        Measure(chord = "C", symbols = [
            Symbol("G"), Symbol("G")]),
        Measure(chord = "F", symbols = [
            Symbol("F"), Symbol("F")]),
        Measure(chord = "C", symbols = [
            Symbol("E"), Symbol("E")]),
        Measure(chord = "G", symbols = [
            Symbol("D", "2")]),
        Measure(chord = "C", symbols = [
            Symbol("G"), Symbol("G")]),
        Measure(chord = "F", symbols = [
            Symbol("F"), Symbol("F")]),
        Measure(chord = "C", symbols = [
            Symbol("E"), Symbol("E")]),
        Measure(chord = "G", symbols = [
            Symbol("D", "2")]),
        Measure(chord = "C", symbols = [
            Symbol("C"), Symbol("C")]),
        Measure(chord = "C", symbols = [
            Symbol("G"), Symbol("G")]),
        Measure(chord = "F", symbols = [
            Symbol("A"), Symbol("A")]),
        Measure(chord = "C", symbols = [
            Symbol("G", "2")]),
        Measure(chord = "F", symbols = [
            Symbol("F"), Symbol("F")]),
        Measure(chord = "C", symbols = [
            Symbol("E"), Symbol("E")]),
        Measure(chord = "G", symbols = [
            Symbol("D"), Symbol("D")]),
        Measure(chord = "C", symbols = [
            Symbol("C", "2")])
])
