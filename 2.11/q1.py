def is_perfect(n):
    # YOUR CODE HERE
    check = 0
    for i in range(1, int(n*(1/2)+1)):
        if n % i == 0:
            check += i
    return check == n

print(is_perfect(10))