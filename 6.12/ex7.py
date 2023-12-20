def sort_students(l):

    ##################
    # YOUR CODE HERE #
    ##################
    res = sorted(l, key=lambda x: [x[1], x[0]])

    return res

print(sort_students([('John', 9.75), ('Max', 9.5), ('James', 9.5), ('Henry', 8.5)]))