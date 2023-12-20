def dec_to_bin(n):
    # YOUR CODE HERE
    if n == 0: return 0
    else:
        return (n % 2 + 10 * dec_to_bin(int(n // 2)))
    
print(dec_to_bin(120))