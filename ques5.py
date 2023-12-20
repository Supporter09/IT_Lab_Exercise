import math
n = int(input())
# YOUR CODE HERE

# If n is greater than 1
if n > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(n/2)+1):
        # If n is divisible by any number between 2 and n / 2, it is not prime
        if (n % i) == 0:
            print("not prime")
            break
    else:
        print('prime')
else:
    print('not prime')