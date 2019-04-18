import selection_methods as sm
import crossover_methods as cm
import mutation_methods as mm
import random as r
import ind
from ind import individual

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
#other:
max_generations = 50

def single_run():
    #initialize
    gen_count = 1
    P = []
    while len(P) < N:
        P.append(individual(None, n, x_min, x_max))
    sm.RWS(P)

    for i in P:
        print(i)

    while gen_count < max_generations:
        P_next = []
        while len(P_next) < N:
            i = mm.gaussian(cm.single_point((sm.RWS_sample(P, r.random()), sm.RWS_sample(P, r.random())), n, Pc), Pm, std)
            if i:
                P_next.append(i)

        gen_count += 1
        P = P_next
        sm.RWS(P) #calculate distribution

    print('\n\n\n')
    for i in P:
        print(i)
    print('Total evaluations:', ind.evals)

def multi_run():
    print('Not yet implemented')

if __name__ == "__main__":
    single_run()