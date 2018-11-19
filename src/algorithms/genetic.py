import random
from copy import deepcopy

from models.tune import Tune


class Genetic():
    """docstring for Genetic"""

    def __init__(self, dest, WEIGHTS, count=None,
                 max_gen=None, seed=None, cost=None):
        self.WEIGHTS = WEIGHTS
        self.dest = dest
        self.count = count if count else 100
        self.max_gen = max_gen if max_gen else 100
        self.cost = cost if cost else 0
        if seed:
            random.seed(seed)

    def run(self):
        # Generate the initial population
        self.gen = 0
        tune_list = [
            Tune(
                note_count=self.dest.note_count,
                note_duration=self.dest.note_duration,
                note_bar=self.dest.note_bar,
                bars=self.dest.bars,
                key=self.dest.key,
                gen=True,
                count=len(
                    self.dest),
                WEIGHTS=self.WEIGHTS) for _ in range(
                self.count)]

        # Compute fitness
        fit = sorted([tune for tune in tune_list],
                     key=lambda x: x.dist(self.dest))
        self.best = fit[0]
        self.best_dist = fit[0].dist(self.dest)

        yield self.gen, self.best_dist, self.best

        while self.gen < self.max_gen and self.best_dist > self.cost:
            # Selection
            parent1 = fit[0]
            parent2 = fit[random.randint(1, 5)]

            # Crossover
            children = parent1.crossover(parent2, double_point=True)

            new = []
            
            if children:
                new = [*children]

                # Mutate children
                for child in children:
                    mutated = deepcopy(child)
                    child.lock_measures(self.dest)
                    child.mutate()
                    new.append(mutated)

            # Select and mutate
            for _ in range(round(self.count / 2) + self.gen):
                mutated = deepcopy(fit[random.randint(0, 3)])
                mutated.lock_measures(self.dest)
                mutated.mutate(count=random.choices([1, 2, 3], [90, 0, 0])[0])
                new.append(mutated)

            # Unfit die
            fit = fit[:len(new) * -1]
            fit.extend(new)

            # Compute fitness
            fit = sorted([tune for tune in fit],
                         key=lambda x: x.dist(self.dest))

            # yield gen, best cost, and best tune if the new best fit is better
            # than the old best
            if self.best_dist > fit[0].dist(self.dest):
                self.best = fit[0]
                self.best_dist = fit[0].dist(self.dest)
                self.gen += 1
                yield self.gen, self.best_dist, self.best
