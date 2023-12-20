s = input()

##################
# YOUR CODE HERE #
##################

# Reverse string and take element with step = 2
res = ''
i = len(s) - 1
while i >= 0:
    if i == len(s) - 1: res += s[i].upper()
    else : res += s[i].lower()
    i -= 2

print(res)