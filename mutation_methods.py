import numpy as np
import random as r
from ind import individual

def gaussian(ind, Pm, std, x_min, x_max):
    if ind:
        values = []
        for x in ind.values:
            if r.random() < Pm:
                values.append(x + np.random.normal(0, std))
            else:
                values.append(x)

            #stay within bounds    
            if values[-1] < x_min:
                values[-1] = x_min
            if values[-1] > x_max:
                values[-1] = x_max

        return individual(values)
    return None

def uniform(ind, Pm, x_min, x_max):
    if ind:
        values = []
        for _ in ind.values:
            values.append(r.uniform(x_min, x_max))
        return individual(values)
    return None