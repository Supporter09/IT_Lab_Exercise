def mirror(s):

    ##################
    # YOUR CODE HERE #
    ##################
    # Mapping mirror character
    mirror_mapping = {
        'b':'d',
        'd':'b',
        'i':'i',
        'o':'o',
        'p':'q',
        'q':'p',
        'v':'v',
        'w':'w',
        'x':'x'
    }
    res = ''

    for char in s[::-1]:
        if char not in mirror_mapping.keys():
            return "NOT POSSIBLE"
        res += mirror_mapping[char]
    return res

print(mirror('void'))