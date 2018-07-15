from problems import DTLZ1
from algorithms import NSGAII
from public import tools
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    plt.ion()
    plt.xlim([0,1])
    plt.ylim([0,1])

    problem = DTLZ1.DTLZ1(M=3)
    algorithm = NSGAII
    generations = 1000
    N = 100
    M = 2
    k = 5
    problem = DTLZ1.DTLZ1(k=k,M=M)
    population, boundary, coding = problem.init(generation_size=N) 
    for i in range(generations):
        # print('generations:{0}'.format(i))
        func_value = problem.value(population)
        # if i%1 == 0:
        func_value_normal = tools.normalized(func_value)
        plt.cla()
        plt.scatter(func_value_normal[:,0],func_value_normal[:,1])
        plt.show()
        plt.pause(0.00001)

        Front, rank = algorithm.fast_non_dominated_sort(func_value)
        crowd_distance = algorithm.crowding_distance(func_value)
        mating_p = tools.mating_pool(population, rank, crowd_distance)
        offspring = tools.real_cross_over(parent=mating_p)
        # offspring = tools.real_mutation(offspring, boundary)

        parent_offspring = np.vstack([population,offspring])
        func_value = problem.value(parent_offspring)
        Front, rank = algorithm.fast_non_dominated_sort(func_value)
        counter = 0
        new_generation_index = list()
        for i in Front:
            counter = counter + len(Front[i])
            if counter > N:
                counter = i
                break
            new_generation_index.extend(Front[i])
        crowd_distance = algorithm.crowding_distance(func_value[Front[counter],:])
        crowd_distance_index = np.argsort(crowd_distance)
        new_generation_index.extend(crowd_distance_index[0:(N-len(new_generation_index))])
        population = parent_offspring[new_generation_index,:]