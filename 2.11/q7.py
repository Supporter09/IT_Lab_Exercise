def sum_of_digit(n):
    # YOUR CODE HERE
    if len(str(n)) == 1:
        return n
    else:
        return n%10 + sum_of_digit(n//10)
    
print(sum_of_digit(123))