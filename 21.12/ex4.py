import numpy as np
import matplotlib.pyplot as plt

# Generate x values in the range [-4, 4]
x = np.linspace(-4, 4, 1000)

# Calculate y values for sin(2x) and cos(2x)
y_sin = np.sin(2 * x)
y_cos = np.cos(2 * x)

# Plotting
plt.plot(x, y_sin, label='y = sin(2x)')
plt.plot(x, y_cos, label='y = cos(2x)')

# Adding labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of triognometrix function')
plt.legend()

# Display the plot
plt.show()