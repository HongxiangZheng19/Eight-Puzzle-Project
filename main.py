import heapq    # Importing heapq for priority queue support
import math


# Funcion for user interface to catch invalid inputs
def get_valid_input(prompt, expected_length):
    while True:
        try:
            user_input = list(map(int, input(prompt).split()))
            if len(user_input) != expected_length or any(i < 0 or i > 8 for i in user_input):
                raise ValueError("Invalid tile numbers or count.")
            return user_input
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
                
class Problem:
# Initialize the problem with the initial state and an optional goal state
    def __init__(self, initial, goal=None):

        # The starting configuration of the puzzle
        self.initial_state = initial

        # Default goal state.
        self.goal_state = goal if goal else [1, 2, 3, 4, 5, 6, 7, 8, 0]

        # Possible moves: up, down, left, right
            # (x,y) where x = row and y = column
            # x = 0 = first row, 1 = second row, 2 = third row
            # y = 0 = first column, 1 = second column, 2 = third column
        self.operators = [(-1, 0), (1, 0), (0, -1), (0, 1)] #up, down, left, right


class PuzzleState:

    # Initialize the puzzle state within the context of a problem
    def __init__(self, configuration, problem, parent=None, move=None, cost=0):

        self.configuration = configuration # current tile configuration
        self.problem = problem # reference to the problem instance
        self.parent = parent # reference to the parent state in the search path
        self.move = move # the move made to reach this state from the parent
        self.cost = cost # the cost from the initial state to this state
        self.blank_pos = self.find_blank()# location of the blank tile
        #self.heuristic = self.euclidean_distance()# compute the Euclidean distance heuristic
        self.score = self.cost  # Score is the cost for UCS

    # Find and return the index of the blank tile
    def find_blank(self):
        return self.configuration.index(0)

    # Check if the current configuration matches the goal configuration
    def is_goal(self):
        return self.configuration == self.problem.goal_state

    # Comparator for priority queue to sort states by their cost
        # Compare the objects stored in the heap (determine the order/priority)
        # Maintains the correct order based on the "cost" 
    def __lt__(self, other):
        return self.cost < other.cost
    
    # Generate all valid child states by moving the blank tile according to the defined operators
        # This function is only responsible for generating all possible children state
    def generate_children(self):
        # hold all the child states generated
        children = []

        # attempts to find the position of the blank tile
            # For example, if self.blank_pos is 5, divmod(5, 3) will return (1, 2) -> the blank will be at (row 1, column 2)
        x, y = divmod(self.blank_pos, 3)
        
        # iterates through the possible movements (up, down, left, right)
        for dx, dy in self.problem.operators:
            # calculates the new position (nx, ny) of the blank tile after moving it in the direction (dx, dy)
            nx, ny = x + dx, y + dy

            # make sure that the tile would not go out of bound (3 x 3 grid)
            if 0 <= nx < 3 and 0 <= ny < 3:
                # translates the 2D grid coordinates back into a 1D index (list of length 9)
                new_pos = nx * 3 + ny
                # creates a copy of the current configuration 
                    # avoids modifying the original configuration
                new_config = self.configuration[:]
                # swaps the blank tile with the tile at the new position
                new_config[self.blank_pos], new_config[new_pos] = new_config[new_pos], new_config[self.blank_pos]
                # creates a new PuzzleState object for the child state
                    # It passes the parameter of:
                        # new configuration
                        # problem instance
                        # current state as the parent
                        # new position of the blank tile
                        # updated cost (incremented by 1 since each move has a cost of 1)
                children.append(PuzzleState(new_config, self.problem, self, new_pos, self.cost + 1))
        # returns the list of all valid child states generated
        return children
    

