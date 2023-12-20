# def GCD(a, b):
#   # YOUR CODE HERE
#     if(b == 0):
#         return abs(a)
#     else:
#         return GCD(b, a % b)

# Take idea from normal GCD recursive method
gcd = lambda a, b: abs(a) if b == 0 else gcd(b, a % b)
# print(gcd(12, 18))