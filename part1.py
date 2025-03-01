# no terminal states
from constants import *
from helpers import *
from grid import Grid
class Part1:
    # Find optimal policy
    # def __init__(self):
    #     self.grid = Grid(0)

    # Function to find optimal policy
    def value_iteration(self):
        self.grid = Grid(0)

        # Initialise policy map
        # Copy utility map
        utility_map = [r[:] for r in self.grid.get_utilities()]
        policy_map = [[Actions.UP for j in range(COLS)] for i in range(ROWS)];
        max_diff = float("inf")
        iter = 0
        # Continue iteration until maximum difference between iterations less than threshold difference
        while max_diff > DIFF_THRESHOLD:
        # for i in range(1):
            max_diff = -float("inf")
            for r in range(ROWS):
                for c in range(COLS):
                    if self.grid.get_state(r, c) == States.WALL:
                        continue
                    optimal_policy, optimal_utility = self.get_optimal_policy(r, c)
                    curr_utility = self.grid.get_latest_utility(r, c)

                    # Get max diff
                    max_diff = max(max_diff, (abs(curr_utility - optimal_utility)))
                    utility_map[r][c] = optimal_utility
                    policy_map[r][c] = optimal_policy
            iter += 1
            
            # Update utilities stored in grid at end of iteration
            self.grid.update_utilities(utility_map)
            # iter += 1
        print(policy_map)
        print(utility_map)
        print(iter)

        
        


        # Start with every U(s) = 0
        # Iterate until convergence
        # U_i+1(s) <- R(s) + DF * max(sum(P(s'|s,a)U_i(s')))
    
    def policy_iteration():
        # policy iteration
        print("lol")
    
    # Get optimal action and utility
    def get_optimal_policy(self, r: int, c: int):
        optimal_utility = -float("inf")
        optimal_action = Actions.UP
        for action in Actions:
            # Get current state
            s = self.grid.get_state(r, c)
            # Straight
            u_1 = self.grid.get_next_state(r, c, action)
            # Left
            u_2 = self.grid.get_next_state(r, c, action.prev())
            # Right
            u_3 = self.grid.get_next_state(r, c, action.next())
            
            # Calculate expected utility
            expected_utility = get_expected_utility(s, [u_1, u_2, u_3], [P_STRAIGHT, P_LEFT, P_RIGHT])
            # if(r == 4 and c == 0 and action == Actions.UP):
            #     print("u1: " + str(u_1) + " u2: " + str(u_2) + " u3: " + str(u_3))
            #     print("expected util: " + str(expected_utility))
            #     print("prev action: " + str(action.prev()))
            #     print("next action: " + str(action.next()))
            if(expected_utility > optimal_utility):
                optimal_action = action
                optimal_utility = expected_utility
        # if(r == 4 and c == 0):
        #     print(optimal_action)
        return (optimal_action, optimal_utility)
            





