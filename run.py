from problems import DTLZ1
from algorithms import NSGAII

if __name__ == "__main__":
    problem = DTLZ1.DTLZ1()
    population, boundary, coding = problem.init(generation_size=10)
    func_value = problem.value(population)
    NSGAII.fast_non_dominated_sort(func_value)