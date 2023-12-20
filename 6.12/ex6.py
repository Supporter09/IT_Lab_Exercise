temp = input().split(' ')
m, n = int(temp[0]), int(temp[1])

a = []
b = []
for i in range(m):
    a.append(list(map(int,input().split(' '))))
for i in range(m):
    b.append(list(map(int,input().split(' '))))

##################
# YOUR CODE HERE #
##################

# res = [[0]*n]*m have some problems that it replicate 2 row
res = []
for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(0)
    res.append(tmp)


for i in range(m):
    for j in range(n):
        res[i][j] = a[i][j] + b[i][j]

for row in res:
    print(*row)