def dictionary_convert(s):

    ##################
    # YOUR CODE HERE #
    ##################
    freq_dict = {}
    for char in s:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    return freq_dict

print(dictionary_convert('hwqrkhakjsfhaskjfhuk'))