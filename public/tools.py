'''
[INTRO] Useful tools in EAs
[CONTRIBUTOR OF CODE] Severus Peng
'''

import numpy as np

# domination testing 
# INPUT: two same-scale solutions p & q
# OOUTPUT: Boolean True  is p  < q, 
#                  False is p !< q
def is_dominate(p,q):
    tag = p < q
    if tag.all():
        return True
    else:
        return False

# matrix sorting order by column
# INPUT: a vector
# OUTPUT: sorted vector & index of previous index(rank)
def sort(p):
    index = np.array([ x for x in range(p.shape[0])])
    index = index.reshape(index.shape[0],1)
    p = np.hstack((p,index))
    p = p[np.lexsort(p[:,::-1].T)]
    rank = p[:,1]
    rank = rank.astype(int)
    return p[:,0],rank

# normalized
# INPUT: a ndarray
# OUTPUT: normalized ndarray
def normalized(p):
    p = (p - np.min(p))/(np.max(p)-np.min(p))
    return p.reshape(p.shape[0],1)

def mating_pool(population, popu_rank, crow_distance):
    pool = np.zeros(population.shape)
    for i in range(int(population.shape[0])):
        select1,select2 = np.random.randint(0,population.shape[0]-1,2)
        if popu_rank[select1] < popu_rank[select2]:
            pool[i,:] = population[select1, :]
        elif popu_rank[select1] > popu_rank[select2]:
            pool[i,:] = population[select2, :]
        else:
            if crow_distance[select1] > crow_distance[select2]:
               pool[i,:] = population[select1,:]
            else:
                pool[i,:] = population[select2,:]
    return pool