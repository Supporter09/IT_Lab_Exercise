def GCD(a, b):
  # YOUR CODE HERE
    if(b == 0):
        return abs(a)
    else:
        return GCD(b, a % b)
    
print(GCD(18, 24))