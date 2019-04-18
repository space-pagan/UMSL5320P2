def RWS(Population):
    fsum = sum([i.f for i in Population])
    for i in Population:
        i.p = i.f / fsum

def RWS_sample(Population, r):
    s = 0
    i = 0
    while s < r:
        s += Population[i].p
        i += 1
    return Population[i-1] if i > 0 else Population[0]