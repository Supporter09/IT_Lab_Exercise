import math

# computed with 9 exact decimal places and rounded to 6 digits after the comma
PI = 3.141592653

def exp_mac(x):
    result = 1.0
    factorial = 1.0
    for n in range(1, x+100):
        factorial *= n
        result += (x**n) / factorial
    return result, 6

def sin_mac(x):
    result = 0.0
    for n in range(x+100):
        term = ((-1)**n) * (x ** (2*n + 1)) / (math.factorial(2 * n + 1))
        result += term
    return result

def cos_mac(x):
    result = 0.0
    for n in range(x+100):
        term = ((-1)**n) * (x ** (2*n)) / (math.factorial(2 * n))
        result += term
    return result