# no terminal states
from constants import *
from helpers import *
from algo import *
from grid import Grid
# class Part1:
#     # Find optimal policy
#     # def __init__(self):
#     #     grid = Grid(0)


def value_iteration_1():
    green_cells = [(5, 0), (5, 2), (5, 5), (4, 3), (3, 4), (2, 5)]
    brown_cells = [(4, 1), (4, 5), (3, 2), (2, 3), (1, 4)]
    wall_cells = [(5, 1), (4, 4), (1, 1), (1, 2), (1, 3)]
    grid = Grid()
    grid.initialise(green_cells, brown_cells, wall_cells)
    policy_map, utility_map = value_iteration(grid)
    print_2d_arr(policy_map)
    print_2d_arr(utility_map)

def value_iteration_test():
    green_cells = [(0, 0)]
    supergreen_cells = [(3, 5)]
    brown_cells = [(5, 1), (0, 1), (0, 4), (0, 5), (4, 4)]
    wall_cells = [(0, 3), (2, 3), (3, 3), (4, 3)]
    grid = Grid()
    grid.initialise(green_cells, brown_cells, wall_cells, supergreen_cells)
    policy_map, utility_map = value_iteration(grid)
    print_2d_arr(policy_map)
    print_2d_arr(utility_map)

# KEY THING: differentiate  VALUE and REWARD
# Function to find optimal policy
# def value_iteration(grid):
#     # grid = Grid(0)
#     utility_map = [r[:] for r in grid.get_utilities()]
#     policy_map = [[Actions.UP.name for j in range(COLS)] for i in range(ROWS)];
#     # Max diff
#     theta = float("inf")
#     iter = 0
#     # Continue iteration until maximum difference between iterations less than threshold difference
    
#     while theta > DIFF_THRESHOLD:
#     # for i in range(1000):
#         theta = -float("inf")
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid.get_state(r, c) == States.WALL:
#                     continue

#                 # Get optimal value and policy
#                 v_max = -float("inf")
#                 a_max = Actions.UP
#                 for a in Actions:
#                     # Get expected future utility and immediate reward
#                     u_1, r_1 = grid.get_next_state(r, c, a) # Straight
#                     u_2, r_2 = grid.get_next_state(r, c, a.prev()) # Left
#                     u_3, r_3 = grid.get_next_state(r, c, a.next()) # Right
                    
#                     # Calculate expected utility
#                     v = get_expected_utility([u_1, u_2, u_3], [r_1, r_2, r_3], [P_STRAIGHT, P_LEFT, P_RIGHT])
#                     if(v > v_max):
#                         a_max = a
#                         v_max = v

#                 # Get current value
#                 v_curr = grid.get_utility(r, c)

#                 # Get max diff
#                 theta = max(theta, (abs(v_curr - v_max)))
#                 utility_map[r][c] = v_max
#                 policy_map[r][c] = a_max.name
#         iter += 1
#         # Update utilities stored in grid at end of iteration
#         grid.update_utilities(utility_map)
#         # iter += 1
#     return policy_map, utility_map
    
    # print(policy_map[5][0])
    # print(utility_map[5][0])

def policy_iteration():
    # policy iteration
    print("lol")

    # Get optimal action and utility
    # def get_optimal_policy(self, r: int, c: int):
    #     optimal_utility = -float("inf")
    #     optimal_action = Actions.UP
    #     # Get immediate reward

    #     for action in Actions:
    #         # Straight
    #         # Get expected future utility and immediate reward
    #         u_1, r_1 = grid.get_next_state(r, c, action)
    #         # Left
    #         u_2, r_2 = grid.get_next_state(r, c, action.prev())
    #         # Right
    #         u_3, r_3 = grid.get_next_state(r, c, action.next())
            
    #         # Calculate expected utility
    #         new_utility = get_expected_utility([u_1, u_2, u_3], [r_1, r_2, r_3], [P_STRAIGHT, P_LEFT, P_RIGHT])
    #         # if(r == 5 and c == 0 and action == Actions.UP):
    #         #     print("u1: " + str(u_1) + " u2: " + str(u_2) + " u3: " + str(u_3))
    #         #     print("imediate reward: " + str(reward))
    #         #     print("expected util: " + str(expected_utility))
    #         #     print("prev action: " + str(action.prev()))
    #         #     print("next action: " + str(action.next()))
    #         if(new_utility > optimal_utility):
    #             optimal_action = action
    #             optimal_utility = new_utility

    #     return (optimal_action, optimal_utility)
    
            





