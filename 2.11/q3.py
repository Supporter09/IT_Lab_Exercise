def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
# boolean array
    p = 2
    while (p * p <= num):
 
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
 
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
 
    return prime

import math
def print_prime(n):
    # YOUR CODE HERE
    prime_arr = SieveOfEratosthenes(n)

    for i in range(2, n):
        if prime_arr[i]: print(i, end=" ")

# print_prime(11)