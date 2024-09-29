from collections import deque

# missionary - cannibalism question from class 1.

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
    if boat == 1:
        moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
        for move in moves:
            new_state = (missionaries - move[0], cannibals - move[1], 0)
            if is_valid(new_state):
                successors.append(new_state)
    else:
        moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
        for move in moves:
            new_state = (missionaries + move[0], cannibals + move[1], 1)
            if is_valid(new_state):
                successors.append(new_state)
    return successors

def bfs(start_state, goal_state):
    queue = deque([(start_state, [])]) #to track the path from initial state
    visited = set() #to store unique values
    while queue:
        (state, path) = queue.popleft()#get leftmost element
        if state in visited:
            continue
        visited.add(state)
        path = path + [state]
        if state == goal_state:
            return path
        for successor in get_successors(state):
            queue.append((successor, path))
    return None

start_state = (3, 3, 1)
goal_state = (0, 0, 0)

solution = bfs(start_state, goal_state)
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")