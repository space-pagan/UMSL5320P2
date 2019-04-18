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

def two_point(Parents, n, Pc):
    if r.random() < Pc:
        child_values = []
        crosspoint1 = r.randint(0, n)
        crosspoint2 = r.randint(crosspoint1, n)
        for i in range(n):
            if i < crosspoint1:
                child_values.append(Parents[0].values[i])
            elif i >= crosspoint1 and i < crosspoint2:
                child_values.append(Parents[1].values[i])
            else:
                child_values.append(Parents[0].values[i])
        return individual(child_values)
    return None #regenerate parent pair

def arithmetic(Parents, n, Pc, weight):
    if r.random() < Pc:
        child_values = []
        for i in range(n):
            child_values.append( (weight * Parents[0].values[i]) + \
                ((1-weight) * Parents[1].values[i]) )
        return individual(child_values)
    return None