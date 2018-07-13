from problems import DTLZ1
from algorithms import NSGAII
import numpy as np
if __name__ == "__main__":
    problem = DTLZ1.DTLZ1(M=5)
    population, boundary, coding = problem.init(generation_size=3)
    func_value = problem.value(population)
    print('func_value = \n{0}'.format(func_value))
    Front,rank = NSGAII.fast_non_dominated_sort(func_value)
    print('Rank = \n{0}'.format(rank))
