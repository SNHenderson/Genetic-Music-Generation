from models.tune import Tune
from models.measure import Measure
from models.symbol import Symbol

ode_to_joy = Tune(measures = [
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

twinkle = Tune(measures = [
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
