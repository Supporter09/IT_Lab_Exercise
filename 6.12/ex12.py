def merge_dict(d1, d2):

    ##################
    # YOUR CODE HERE #
    ##################
    res_dict = {}
    for key in d1.keys():
        res_dict[key] = res_dict.get(key, 0) + d1[key]
    
    for key in d2.keys():
        res_dict[key] = res_dict.get(key, 0) + d2[key]
        
    return res_dict

print(merge_dict({'a': 3, 'b': 2, 'c': 1},{'b': 3, 'c': 2, 'd': 1}))