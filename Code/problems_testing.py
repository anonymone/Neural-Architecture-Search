from problems import DTLZ1
import numpy as np

problem = DTLZ1.DTLZ1()
population,boundary,coding = problem.init(generation_size=100)

print("population = \n {0}".format(population))
print("Value = \n {0}".format(problem.value(population)))