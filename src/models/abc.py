""" ABC_PREFIX and WEIGHTS are kept here """
ABC_PREFIX = ("X:1\n"
              "T:{}\n"
              "M:{}/{}\n"
              "L:{}/{}\n"
              "K:{}\n"
              "{}")

WEIGHTS = {}
# WEIGHTS['NOTE'] = random.sample(list(range(100)), 8)
WEIGHTS['NOTE'] = [10, 10, 10, 10, 10, 10, 10, 10]
# WEIGHTS['CHORD'] = [x + y for x, y in zip(WEIGHTS['NOTE'][:7],
# WEIGHTS['NOTE'][7:-1])]
WEIGHTS['CHORD'] = WEIGHTS['NOTE'][:-1]
WEIGHTS['PITCH_P'] = [60, 10, 10, 10]

WEIGHTS['PITCH_S'] = [80, 10]
WEIGHTS['LENGTH'] = [55, 34, 21, 13, 8, 5, 3, 2, 2, 1, 1]
