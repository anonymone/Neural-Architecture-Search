'''
[INTRO] 
[REFERRENCE]: 
[CONTRIBUTION OF CODE] Severus Peng
'''

import numpy as np

def is_dominate(p,q):
    # if p is None or q is None:
    #     return False
    tag = p < q
    if tag.all():
        return True
    else:
        return False
        

def fast_non_dominated_sort(population_value):
    Sp = dict()
    Np = np.zeros(population_value.shape[0])
    Prank = np.zeros(population_value.shape[0])
    Fi = dict()
    Fi[1] = list()
    for p in range(population_value.shape[0]):
        Sp[p] = list()
        for q in range(population_value.shape[0]):
            if is_dominate(population_value[p],population_value[q]):
                Sp[p].append(population_value[q])
            else:
                Np[p] = Np[p] + 1
        if Np[p] == 0:
            Prank[p] = 1 
            Fi[1].append(population_value[p])
    i = 1 
    while Fi[i] == []:
        Q = list()
        for p in range(len(Fi[1])):
            for q in range(len(Sp[p])):
                Np[q] = Np[q] - 1
                if Np[q] == 0:
                    Prank[q] = i + 1
                    Q.append(Sp[p][q])
        i = i + 1
        Fi[i] = Q
