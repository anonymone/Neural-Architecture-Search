import numpy as np


class DTLZ1:
    def __init__(self, k = 5, M =2):
        # Default
        self.k = k
        self.M = M
        
    def init(self, generation_size = 100): 
        n = self.M + self.k -1
        max_boundary = np.ones([1,n])
        min_boundary = np.zeros([1,n])
        population = np.random.rand(generation_size, n)
        coding = 'Real'
        return population,[max_boundary,min_boundary],coding

    def value(self, population):
        function_value = np.zeros([population.shape[0], self.M])
        gx = 100 * (self.k + np.sum((population[:,self.M-1:]-0.5)**2-np.cos(20*np.pi*(population[:,self.M-1:]-0.5)),axis=1))
        gx = gx.reshape(gx.shape[0],1)
        for i in range(self.M):
            function_value[:,i] = np.prod(population[:,0:self.M-1-i],axis=1)
            if i > 0:
                function_value[:,i] = function_value[:,i]*(1-population[:,self.M-1-i])
        function_value = function_value*0.5*(1+gx)
        return function_value
