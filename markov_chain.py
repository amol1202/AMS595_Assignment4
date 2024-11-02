import numpy as np

# Step 1: Create a 5x5 Markov transition matrix and normalize rows
P = np.random.rand(5, 5)
P = P / P.sum(axis=1, keepdims=True)

# Step 2: Create a random 5-element probability vector and normalize it
p = np.random.rand(5)
p /= p.sum()

# Step 3: Apply the transition rule 50 times
for _ in range(50):
    p = P.T @ p

# Step 4: Compute the stationary distribution
eigenvalues, eigenvectors = np.linalg.eig(P.T)
stationary = eigenvectors[:, np.isclose(eigenvalues, 1)]
stationary = stationary / stationary.sum()

# Step 5: Compare p50 with the stationary distribution
diff = np.abs(p - stationary.flatten())
print("Difference within tolerance:", np.all(diff < 1e-5))
