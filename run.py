from problems import DTLZ1
from algorithms import NSGAII
import numpy as np
if __name__ == "__main__":
    problem = DTLZ1.DTLZ1(M=3)
    population, boundary, coding = problem.init(generation_size=1000)
    func_value = problem.value(population)

    # func_value = [ [39.45757807, 109.22284033], 
    #                 [2.86965248,  91.65383822],
    #                 [229.9125652,   33.88312065],
    #                 [175.35145278, 196.53583365],
    #                 [143.62980809, 123.4551886],  
    #                 [68.24446104, 203.41141973],
    #                 [363.35745327,  36.28574311],
    #                 [56.44501436, 253.76417207], 
    #                 [187.71003021,  34.78490607],
    #                 [155.58596971, 56.68474627]]
    # func_value = np.array(func_value)

    print('func_value = \n{0}'.format(func_value))
    Front,rank = NSGAII.fast_non_dominated_sort(func_value)
    print('Rank = \n{0}'.format(rank))
    crowd_distance = NSGAII.crowding_distance(func_value)
    print('crowd_distance = \n{0}'.format(crowd_distance))
