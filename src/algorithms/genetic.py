import random 
from copy import deepcopy

from models.tune import Tune

class Genetic():
    """docstring for Genetic"""
    def __init__(self, dest, WEIGHTS, count = 100, max_gen = 100, seed = None):
        self.WEIGHTS = WEIGHTS
        self.dest = dest
        self.count = count
        self.max_gen = max_gen
        if seed:
            random.seed(seed)
        
    def run_old(self, count):
        self.gen = 0
        tune_list = [Tune(note_count = self.note_count, note_bar = self.note_bar, bars = self.bars, key = self.key, gen = True, count = count, WEIGHTS = self.WEIGHTS) for _ in range(self.count)]
        self.best = min([tune for tune in tune_list], key = lambda x: x.dist(self.dest))
        self.best_dist = self.best.dist(self.dest)

        yield self.gen, self.best_dist, self.best
        
        while self.best_dist > 0 and self.gen < self.max_gen:
            best_children = [deepcopy(self.best) for _ in range(self.count)]

            for best in best_children:
                best.lock_measures(self.dest)
                best.mutate(count = random.choices([1, 2, 3], [70, 20, 0])[0])

            best_child = min(best_children, key = lambda x: x.dist(self.dest))

            if self.best_dist > best_child.dist(self.dest):
                self.best_dist = best_child.dist(self.dest)
                self.best = best_child
                self.gen += 1
                yield self.gen, self.best_dist, self.best

    def run(self):
        # Generate the initial population
        self.gen = 0
        tune_list = [Tune(note_count = self.dest.note_count, note_duration = self.dest.note_duration, note_bar = self.dest.note_bar, bars = self.dest.bars, key = self.dest.key, gen = True, count = len(self.dest), WEIGHTS = self.WEIGHTS) for _ in range(self.count)]
        
        # Compute fitness
        fit = sorted([tune for tune in tune_list], key = lambda x: x.dist(self.dest))
        new_fit = []
        self.best = fit[0]
        self.best_dist = fit[0].dist(self.dest)

        yield self.gen, self.best_dist, self.best

        while self.best_dist > 0 and self.gen < self.max_gen:
            #Selection
            parent1 = fit[0]
            # print(parent1)
            parent2 = fit[random.randint(1,3)]
            # print(parent2)
            #Crossover
            children = parent1.crossover(parent2)
                
            if children:
                new_fit.extend([*children])

            for child in children:
                mutated = deepcopy(child)
                child.lock_measures(self.dest)
                child.mutate()
                new_fit.append(mutated)

            for _ in range(round(self.count / 2) + self.gen):
                mutated = deepcopy(fit[random.randint(0, 3)])
                mutated.lock_measures(self.dest)
                mutated.mutate(count = random.choices([1, 2, 3], [90, 0, 0])[0])
                new_fit.append(mutated)
            
            # mutated = [deepcopy(tune) for tune in fit[:round(self.count / 2)]]

            # for best in mutated:
            #     best.lock_measures(self.dest)
            #     best.mutate(count = random.choices([1, 2, 3], [70, 0, 0])[0])
            
            # new_fit.extend(mutated)
            
            #Unfit die
            fit = fit[:len(new_fit) * -1]
            fit.extend(new_fit)
            new_fit = []
            
            #Compute fitness
            fit = sorted([tune for tune in fit], key = lambda x: x.dist(self.dest))
            
            if self.best_dist > fit[0].dist(self.dest):
                self.best = fit[0]
                self.best_dist = fit[0].dist(self.dest)
                self.gen += 1
                yield self.gen, self.best_dist, self.best
