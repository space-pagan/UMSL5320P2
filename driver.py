import sample_methods as sm
import crossover_methods as cm
import mutation_methods as mm
import random as r
import ind
from ind import individual
import statistics

#global variables:

#Population size:
N = 10
#value bounds:
x_min = -1.0
x_max = 5.0
n = 3
#crossover:
Pc = 0.8
#mutation:
Pm = 0.1
std = 0.02
#ranking minimum expectation:
rank_min = 0.1
#truncate n elements:
loss = 2
#arithmetic weight:
weight = 0.3
#other:
max_generations = 50

def distr(P, method):
    #Distribution Methods:
    #RWS
    #rank
    #truncate - must be used with tournament
    #no_distr - must be used with tournament
    if method == 'RWS':
        return sm.RWS(P)
    elif method == 'rank':
        return sm.rank(P, rank_min)
    elif method == 'truncate':
        return sm.truncate(P, loss)
    else:
        return

def sample(P, method):
    #Sampling Methods:
    #tournament_sample2
    #p_sample - for RWS and rank
    if method == 'tournament':
        return sm.tournament_sample2(P)
    elif method == 'p_sample':
        return sm.p_sample(P)
    else:
        return

def cross(P, method):
    #Crossover Methods:
    #single_point
    #two_point
    #arithmatic
    if method == 'single_point':
        return cm.single_point(P, n, Pc)
    elif method == 'two_point':
        return cm.two_point(P, n, Pc)
    elif method == 'arithmatic':
        return cm.arithmatic(P, n, Pc, weight)
    else:
        return None

def mut(P, method):
    #Mutation Methods:
    #gaussian
    #uniform
    if method == 'gaussian':
        return mm.gaussian(P, Pm, std, x_min, x_max)
    elif method == 'uniform':
        return mm.uniform(P, Pm, x_min, x_max)
    else:
        return None

def single_run(fdistr, fsamp, fcross, fmut):
    #initialize
    best_of_run = individual([x_max, x_max, x_max]) #start with worst
    gen_count = 1
    P = []
    while len(P) < N:
        P.append(individual(None, n, x_min, x_max))

    while gen_count < max_generations:
        distr(P, fdistr) #calculate distribution
        for i in P:
            if i.f > best_of_run.f:
                best_of_run = i
        P_next = []
        while len(P_next) < N:
            i = mut(cross( (sample(P, fsamp), sample(P, fsamp)), fcross), fmut)
            if i: #if not None
                P_next.append(i)

        gen_count += 1
        P = P_next

    print('Total evaluations:', ind.evals)
    return best_of_run


#Distribution Methods:
#RWS - must be used with p_sample
#rank - must be used with p_sample
#truncate - must be used with tournament
#no_distr - must be used with tournament

#Sampling Methods:
#tournament
#p_sample - for RWS and rank

#Crossover Methods:
#single_point
#two_point
#arithmatic

#Mutation Methods:
#gaussian
#uniform
multi_run = 30
if multi_run:
    best_of_run_data = []
    for _ in range(multi_run):
        best_of_run_data.append(single_run('truncate', 'tournament', 'arithmatic', 'uniform'))
        ind.evals = 0
    for i in best_of_run_data:
        print(i)
    best_of_run_fit = [i.pure_fit for i in best_of_run_data]
    print('Average of BORs is', sum(best_of_run_fit)/len(best_of_run_fit))
    print('Standard Deviation of BORs is', statistics.pstdev(best_of_run_fit))
else:
    single_run('RWS', 'p_sample', 'single_point', 'gaussian')