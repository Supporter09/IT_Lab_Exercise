n = int(input())
s = input()

##################
# YOUR CODE HERE #
##################
test = s.split()
res = []
for group in test:
    tmp = ''
    for char in group:
        # Encrypt uppercase characters
        if (char.isupper()):
            tmp += chr((ord(char) + n - 65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            tmp += chr((ord(char) + n - 97) % 26 + 97)
    res.append(tmp)
    
print(' '.join(res))