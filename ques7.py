a = float(input())

precision = 0.0000001
# YOUR CODE HERE

# Assume that x = a
x = a

while True:
    # Calculate more closed x
    root = 0.5 * (x + (a / x))

    # Check for closeness
    if (abs(root - x) < precision):
        print('%.4f'%root)
        break

    # Update root
    x = root