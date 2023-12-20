tmp = input().split(' ')
m, n = int(tmp[0]), int(tmp[1])

##################
# YOUR CODE HERE #
##################
res = []
for i in range(1, m+1): 
    tmp = [x for x in range(n*(i-1) + 1, n*i + 1)]
    res.append(tmp)

for row in res:
    print(*row)

