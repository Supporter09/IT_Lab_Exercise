import numpy as np
import matplotlib.pyplot as plt

def convert(a):
    
    ##################
    # YOUR CODE HERE #
    ##################
    for i in range(len(a)):
        a[i] /= sum(a[i]) # Divide each row to its own sum
    return a

check = np.array([[0, 1, 2],[3, 4, 5],[6, 7, 8]])
print(convert(check.astype('f')))