def transform(l):

    ##################
    # YOUR CODE HERE #
    ##################
    res = []
    for el in l:
        if el % 2 == 0: res.append(el*2)
        else: res.append(-el)

    return res

print(transform([32, 56, 99, -40, 20, 78, 43, -61, 61]))