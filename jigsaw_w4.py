import numpy as np
import random
import math
import matplotlib.pyplot as plt

# Function to create an initial random state of the puzzle
def create_random_state(puzzle_size):
    pieces = list(range(puzzle_size * puzzle_size))
    random.shuffle(pieces)
    return np.array(pieces).reshape(puzzle_size, puzzle_size)

# Function to calculate the cost (number of correctly placed pieces)
def calculate_cost(state, goal_state):
    cost = 0
    for i in range(state.shape[0]):
        for j in range(state.shape[1]):
            if state[i, j] == goal_state[i, j]:
                cost += 1
    return cost

# Function to swap two pieces in the state
def swap(state):
    x1, y1 = random.randint(0, state.shape[0]-1), random.randint(0, state.shape[1]-1)
    x2, y2 = random.randint(0, state.shape[0]-1), random.randint(0, state.shape[1]-1)
    
    new_state = state.copy()
    new_state[x1, y1], new_state[x2, y2] = new_state[x2, y2], new_state[x1, y1]
    
    return new_state

# Simulated Annealing algorithm
def simulated_annealing(puzzle_size, initial_temp=1000, iter_max=10000, min_temp=0.01):
    # Create goal state
    goal_state = np.arange(puzzle_size * puzzle_size).reshape(puzzle_size, puzzle_size)
    
    # Create initial state
    current_state = create_random_state(puzzle_size)
    current_cost = calculate_cost(current_state, goal_state)
    
    best_state = current_state
    best_cost = current_cost
    
    costs = []

    T = initial_temp
    for iteration in range(iter_max):
        new_state = swap(current_state)
        new_cost = calculate_cost(new_state, goal_state)
        
        # Acceptance criteria
        if new_cost > current_cost:
            current_state = new_state
            current_cost = new_cost
            if new_cost > best_cost:
                best_state = new_state
                best_cost = new_cost
        else:
            E = current_cost - new_cost
            if T > min_temp:  # Ensure T is greater than min_temp
                pE = math.exp(E / T)
                if random.random() < pE:
                    current_state = new_state
                    current_cost = new_cost
        
        # Record the best cost
        costs.append(best_cost)

        # Cooling schedule
        T *= 0.99
    
    return best_state, best_cost, costs

# Parameters
puzzle_size = 3  # 3x3 puzzle
best_state, best_cost, costs = simulated_annealing(puzzle_size)

# Display results
print("Best State:\n", best_state)
print("Best Cost (Correct Pieces):", best_cost)

# Plot the cost vs iterations graph
plt.figure(figsize=(10, 6))
plt.plot(costs, label='Correct Pieces', color='blue')
plt.xlabel('Iterations')
plt.ylabel('Number of Correctly Placed Pieces')
plt.title('Cost vs Iterations for Simulated Annealing (Jigsaw Puzzle)')
plt.grid(True)
plt.legend()
plt.show()