# UNIFORM COST SEARCH
# ------------------------------
def uniform_cost_search(problem):
        print("Starting Uniform Cost Search...")
        # create an initial "PuzzleState" object
        initial_state = PuzzleState(problem.initial_state, problem)
        # priority queue for states to be explored
            # inserting and removing the state with lowest cost
        open_list = [] 

        # initializate the search 
            # pushing the initial state into the priority queue
        heapq.heappush(open_list, initial_state)

        # visited_cost is used to keep track of the lowest cost to each state
        visited_costs = {tuple(problem.initial_state): 0}

        # set to track visited configurations to prevent revisiting
        visited = set() 
        # initial state is "visited", therefore it is added to the set
        visited.add(tuple(problem.initial_state))

        # loop until the open list is empty
        while open_list:
            # pop the state with the lowest cost
            current_state = heapq.heappop(open_list) 

            # check if the current state is the goal state
            if current_state.is_goal():
                print("Goal state reached!")
                # return the solution path if the goal state is reached
                return current_state  
            
            # explore all child states
                # using the "generate_children" function to find all valid moves from the current state
            for child in current_state.generate_children(): 
                # the configuration of each child is converted into a tuple for comparison 
                child_config_tuple = tuple(child.configuration)

                # checks if the configuration has not been visited 
                # checks if the current path to it is cheaper than a previously recorded path
                    # !!! allows revisiting of states if a cheaper path is found
                if child_config_tuple not in visited_costs or child.cost < visited_costs[child_config_tuple]:
                    # if not visited before, it is added to both the visited set and the open_list priority queue
                    visited.add(child_config_tuple)
                    # adding the child to open list managed by a heap
                        # the queue will then determine the order of state (by cost)
                    heapq.heappush(open_list, child)
        # Note: the child is ignored if it has already been visited before with a cost that is not cheaper than the previously recorded cost
        # return None if no solution is found
        return None  

# User Interface

print("Welcome to XXX (change this to your student ID) 8 puzzle solver.")
x = int(input('Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n'))
if x == 1: 
    print('Default puzzle\n')
    initial_config = [1, 2, 3, 4, 8, 0, 7, 6, 5] 

elif x == 2:
    print('Enter your puzzle, use a zero to represent the blank')
    a1, a2, a3 = get_valid_input('Enter the first row, use space or tabs between numbers ', 3)
    b1, b2, b3 = get_valid_input('Enter the second row, use space or tabs between numbers ', 3)
    c1, c2, c3 = get_valid_input('Enter the third row, use space or tabs between numbers ', 3)
    print('\n')
    initial_config = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
else:
    print("Invalid puzzle choice.")
    exit()

print('Enter your choice of algorithm')
print('Uniform Cost Search')
print('A* with the Misplaced Tile heuristic.')
print('A* with the Euclidean distance heuristic.')

algorithm_call = int(input('Choose your option (1, 2, or 3): '))

problem = Problem(initial=initial_config)
result = None
if algorithm_call == 1:
    result = uniform_cost_search(problem)
elif algorithm_call == 2:
    print('A* misplaced not implemented yet')
elif algorithm_call == 3:
    print('A* Euclidean not implemented yet')
else:
    print("Invalid algorithm choice.")

if result:
    steps = []
    while result:
        steps.append(result.configuration)
        result = result.parent
    steps.reverse()
    print("Solution path:")
    for step in steps:
        print(step)
else:
    print("No solution found.")

'''
elif algorithm_call == 2:
    print('calls A* misplaced')

elif algorithm_call == 3: 

    problem = Problem(initial=initial_config)  # Create a problem instance.
    result = PuzzleState.a_star(problem)  # Solve the problem using A* search.
    steps = []

    if result == None: #when the result of the A star program is none, means that a solution was not found. Concluding that the puzzle is impossible to solve
        print('No solution, Impossible puzzle')
        exit(1)

    while result:
        steps.append(result.configuration)
        result = result.parent     
    steps.reverse()
    print('Expanding state')
    g_n = 0
    
    for step in steps: 
        print('The best state to expand with g(n) =',g_n, 'and h(n) = ',)
        print(step[0],step[1],step[2])
        print(step[3],step[4],step[5])
        print(step[6],step[7],step[8], 'Expanding this node..')
        g_n+=1
        print('\n')
    
    print('Goal!!!')
    print('To solve this problem the search algorithm expanded a total of XXX nodes.')
    print('The maximum number of nodes in the queue at any one time: YYY.')
    print('The depth of the goal node was ZZZ.')
    #[a1,a2,a3]
    #[b1,b2,b3]
    #[c1,c2,c3]

    '''