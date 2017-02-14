####Reservoir sampling###
import random
def reservoir_sampling(iterable,K):
    result = []
    N = 0
    for i in iterable:
        N += 1
        if len(result)<K:
            result.append(i)
        else:
            s = int(random.uniform(0,N))
            if s < K:
                result[s] = i
    return result

user = range(50)
print reservoir_sampling(user,5)
