import numpy as np

# 1. Create two 2x2 Matrices
# Think of these as transformations (stretching/rotating space)
A = np.array([[2, 1], 
              [1, 3]])

B = np.array([[1, 0], 
              [0, 1]]) # Identity Matrix (Does nothing!)

print("Matrix A:\n", A)
print("\nMatrix B (Identity):\n", B)

# 2. Dot Product (Matrix Multiplication)
# Applying transformation A to B
dot_product = np.dot(A, B)
print("\nDot Product (A . B):\n", dot_product)

# 3. Determinant
# How much does Matrix A stretch space? (Area scaling factor)
det_A = np.linalg.det(A)
print(f"\nDeterminant of A: {det_A}")

# 4. Inverse
# The 'Undo' button. If A stretches space, Inverse A shrinks it back.
try:
    inv_A = np.linalg.inv(A)
    print("\nInverse of A:\n", inv_A)
    
    # Proof: A dot Inverse_A should equal Identity (approx)
    print("\nProof (A . Inverse A):\n", np.dot(A, inv_A))
except np.linalg.LinAlgError:
    print("\nMatrix A has no inverse (Determinant is 0)!")