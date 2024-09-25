import random
import math
import matplotlib.pyplot as plt
import numpy as np

# Random points in 2D space
N = 1000
x = np.random.rand(2, N)

# Distance matrix based on Euclidean distance
distance_matrix = np.zeros((N, N))
for i in range(N-1):
    for j in range(i + 1, N):
        distance_matrix[i, j] = np.linalg.norm(x[:, i] - x[:, j])
        distance_matrix[j, i] = distance_matrix[i, j]

# total distance of a tour
def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1)) + distance_matrix[tour[-1], tour[0]]

# Simulated Annealing for TSP
def simulated_annealing_tsp(N, distance_matrix, T_init=1000, iter_max=500000):
    # Random initial solution
    current_solution = list(range(N))
    random.shuffle(current_solution)
    
    best_solution = current_solution[:]
    best_cost = calculate_total_distance(best_solution, distance_matrix)
    
    costs = []
    
    for i in range(1, iter_max + 1):
        # Randomly select two cities
        id = random.sample(range(N), 2)
        id.sort()
        
        # Create a new solution using second neighbor operator
        new_solution = current_solution[:]
        new_solution[id[0]:id[1] + 1] = reversed(current_solution[id[0]:id[1] + 1])
        
        # Calculate new cost
        new_cost = calculate_total_distance(new_solution, distance_matrix)
        
        # Acceptance criteria
        E = best_cost - new_cost  # to check for minimum direction
        T = T_init / i  # Cooling schedule
        
        if E > 0:
            pE = 1  # Always accept better solutions
        elif T <= 0:
            pE = 0  # No chance to accept worse solutions
        else:
            if E / T > 500:  # Large value threshold for stability
                pE = 0
            elif E / T < -500:
                pE = 1
            else:
                pE = 1 / (1 + math.exp(-E / T))  # Use original formula
            
        if E > 0 or random.random() < pE:
            current_solution = new_solution
            if new_cost < best_cost:
                best_solution = current_solution
                best_cost = new_cost
        
        # Track costs
        costs.append(best_cost)
    
    return best_solution, best_cost, costs

# Run Simulated Annealing
best_tour, best_distance, costs = simulated_annealing_tsp(N, distance_matrix)

# Display results
print("Best tour:", best_tour)
print("Best distance:", best_distance)

# Plot the cost vs iterations graph
plt.figure(figsize=(10, 6))
plt.plot(costs, label='Total Distance (Cost)', color='blue')
plt.xlabel('Iterations')
plt.ylabel('Total Distance (Cost)')
plt.title('Cost vs Iterations for Simulated Annealing (TSP)')
plt.grid(True)
plt.legend()
plt.show()
