import cProfile

import matplotlib.pyplot as plt

from algorithms.genetic import Genetic
from models.abc import ABC_PREFIX, WEIGHTS
from songs import songs
from utils import argparser


def run():
    """Runs the algorithm and saves the song """

    # parse arguments
    args = argparser.parse()

    # big_tune = ""
    big_tune = []

    # load song
    try:
        song = getattr(songs, args.song)
    except BaseException:
        raise Exception("Song '{}' does not exist".format(args.song))

    # load variables
    title = args.title if args.title else 'evolved'
    generation_n = args.number if args.number else 10

    # init genetic algorithm and log
    gen = Genetic(
        song,
        WEIGHTS=WEIGHTS,
        count=args.population,
        max_gen=args.max,
        seed=args.seed,
        cost=args.cost)
    gen_log = []
    cost_log = []

    # run algorithm, adding every nth generation to the big tune
    for generation in gen.run():
        gen_log.append(generation[0])
        cost_log.append(generation[1])
        print("Generation: {:4d} | Cost: {:3d} | Best: {}".format(*generation))
        if not gen.gen % generation_n:
            big_tune.append(gen.best)
            #big_tune += "| " + str(gen.best)

    # add final song to tune
    if gen.gen % generation_n or gen.best_dist != 0:
        big_tune.append(song)
        #big_tune += "| " + str(song)

    # format as ABC notation
    if args.reverse:
        big_tune.reverse()

    best = ABC_PREFIX.format(
        song.title + " " + title,
        song.note_count,
        song.bars,
        song.note_duration,
        song.note_bar,
        song.key,
        "\n| ".join([str(gen) for gen in big_tune]) + " |]")
        #big_tune + " |]")

    # Save song
    with open('generated_songs/{}.abc'.format(title), 'w') as file:
        file.write(best)

    # Display song in console
    print('\n')
    print(best)

    # Plot and display log
    plt.plot(gen_log, cost_log)
    plt.axis([0, max(gen_log), 0, max(cost_log) + 50])
    plt.show()


# If run with python abc_generator.py, run a profile and sort by
# cumulative time
if __name__ == "__main__":
    cProfile.run('run()', sort='cumtime')
