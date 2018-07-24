import random 
from copy import deepcopy

from models.tune import Tune

class Genetic():
    """docstring for Genetic"""
    def __init__(self, dest, key, note_count, note_bar, bars, WEIGHTS, count = 100, max_gen = 100):
        self.WEIGHTS = WEIGHTS
        self.key = key
        self.note_count = note_count
        self.note_bar = note_bar
        self.bars = bars
        self.dest = dest
        self.count = count
        self.max_gen = max_gen
        
    def run(self, count):
        self.gen = 0
        tune_list = [Tune(note_count = self.note_count, note_bar = self.note_bar, bars = self.bars, key = self.key, gen = True, count = count, WEIGHTS = self.WEIGHTS) for _ in range(self.count)]
        self.best = min([tune for tune in tune_list], key = lambda x: x.dist(self.dest))
        self.best_dist = self.best.dist(self.dest)

        yield self.gen, self.best_dist, self.best
        
        while self.best_dist > 0 and self.gen < self.max_gen:
            best_children = [deepcopy(self.best) for _ in range(self.count)]

            [best.lock_measures(self.dest) for best in best_children]
            [best.mutate(count = random.randint(1, 2)) for best in best_children]

            best_child = min([best for best in best_children], key = lambda x: x.dist(self.dest))

            if self.best_dist > best_child.dist(self.dest):
                self.best_dist = best_child.dist(self.dest)
                self.best = best_child
                self.gen += 1
                yield self.gen, self.best_dist, self.best
