import numpy as np
import matplotlib.pyplot as plt

def generate_random_walks(W, N, d):
    # Initialize arrays to store endpoints
    endpoints = np.zeros((W, d))

    for i in range(W):
        # Generate random steps in d dimensions
        steps = np.random.normal(0, 1, size=(N, d))

        # Calculate cumulative sum to get the random walk path
        path = np.cumsum(steps, axis=0)

        # Store the endpoint of the random walk
        endpoints[i] = path[-1]

    return endpoints

def plot_random_walks(W, N_values, d):
    # Set up the plot
    plt.figure(figsize=(8, 8))
    plt.title(f'Endpoints of {W} Random Walks with Different Step Counts in {d} Dimensions')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Generate and plot random walks for different step counts
    for N in N_values:
        endpoints = generate_random_walks(W, N, d)
        plt.scatter(endpoints[:, 0], endpoints[:, 1], label=f'N={N}', alpha=0.5)

    plt.legend()
    plt.show()

# Set parameters
W = 10000
N_values = [1, 10]
d = 2

# Plot random walks
plot_random_walks(W, N_values, d)