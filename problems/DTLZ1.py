'''
[INTRO] DTLZ1 is an M-objective problems with a linear  Pareto-optimal front.
[REFERRENCE]: Deb, Kalyanmoy, et al. Scalable Test Problems for Evolutionary Multiobjective Optimization. Evolutionary Multiobjective Optimization. 2005:105-145.
'''

import numpy as np


class DTLZ1:
    # init problem setting 
    # k : the number of Xm's variables
    # M : the number of objections
    def __init__(self, k = 5, M =2):
        # Default setting k =5 M = 2
        self.k = k
        self.M = M

    # init the first population with size of generation_size
    # INPUT: generation size (int)
    # OUTPUT: 
    #        population (np.array)
    #        Boundary   ([Max,Min])
    #        coding method  (string)
    def init(self, generation_size = 100): 
        n = self.M + self.k -1
        max_boundary = np.ones([1,n])
        min_boundary = np.zeros([1,n])
        population = np.random.rand(generation_size, n)
        coding = 'Real'
        return population,[max_boundary,min_boundary],coding

    # get the problem's Value of population
    # INPUT:    population     (np.array)
    # OUTPUT:   Problem result (np.array)
    def value(self, population):
        problem_values = np.zeros([population.shape[0], self.M])
        gx = 100 * (self.k + np.sum((population[:,self.M-1:]-0.5)**2-np.cos(20*np.pi*(population[:,self.M-1:]-0.5)),axis=1))
        gx = gx.reshape(gx.shape[0],1)
        for i in range(self.M):
            problem_values[:,i] = np.prod(population[:,0:self.M-1-i],axis=1)
            if i > 0:
                problem_values[:,i] = problem_values[:,i]*(1-population[:,self.M-1-i])
        problem_values = problem_values*0.5*(1+gx)
        return problem_values
