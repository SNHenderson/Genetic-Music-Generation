import random 
from copy import deepcopy

from models.tune import Tune

class Genetic():
    """docstring for Genetic"""
    def __init__(self, dest, WEIGHTS, count, max_gen, seed = None):
        self.WEIGHTS = WEIGHTS
        self.dest = dest
        self.count = count if count else 100
        self.max_gen = max_gen if max_gen else 100
        if seed:
            random.seed(seed)

    def run(self):
        # Generate the initial population
        self.gen = 0
        tune_list = [Tune(note_count = self.dest.note_count, note_duration = self.dest.note_duration, note_bar = self.dest.note_bar, bars = self.dest.bars, key = self.dest.key, gen = True, count = len(self.dest), WEIGHTS = self.WEIGHTS) for _ in range(self.count)]
        
        # Compute fitness
        fit = sorted([tune for tune in tune_list], key = lambda x: x.dist(self.dest))
        new = []
        self.best = fit[0]
        self.best_dist = fit[0].dist(self.dest)

        yield self.gen, self.best_dist, self.best

        while self.best_dist > 0 and self.gen < self.max_gen:
            #Selection
            parent1 = fit[0]
            parent2 = fit[random.randint(1,3)]

            #Crossover
            children = parent1.crossover(parent2)
                
            #Mutate
            if children:
                new.extend([*children])

            for child in children:
                mutated = deepcopy(child)
                child.lock_measures(self.dest)
                child.mutate()
                new.append(mutated)

            for _ in range(round(self.count / 2) + self.gen):
                mutated = deepcopy(fit[random.randint(0, 3)])
                mutated.lock_measures(self.dest)
                mutated.mutate(count = random.choices([1, 2, 3], [90, 0, 0])[0])
                new.append(mutated)
            
            #Unfit die
            fit = fit[:len(new) * -1]
            fit.extend(new)
            new = []
            
            #Compute fitness
            fit = sorted([tune for tune in fit], key = lambda x: x.dist(self.dest))
            
            if self.best_dist > fit[0].dist(self.dest):
                self.best = fit[0]
                self.best_dist = fit[0].dist(self.dest)
                self.gen += 1
                yield self.gen, self.best_dist, self.best
