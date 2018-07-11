import numpy as np

class DTLZ1:
    def __init__(self):
        # Default
        self.k = 5
    def init(self, M = 2, generation_size = 100):
        
        n = M + self.k -1
        max_boundary = np.ones([1,n])
        min_boundary = np.zeros([1,n])
        population = np.random.rand(generation_size, n)
        coding = 'Real'
        return [population,[max_boundary,min_boundary],coding]

    def value(self, population, M = 2):
        function_value = np.zeros([population.shape[0], M])
        gx = 100 * (self.k + np.sum())
