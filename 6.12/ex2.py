s = input()

##################
# YOUR CODE HERE #
##################
res = s.split('_')
res = ''.join([x.title() for x in res])

print(res)