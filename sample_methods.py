import random as r

def RWS(Population):
    fsum = sum([i.f for i in Population])
    for i in Population:
        i.p = i.f / fsum

def p_sample(Population):
    rand = r.random()
    s = 0
    i = 0
    while s < rand:
        s += Population[i].p
        i += 1
    return Population[i-1] if i > 0 else Population[0]

def tournament_sample2(Population):
    i1 = Population[r.randint(0, len(Population)-1)]
    i2 = Population[r.randint(0, len(Population)-1)]
    return i1 if i1.f > i2.f else i2

def rank(Population, min_occurance):
    max_occurence = 2-min_occurance
    Population.sort(key = lambda x: x.f)
    for i, j in enumerate(Population):
        j.p = (((max_occurence-min_occurance)/(len(Population)-1))*i + min_occurance)/len(Population)

def truncate(Population, loss):
    Population.sort(key = lambda x: x.f)
    while loss > 0:
        Population.pop(0)
        loss -= 1