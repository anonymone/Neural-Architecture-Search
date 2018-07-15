'''
[INTRO] Useful tools in EAs
[CONTRIBUTOR OF CODE] Severus Peng
'''

import numpy as np

# domination testing
# INPUT: two same-scale solutions p & q
# OOUTPUT: Boolean True  is p  < q,
#                  False is p !< q


def is_dominate(p, q):
    tag = p < q
    if tag.all():
        return True
    else:
        return False

# matrix sorting order by column
# INPUT: a vector
# OUTPUT: sorted vector & index of previous index(rank)


def sort(p):
    index = np.array([x for x in range(p.shape[0])])
    index = index.reshape(index.shape[0], 1)
    p = np.hstack((p, index))
    p = p[np.lexsort(p[:, ::-1].T)]
    rank = p[:, 1]
    rank = rank.astype(int)
    return p[:, 0], rank

# normalized
# INPUT: a ndarray
# OUTPUT: normalized ndarray


def normalized(p):
    p = (p - np.min(p))/(np.max(p)-np.min(p))
    return p.reshape(p.shape[0], 1)

# mating pool
# INPUT: population:     ndarray
#        pop_rank:       ndarray row vector
#        crow_distance:  ndarray row vector
# OUTPUT:pool：          ndarray paired individuals


def mating_pool(population, popu_rank, crow_distance):
    pool = np.zeros(population.shape)
    for i in range(int(population.shape[0])):
        select1, select2 = np.random.randint(0, population.shape[0]-1, 2)
        if popu_rank[select1] < popu_rank[select2]:
            pool[i, :] = population[select1, :]
        elif popu_rank[select1] > popu_rank[select2]:
            pool[i, :] = population[select2, :]
        else:
            if crow_distance[select1] > crow_distance[select2]:
                pool[i, :] = population[select1, :]
            else:
                pool[i, :] = population[select2, :]
    return pool

# real code cross over
# INPUT: parent:    ndarray
#        proC:      int
#        disC:      int
# OUTPUT:offspring: ndarray


def real_cross_over(parent, proC=1, disC=20):
    N, M = parent.shape
    parent1 = parent[0:int(N/2), :]
    parent2 = parent[int(N/2):, :]
    beta = np.zeros((int(N/2), M))
    mu = np.random.rand(int(N/2), M)
    mu_index = np.where(mu <= 0.5)
    beta[mu_index] = ((2*mu[mu_index])**(1/(disC+1)))
    mu_index = np.where(mu > 0.5)
    beta[mu_index] = (2-2*mu[mu_index])**(-1/(disC+1))
    beta = beta*(-1)**np.random.randint(0, 2, [int(N/2), M])
    mu_index = np.where(np.random.rand(int(N/2), M) < 0.5)
    beta[mu_index] = 1
    beta[np.where(np.tile(np.random.rand(int(N/2), 1) > proC, [1, M]))] = 1
    offspring = np.vstack(((parent1 + parent2)/2+beta*(parent1-parent2)/2,
                           (parent1 + parent2)/2-beta*(parent1-parent2)/2))
    return offspring

# real code mutation
# INPUT: parent:    ndarray
#        proM:      int
#        disCM:      int
# OUTPUT:offspring: ndarray


def real_mutation(parent, boundary, proM=1, disM=20):
    offspring = parent
    N, M = parent.shape
    lower = np.tile(boundary[0], [N, 1])
    upper = np.tile(boundary[1], [N, 1])
    position = np.random.rand(N, M) < (proM/M)
    mu = np.random.rand(N, M)
    sweap = position & (mu <= 0.5)
    sweap_index = np.where(sweap == True)
    offspring[sweap_index] = offspring[sweap_index] + (upper[sweap_index]-lower[sweap_index])*((2*mu[sweap_index]+(
        1-2*mu[sweap_index])))*(1-(offspring[sweap_index]-lower[sweap_index])/(upper[sweap_index]-lower[sweap_index]))**(disM+1)**(1/(disM+1)-1)
    sweap = position & (mu > 0.5)
    sweap_index = np.where(sweap == True)
    offspring[sweap_index] = offspring[sweap_index] + (upper[sweap_index]-lower[sweap_index])*(1-(2*(1-mu[sweap_index])+(
        2*mu[sweap_index]-0.5)))*(1-(upper[sweap_index]-offspring[sweap_index])/(upper[sweap_index]-lower[sweap_index]))**(disM+1)**(1/(disM+1)-1)
    return offspring
