import trig
import math
n = int(input())

res = 0.
lib_res = 0.
for i in range(1, 21):
    if i % 2 == 1:
        res += trig.sin_mac(n+i)
        lib_res += math.sin(n+i)
    else:
        res += trig.cos_mac(n+i)
        lib_res += math.cos(n+i)

print(round(res,6))
print(round(lib_res, 6))
