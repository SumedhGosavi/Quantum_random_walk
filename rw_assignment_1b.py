import numpy as np
import matplotlib.pyplot as plt

def generate_random_walks(W, N, d):
    endpoints = np.zeros((W, d))

    for i in range(W):
        steps = np.random.normal(0, 1, size=(N, d))
        path = np.cumsum(steps, axis=0)
        endpoints[i] = path[-1]

    return endpoints

def plot_random_walks(W, N_values, d):
    plt.figure(figsize=(8, 8))
    plt.title(f'Endpoints of {W} Random Walks with Different Step Counts in {d} Dimensions')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    for N in N_values:
        endpoints = generate_random_walks(W, N, d)
        plt.scatter(endpoints[:, 0], endpoints[:, 1], label=f'N={N}', alpha=0.5)

    plt.legend()
    plt.show()

W = 10000
N_values = [1, 10]
d = 2

plot_random_walks(W, N_values, d)