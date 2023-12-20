def remove_duplicates(l):

    ##################
    # YOUR CODE HERE #
    ##################
    res = [l[0]]
    for i in range(1, len(l)):
        if l[i] != l[i-1]: res.append(l[i])

    return res

print(remove_duplicates([1, 0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 5, 5]))