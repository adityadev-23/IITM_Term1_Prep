import numpy as np
import matplotlib.pyplot as plt

# 1. The Data (Unit Square)
X = np.array([[0, 1, 1, 0, 0], 
              [0, 0, 1, 1, 0]])

# 2. The Machine (Shear Matrix)
T = np.array([[1, 1], 
              [0, 1]])

# 3. The Calculation
X_new = np.dot(T, X)

# 4. Plotting Magic
plt.figure(figsize=(10, 5))

# Plot Original
plt.subplot(1, 2, 1)
plt.plot(X[0, :], X[1, :], 'b--', linewidth=3, label='Original')
plt.title("Original Square")
plt.grid(True)
plt.xlim(-1, 3)
plt.ylim(-1, 3)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Plot Transformed (YOUR Green Dotted Line)
plt.subplot(1, 2, 2)
plt.plot(X_new[0, :], X_new[1, :], 'g:', linewidth=3, label='Transformed') 
plt.title("After Matrix T")
plt.grid(True)
plt.xlim(-1, 3)
plt.ylim(-1, 3)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.show()