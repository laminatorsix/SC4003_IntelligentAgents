from constants import *
class Grid():
    # Define grid
    # Default initialisation
    def __init__(self):
        self.grid = [[States.WHITE for j in range(COLS)] for i in range(ROWS)]
        self.utilities = [[0 for j in range(COLS)] for i in range(ROWS)]
        self.policies = [[Actions.NONE for j in range(COLS)] for i in range(ROWS)];

    def get_utilities(self):
        return self.utilities

    def initialise_values(self, value: int):
        self.utilities = [[value for j in range(COLS)] for i in range(ROWS)]

    def initialise_policies(self, action: Actions):
        self.policies = [[action for j in range(COLS)] for i in range(ROWS)];

    def get_policies(self):
        return self.policies

    def update_policies(self, policies):
        self.policies = [r[:] for r in policies]

    def update_utilities(self, utilities):
        self.utilities = [r[:] for r in utilities]
    
    def initialise(self, green_cells, brown_cells, wall_cells, supergreen_cells=[]):
        for r, c in green_cells:
            self.grid[r][c] = States.GREEN
        for r, c in supergreen_cells:
            self.grid[r][c] = States.SUPERGREEN
        for r, c in brown_cells:
            self.grid[r][c] = States.BROWN
        for r, c in wall_cells:
            self.grid[r][c] = States.WALL

    # Function to initialise grid for part 1
    def initialiseGrid1(self):
        green_cells = [(5, 0), (5, 2), (5, 5), (4, 3), (3, 4), (2, 5)]
        brown_cells = [(4, 1), (4, 5), (3, 2), (2, 3), (1, 4)]
        wall_cells = [(5, 1), (4, 4), (1, 1), (1, 2), (1, 3)]

        for r, c in green_cells:
            self.grid[r][c] = States.GREEN
            # self.utilities[r][c] = States.GREEN.reward
        for r, c in brown_cells:
            self.grid[r][c] = States.BROWN
            # self.utilities[r][c] = States.BROWN.reward
        for r, c in wall_cells:
            self.grid[r][c] = States.WALL
            # self.utilities[r][c] = States.WALL.reward
    
    # Function to initialise grid for part 2
    def initialiseGrid2(self):
        green_cells = [(0, 0)]
        supergreen_cells = [(3, 5)]
        brown_cells = [(5, 1), (0, 1), (0, 4), (0, 5), (4, 4)]
        wall_cells = [(0, 3), (2, 3), (3, 3), (4, 3)]

        for r, c in green_cells:
            self.grid[r][c] = States.GREEN
        for r, c in supergreen_cells:
            self.grid[r][c] = States.SUPERGREEN
        for r, c in brown_cells:
            self.grid[r][c] = States.BROWN
        for r, c in wall_cells:
            self.grid[r][c] = States.WALL

    def get_reward(self, r, c) -> int:
        return self.grid[r][c].reward
    
    def get_state(self, r, c) -> States:
        return self.grid[r][c]
    
    def get_utility(self, r, c) -> int:
        return self.utilities[r][c]

    # Function to get utility of next state and immediate reward
    def get_next_state(self, r: int, c: int, action: Actions):
        new_r, new_c = r, c
        if action == Actions.UP:
            if r != ROWS-1:
                new_r += 1
        elif action == Actions.RIGHT:
            if c != COLS-1:
                new_c += 1
        elif action == Actions.LEFT:
            if c != 0:
                new_c -= 1
        elif action == Actions.DOWN:
            if r != 0:
                new_r -= 1
        
        # if hit wall or stay in place
        if self.grid[new_r][new_c] == States.WALL:
            return self.utilities[r][c], self.grid[r][c].reward
        return self.utilities[new_r][new_c], self.grid[new_r][new_c].reward
        
    def update_utility(self, r, c, utility):
        self.utilities[r][c] = utility

    # def get_optimal_utility(self, r, c) -> int:
    #     if min(r, c) < 0 or r >= ROWS or c >= COLS:
    #         return 0
    #     curr_state = self.grid[r][c]
