s = input()

##################
# YOUR CODE HERE #
##################

# Reverse string and take element with step = 2
res = s[::-1][::2]
res = res.lower()
print(res.title())