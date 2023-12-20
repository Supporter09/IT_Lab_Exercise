n = int(input())
# YOUR CODE HERE
for i in range(1, n+1): # loop through each row
    print('_'*(n-i) + '/' + ' '*((i - 1)*2) +'\\' + '_'*(n-i) )