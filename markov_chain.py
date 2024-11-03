# Amol Arora, 116491705

import numpy as np

# I start by creating a 5x5 Markov transition matrix and normalizing rows
P = np.random.rand(5, 5)
P = P / P.sum(axis=1, keepdims=True)

# Creating a random 5-element probability vector and normalize it
p = np.random.rand(5)
p /= p.sum()

# Applying the transition rule 50 times
for _ in range(50):
    p = P.T @ p

# Computing the stationary distribution
eigenvalues, eigenvectors = np.linalg.eig(P.T)
stationary = eigenvectors[:, np.isclose(eigenvalues, 1)]
stationary = stationary / stationary.sum()

# Comparing p50 with the stationary distribution
diff = np.abs(p - stationary.flatten())
print("Difference within tolerance:", np.all(diff < 1e-5))
