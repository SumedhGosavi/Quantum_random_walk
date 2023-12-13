import numpy as np
import matplotlib.pyplot as plt

def generate_random_walk(N, d, seed=None):
    
    rng = np.random.default_rng(seed)
    steps = rng.uniform(-0.5, 0.5, size=(N, d))
    trajectory = np.cumsum(steps, axis=0)
    return trajectory

def plot_random_walk_1d(N, num_walks):
    for i in range(num_walks):
        random_walk = generate_random_walk(N, 1)
        plt.plot(random_walk, label=f'Walk {i + 1}')

    plt.title(f'{num_walks} Random Walks in 1D')
    plt.xlabel('Time Step')
    plt.ylabel('Position')
    plt.legend()
    plt.show()

def plot_random_walk_2d(N_values):
    for N in N_values:
        random_walk = generate_random_walk(N, 2)
        plt.plot(random_walk[:, 0], random_walk[:, 1], label=f'N={N}')

    plt.title('2D Random Walks')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.legend()
    plt.axis('equal')  # Set equal aspect ratio
    plt.show()

#(i)
plot_random_walk_1d(N=10000, num_walks=5)

#(ii)
N_values = [10, 1000, 100000]
plot_random_walk_2d(N_values)
