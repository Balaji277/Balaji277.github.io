import numpy as np
import matplotlib.pyplot as plt

# Define the function to plot
def f(x, y):
    return np.sin(x) + np.cos(y)

# Generate the data to plot
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.linspace(-2*np.pi, 2*np.pi, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
print('capX: ',x)
print('not cap x: ',x)
# Plot the filled contour plot
plt.contourf(X, Y, Z, cmap='coolwarm')
#plt.colorbar()

plt.title('Filled Contour Plot')
plt.xlabel('x')
plt.ylabel('y')

plt.show()