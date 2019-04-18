import numpy as np
import random as r
from ind import individual

def gaussian(ind, Pm, std):
    if ind:
        values = []
        for x in ind.values:
            #values.append(x + (np.random.normal(0, std) if r.random() < Pm else 0) )
            rand = r.random()
            if rand < Pm:
                values.append(x + np.random.normal(0, std))
            else:
                values.append(x)
        return individual(values)
    return None