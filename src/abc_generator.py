import random 
from copy import copy, deepcopy
import matplotlib.pyplot as plt
import cProfile

from models.abc import ABC_PREFIX
from models.tune import Tune
from models.measure import Measure
from models.symbol import Symbol
from songs.songs import Mazurka
from songs.songs import Lichfield
from algorithms.genetic import Genetic

def run():
    WEIGHTS = {}
    CHOICES = {}
    #WEIGHTS['NOTE'] = random.sample(list(range(100)), 8)
    WEIGHTS['NOTE'] = [10, 10, 10, 10, 10, 10, 10, 10]
    #WEIGHTS['CHORD'] = [x + y for x, y in zip(WEIGHTS['NOTE'][:7], WEIGHTS['NOTE'][7:-1])]
    WEIGHTS['CHORD'] = WEIGHTS['NOTE'][:-1]
    WEIGHTS['PITCH_P'] = [60, 10, 10, 10]

    WEIGHTS['PITCH_S'] = [80, 10]
    WEIGHTS['LENGTH'] = [55, 34, 21, 13, 8, 5, 3, 2, 2, 1]
    
    big_tune = ""
    song = Lichfield
    gen = Genetic(song, WEIGHTS = WEIGHTS, count = 75, max_gen = 1000, seed = 0)
    gen_log = []
    cost_log = []
    for generation in gen.run():
        gen_log.append(generation[0])
        cost_log.append(generation[1])
        print("Generation: {}       | Cost: {}      | Best: {}".format(*generation))
        if not gen.gen % 10:
            big_tune += "| " + str(gen.best)
    
    if gen.gen % 10:
        big_tune += "| " + str(gen.best)

    best = ABC_PREFIX.format(song.title + " evolved", song.note_count, song.bars, song.note_duration, song.note_bar, song.key, big_tune + " |]")

    with open('best.abc', 'w') as file:
        file.write(best)
    
    print('\n')
    print(best)

    plt.plot(gen_log, cost_log)
    plt.axis([0, max(gen_log), 0, max(cost_log) + 50])
    plt.show()

if __name__ == "__main__":
    cProfile.run('run()', sort = 'cumtime')
