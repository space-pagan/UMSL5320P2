import random as r
from ind import individual

def single_point(Parents, n, Pc):
    if r.random() < Pc:
        child_values = []
        crosspoint = r.randint(0, n)
        for i in range(n):
            if i < crosspoint:
                child_values.append(Parents[0].values[i])
            else:
                child_values.append(Parents[1].values[i])
        return individual(child_values)
    return None #regenerate parent pair