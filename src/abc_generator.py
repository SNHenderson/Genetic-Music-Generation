import random 
from copy import copy, deepcopy
import matplotlib.pyplot as plt
import cProfile

from models.abc import ABC_PREFIX, WEIGHTS
from models.tune import Tune
from models.measure import Measure
from models.symbol import Symbol
from songs import songs
from utils import argparser
from algorithms.genetic import Genetic

def run():
    # parse arguments
    args = argparser.parse()
    
    big_tune = ""
    try:
        song = getattr(songs, args.song)
    except:
        raise Exception("Song '{}' does not exist".format(args.song))

    gen = Genetic(song, WEIGHTS = WEIGHTS, count = args.population, max_gen = args.max, seed = args.seed, cost = args.cost)
    gen_log = []
    cost_log = []
    for generation in gen.run():
        gen_log.append(generation[0])
        cost_log.append(generation[1])
        print("Generation: {:4d} | Cost: {:3d} | Best: {}".format(*generation))
        if not gen.gen % 10:
            big_tune += "| " + str(gen.best)
    
    if gen.gen % 10:
        big_tune += "| " + str(gen.best)

    best = ABC_PREFIX.format(song.title + " evolved", song.note_count, song.bars, song.note_duration, song.note_bar, song.key, big_tune + " |]")

    with open('generated_songs/{}.abc'.format('evolved'), 'w') as file:
        file.write(best)
    
    print('\n')
    print(best)

    plt.plot(gen_log, cost_log)
    plt.axis([0, max(gen_log), 0, max(cost_log) + 50])
    plt.show()

if __name__ == "__main__":
    cProfile.run('run()', sort = 'cumtime')
