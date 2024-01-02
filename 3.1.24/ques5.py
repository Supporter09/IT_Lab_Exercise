class Matrix():
    def __init__(self, l):
        self.l = l
    def __str__(self):
        res = []
        for e in self.l:
            res.append('	'.join(list(map(str, e))))
        return '\n'.join(res)
    def size(self):
        return (len(self.l), len(self.l[0]))
    def __add__(self, other):
        return Matrix([[u + v for (u, v) in zip(x, y)] for (x, y) in zip(self.l, other.l)])
    def __mul__(self, k):
        return Matrix([[u * k for u in e] for e in self.l])
    __rmul__ = __mul__

def mulmtx(a, b):
    n = len(a)
    c = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

class SquareMatrix(Matrix):
    def __pow__(self, n):
        siz = len(self.l)
        res = [[1 if(j == i) else 0 for j in range(siz)] for i in range(siz)]
        a = self.l[:]
        while(n > 0):
            if(n%2 == 1):
                res = mulmtx(res, a)
            a = mulmtx(a, a)
            n //= 2
        return SquareMatrix(res)