import random 
from copy import copy, deepcopy

from models.tune import Tune
from models.measure import Measure
from models.symbol import Symbol
from songs.songs import Lichfield
from algorithms.genetic import Genetic

ABC_PREFIX = ("X:1\n"
              "T:{}\n"
              "M:{}/{}\n"
              "L:{}/{}\n"
              "K:{}\n"
              "{}")

def run():
    WEIGHTS = {}
    CHOICES = {}
    WEIGHTS['NOTE'] = random.sample(list(range(100)), 8)
    #WEIGHTS['NOTE'] = [10, 10, 10, 10, 10, 10, 10, 10]
    #WEIGHTS['CHORD'] = [x + y for x, y in zip(WEIGHTS['NOTE'][:7], WEIGHTS['NOTE'][7:-1])]
    WEIGHTS['CHORD'] = WEIGHTS['NOTE'][:-1]
    WEIGHTS['PITCH_P'] = [60, 10, 10, 10]
    WEIGHTS['PITCH_S'] = [90, 10]
    WEIGHTS['LENGTH'] = [55, 34, 21, 13, 8, 5, 3, 2, 2, 1]

    title = "Test"
    note_count = 4
    note_duration = 1
    bars = 4
    note_bar = 8
    key = 'G'
    measures = 16
    
    big_tune = ""
    gen = Genetic(Lichfield, key = key, note_count = note_count, note_bar = note_bar, bars = bars, WEIGHTS = WEIGHTS, max_gen = 200)

    for generation in gen.run(measures):
        print("Generation: {}       | Cost: {}      | Best: {}".format(*generation))
        if not gen.gen % 10:
            big_tune += "| " + str(gen.best)
    
    if gen.gen % 10:
        big_tune += "| " + str(gen.best)

    tune = big_tune + " |]"
    best = ABC_PREFIX.format(title, note_count, bars, note_duration, note_bar, key, tune)

    with open('best.abc', 'w') as file:
        file.write(best)
    
    print('\n')
    print(best)

if __name__ == "__main__":
    run()
