from models.measure import Measure
from models.symbol import Symbol
from models.tune import Tune

"""Tunes are encoded in this file"""
Marimba_3 = Tune(
	title = "marimba_test",
	note_count=5,
	bars=4,
	note_duration=1,
	note_bar=16,
	key='B',
	string=('"B" F F F F F F F F F F F F F F F F F F F F|"B" F F F F F F F F F F F F F F F F F F F F|"B" F F F F F F F F F F F F F F F F F F F F'))

Marimba_2 = Tune(
	title = "marimba_test",
	note_count=5,
	bars=4,
	note_duration=1,
	note_bar=16,
	key='B',
	string=('"B" D D D D D D D D D D D D D D D D D D D D|"B" D D D D D D D D D D D D D D D D D D D D|"B" D D D D D D D D D D D D D D D D D D D D'))

Marimba = Tune(
	title = "marimba_test",
	note_count=5,
	bars=4,
	note_duration=1,
	note_bar=16,
	key='B',
	string=('"B" B B B B B B B B B B B B B B B B B B B B|"B" B B B B B B B B B B B B B B B B B B B B|"B" B B B B B B B B B B B B B B B B B B B B'))

Invention_0 = Tune(
	title = "i_1",
	note_count=4,
	bars=4,
	note_duration=1,
	note_bar=4,
	key='G',
	string=('"Bm" b1/2 b b c\'1/2 b|"Fdim" a1/2 g f g1/2 a|"G" b1/2 a g f1/2 g|"Em" e1/2 e e f1/2 g1/2 a1/2'))

Invention_4 = Tune(
	title = "i_4",
	note_count=4,
	bars=4,
	note_duration=1,
	note_bar=4,
	key='G',
	string=('"Fdim" f4|"C" c4|"D" d4|"Bm" B4|"Fdim" f4|"C" c4|"D" d4|"Bm" B4'))

Invention_3 = Tune(
	title = "i_3",
	note_count=4,
	bars=4,
	note_duration=1,
	note_bar=4,
	key='G',
	string=('"D" d4|"Am" A4|"C" c4|"G" G4|"D" d4|"Am" A4|"C" c4|"G" G4'))

Invention_2 = Tune(
	title = "i_2",
	note_count=4,
	bars=4,
	note_duration=1,
	note_bar=4,
	key='G',
	string=('"C" c4|"G" G4|"Bm" B4|"Fdim" F4|"C" c4|"G" G4|"Bm" B4|"Fdim" F4'))

Invention_1 = Tune(
	title = "i_1",
	note_count=4,
	bars=4,
	note_duration=1,
	note_bar=4,
	key='G',
	string=('"Bm" B4|"Fdim" F4|"G" G4|"Em" E4|"Bm" B4|"Fdim" F4|"G" G4|"Em" E4'))

DiesIrae = Tune(
    title="Dies Irae",
    note_count=6,
    bars=8,
    note_duration=1,
    note_bar=4,
    key='F',
    string=('"Dm" F3|"Dm" E3|"Dm" F3|"Dm" D3|"Dm" E3|"Dm" C3|"Dm" D3|"Dm" D3|'
            '"Dm" F3|"Dm" F3|"Dm" G3|"Dm" F3|"Dm" E3|"Dm" D3|"Dm" C3|"Dm" E3|"Dm" F3|"Dm" E3|"Dm" E3|"Dm" D3|"Dm" D3|"Dm" D3'))

Mandad = Tune(
    title="Mandad'ei comigo",
    note_count=3,
    bars=4,
    note_duration=1,
    note_bar=4,
    key='C',
    string=('"G" B G2|"G" A B2|"G" B d2|"G" c B A|"G" B A3/2 G1/2|"G" G3|'
            '"G" A G2|"G" A B2|"G" B d2|"G" c B A|"G" G3|"F" G F2|'
            '"G" G A2|"G" B3|"G" A G2|"F" A G F|"G" G A1/2 B1/2 c|"G" B A B|"G" G3'))

