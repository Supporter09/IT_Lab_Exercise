import math 

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def cosine(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

def vector_distance(v1, v2, **kwargs):

    ##################
    # YOUR CODE HERE #
    ##################
    if kwargs:
        if kwargs['norm'] == 'manhattan':
            return manhattan(v1,v2)
        elif kwargs['norm'] == 'cosine':
            return round(cosine(v1,v2),9)
        else:
            return math.dist(v1,v2)
    else:
        return math.dist(v1,v2)

print(vector_distance([1, 2], [4, 6], norm='cosine'))