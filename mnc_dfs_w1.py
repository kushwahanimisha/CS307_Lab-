from collections import deque

# Missionary - Cannibalism question using DFS

def is_valid(state):
    missionaries, cannibals, boat = state
    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:


        return False
    if missionaries > 0 and missionaries < cannibals:
                #to check the criteria on the side of the river
        return False
    if 3 - missionaries > 0 and 3 - missionaries < 3 - cannibals:
        #to check the criteria on other side of the river

        return False
    return True

def get_successors(state):
    successors = []
    missionaries, cannibals, boat = state
    if boat == 1:  # Boat on the starting side
        moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
        for move in moves:
            new_state = (missionaries - move[0], cannibals - move[1], 0)  # Boat moves to the other side
            if is_valid(new_state):
                successors.append(new_state)
    else:  # Boat on the other side
        moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
        for move in moves:
            new_state = (missionaries + move[0], cannibals + move[1], 1)  # Boat returns
            if is_valid(new_state):
                successors.append(new_state)
    return successors

def dfs(start_state, goal_state):
    stack = [(start_state, [])]  # To track the path from the initial state
    visited = set()  # To store unique values
    while stack:
        (state, path) = stack.pop()  # Get the last element (DFS)
        if state in visited:
            continue
        visited.add(state)
        path = path + [state]
        if state == goal_state:
            return path
        for successor in get_successors(state):
            stack.append((successor, path))
    return None

start_state = (3, 3, 1)
goal_state = (0, 0, 0)

solution = dfs(start_state, goal_state)
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