pan_16 = Tune(
    title="Panning",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" z4 z2 z2 z4 z z z B|"B" z4 z2 z2 z4 z z z B'))

pan_15 = Tune(
    title="Panning",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" z4 z2 z2 z4 z z B z|"B" z4 z2 z2 z4 z z B z'))

pan_14 = Tune(
    title="Panning",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" z4 z2 z2 z4 z B z z|"B" z4 z2 z2 z4 z B z z'))

pan_13 = Tune(
    title="Panning",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" z4 z2 z2 z4 B z z z|"B" z4 z2 z2 z4 B z z z'))

pan_12 = Tune(
    title="Panning",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" z4 z4 z z z B z4|"B" z4 z4 z z z B z4'))

pan_11 = Tune(
    title="Panning",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" z4 z4 z z B z4 z|"B" z4 z4 z z B z4 z'))

pan_10 = Tune(
    title="Panning",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" z4 z4 z B z4 z z|"B" z4 z4 z B z4 z z'))

pan_9 = Tune(
    title="Panning",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" z4 z4 B z4 z z z|"B" z4 z4 B z4 z z z'))

pan_8 = Tune(
    title="Panning",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" z4 z z z B z4 z4|"B" z4 z z z B z4 z4'))

pan_7 = Tune(
    title="Panning",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" z4 z z B z4 z4 z|"B" z4 z z B z4 z4 z'))

pan_6 = Tune(
    title="Panning",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" z4 z B z4 z4 z z|"B" z4 z B z4 z4 z z'))

pan_5 = Tune(
    title="Panning",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" z4 B z4 z4 z z z|"B" z4 B z4 z4 z z z'))

pan_4 = Tune(
    title="Panning",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" z z z B z4 z2 z2 z4|"B" z z z B z4 z2 z2 z4'))

pan_3 = Tune(
    title="Panning",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" z z B z4 z2 z2 z4 z|"B" z z B z4 z2 z2 z4 z'))

pan_2 = Tune(
    title="Panning",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" z B z4 z2 z2 z4 z z|"B" z B z4 z2 z2 z4 z z'))

pan_1 = Tune(
    title="Panning",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" B z4 z2 z2 z4 z z z|"B" B z4 z2 z2 z4 z z z'))

Clarinet_2 = Tune(
    title="Clarinet research",
    note_count=3,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" B D F B D F B D F B D F'))

Clarinet = Tune(
    title="Clarinet research",
    note_count=3,
    bars=4,
    note_duration=1,
    note_bar=16,
    key="B",
    string=('"B" B B B B B B B B B B B B'))

Lichfield = Tune(
    title="Lichfield",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=8,
    key='G',
    string=('"G" G2 G A B2 G2|"C" E2 c c c4|"D" D2 D E F2 c2|"D" B4 A4|'
            '"G" G2 G A B2 G2|"C" E2 c c c4|"D" D2 D E F2 G A|"G" A4 G4|'
            '"G" d2 d d c2 c2|"D" B c d B A4|"G" d2 d d c2 c c|"D" B4 A4|'
            '"G" G2 G A B2 G2|"C" E2 c c c4|"D" D2 D E F2 G A|"G" A4 G4'))

Mazurka = Tune(
    title="Mazurka : Boite de Jazz",
    note_count=9,
    bars=8,
    note_duration=1,
    note_bar=8,
    key='C',
    string=('"Am" z4 z E A2 B|"Am" c3 B2 A B2 A|"G" G2 B E2 E A2 B|'
            '"F" c3 B2 c d2 G|"C" e3 z2 d c2 B|"Am" c3 B2 A B2 A|'
            '"G" G2 B E2 E A2 B|"F" c3 B2 A G2 B|"Am" A3 z2 A A2 B|'
            '"Am" c3 B2 A B2 A|"G" G2 B E2 E A2 B|"F" c3 B2 c d2 G|'
            '"C" e3 z2 d c2 B|"Am" c3 B2 A B2 A|"G" G2 B E2 E A2 B|'
            '"F" c3 B2 A G2 B|"Am" A3 z2 A A2 c|"Am" e3 ^d3 B2 =d|'
            '"G" c3 B3 A2 B|"F" c3 B2 c d2 G|"C" e2 d c2 B c2 d|'
            '"Am" e3 ^d3 B2 =d|"G" c3 B3 A2 B|"F" c3 B2 A G2 B|'
            '"Am" A3 z2 A A2 c|"Am" e3 ^d3 B2 =d|"G" c3 B3 A2 B|'
            '"F" c3 B2 c d2 G|"C" e2 d c2 B c2 d|"Am" e3 ^d3 B2 =d|'
            '"G" c3 B3 A2 B|"F" c3 B2 A G2 B|"Am" A3 A,6'))

Ode_to_joy = Tune(
    title="Ode to Joy",
    note_count=4,
    bars=4,
    note_duration=1,
    note_bar=4,
    key='C',
    measures=[
        Measure(chord="C", symbols=[
            Symbol("E"), Symbol("E"), Symbol("F"), Symbol("G")]),
        Measure(chord="C", symbols=[
            Symbol("G"), Symbol("F"), Symbol("E"), Symbol("D")]),
        Measure(chord="C", symbols=[
            Symbol("C"), Symbol("C"), Symbol("D"), Symbol("E")]),
        Measure(chord="G", symbols=[
            Symbol("E", "3/2"), Symbol("D", "1/2"), Symbol("D", "2")]),
        Measure(chord="C", symbols=[
            Symbol("E"), Symbol("E"), Symbol("F"), Symbol("G")]),
        Measure(chord="C", symbols=[
            Symbol("G"), Symbol("F"), Symbol("E"), Symbol("D")]),
        Measure(chord="C", symbols=[
            Symbol("C"), Symbol("C"), Symbol("D"), Symbol("E")]),
        Measure(chord="C", symbols=[
            Symbol("D", "3/2"), Symbol("C", "1/2"), Symbol("C", "2")])])

Twinkle = Tune(
    title="Twinkle",
    note_count=2,
    bars=4,
    note_duration=1,
    note_bar=4,
    key='C',
    measures=[
        Measure(chord="C", symbols=[
            Symbol("C"), Symbol("C")]),
        Measure(chord="C", symbols=[
            Symbol("G"), Symbol("G")]),
        Measure(chord="F", symbols=[
            Symbol("A"), Symbol("A")]),
        Measure(chord="C", symbols=[
            Symbol("G", "2")]),
        Measure(chord="F", symbols=[
            Symbol("F"), Symbol("F")]),
        Measure(chord="C", symbols=[
            Symbol("E"), Symbol("E")]),
        Measure(chord="G", symbols=[
            Symbol("D"), Symbol("D")]),
        Measure(chord="C", symbols=[
            Symbol("C", "2")]),
        Measure(chord="C", symbols=[
            Symbol("G"), Symbol("G")]),
        Measure(chord="F", symbols=[
            Symbol("F"), Symbol("F")]),
        Measure(chord="C", symbols=[
            Symbol("E"), Symbol("E")]),
        Measure(chord="G", symbols=[
            Symbol("D", "2")]),
        Measure(chord="C", symbols=[
            Symbol("G"), Symbol("G")]),
        Measure(chord="F", symbols=[
            Symbol("F"), Symbol("F")]),
        Measure(chord="C", symbols=[
            Symbol("E"), Symbol("E")]),
        Measure(chord="G", symbols=[
            Symbol("D", "2")]),
        Measure(chord="C", symbols=[
            Symbol("C"), Symbol("C")]),
        Measure(chord="C", symbols=[
            Symbol("G"), Symbol("G")]),
        Measure(chord="F", symbols=[
            Symbol("A"), Symbol("A")]),
        Measure(chord="C", symbols=[
            Symbol("G", "2")]),
        Measure(chord="F", symbols=[
            Symbol("F"), Symbol("F")]),
        Measure(chord="C", symbols=[
            Symbol("E"), Symbol("E")]),
        Measure(chord="G", symbols=[
            Symbol("D"), Symbol("D")]),
        Measure(chord="C", symbols=[
            Symbol("C", "2")])])
