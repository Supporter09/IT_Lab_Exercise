f = lambda a, b, c: a if (a > b and a > c) else b if (b>a and b>c) else c if (c>a and c>b) else 0
print(f(2, 3, 1))