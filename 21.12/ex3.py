import numpy as np
import matplotlib.pyplot as plt

def system_solver(a):
    ##################
    # YOUR CODE HERE #
    ##################
    
    # Using numpy linear equation solver .linalg.solve(a, b)
    # Split augmented matrix [A|b] into A and B

    A = a[:, :-1]
    B = a[:, -1]

    # Solve
    res = np.linalg.solve(A, B)

    return res

a = np.array(
[[ 1,  3, -2,  5],
[ 3,  5,  6,  7],
[ 2,  4,  3,  8]]
)

res = system_solver(a.astype('f'))

# Convert to column matrix
# -1 is stand for the length of array
print(res.reshape(-1,1))