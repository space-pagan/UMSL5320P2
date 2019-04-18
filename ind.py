import random as r

class individual:
    '''Implements an individual in a genetic algorithm
    
    Arguments:
        values {numerical interable} -- Initial values for the individual.
        If None, provide the desired value list length, minimum, and maximum, in that order.
        Ex: individual([1, 2, 3]) or individual(None, 3, 1, 3)
    '''
    def __init__(self, values, *params):
        #params should be (x_len, x_min, x_max)
        if values == None:
            values = []
            for _ in range(params[0]):
                values.append(r.uniform(params[1], params[2]))

        self.values = values
        self.__f = None
        self.p = 0
        self.pure_fit = pure_fitness(values)

    @property
    def f(self):
        if self.__f == None:
            self.__f = fitness(self.values)
        return self.__f

    def __repr__(self):
        return str(['%5.3f' % s for s in self.values]) + '\t'+'%5.3f' % self.pure_fit

epsilon = 0.000000000000001
evals = 0

def pure_fitness(values):
    return sum([x**2 for x in values])

def fitness(values):
    global evals
    evals += 1
    return (1+epsilon)/(pure_fitness(values)+epsilon) #to avoid 1/0