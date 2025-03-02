from constants import *
from helpers import *
from grid import Grid

# Value Iteration function
def value_iteration(grid: Grid):
    # Initialise all values to 0
    grid.initialise_values(0)
    utility_map = [r[:] for r in grid.get_utilities()]
    policy_map = [r[:] for r in grid.get_policies()]
    # Max diff
    theta = float("inf")
    iter = 0
    # Continue iteration until maximum difference between iterations less than threshold difference
    
    while theta > DIFF_THRESHOLD:
    # for i in range(2):
        theta = -float("inf")
        for r in range(ROWS):
            for c in range(COLS):
                if grid.get_state(r, c) == States.WALL:
                    continue

                # Get optimal value and policy
                v_max = -float("inf")
                a_max = Actions.UP
                for a in Actions:
                    if a == Actions.NONE:
                        continue
                    # Get expected future utility and immediate reward
                    u_1, r_1 = grid.get_next_state(r, c, a) # Straight
                    u_2, r_2 = grid.get_next_state(r, c, a.prev()) # Left
                    u_3, r_3 = grid.get_next_state(r, c, a.next()) # Right
                    
                    # Calculate expected utility
                    v = get_expected_utility([u_1, u_2, u_3], [r_1, r_2, r_3], [P_STRAIGHT, P_LEFT, P_RIGHT])
                    if(v > v_max):
                        a_max = a
                        v_max = v

                # Get current value
                v_curr = grid.get_utility(r, c)

                # Get max diff
                theta = max(theta, (abs(v_curr - v_max)))
                utility_map[r][c] = v_max
                policy_map[r][c] = a_max.name
        iter += 1
        # Update utilities stored in grid at end of iteration
        grid.update_utilities(utility_map)
        # iter += 1
    return policy_map, utility_map

# Policy Iteration
def policy_iteration(grid: Grid):
    # Initialise policy
    grid.initialise_policies(Actions.UP)

    policy_map = [r[:] for r in grid.get_policies()]
    utility_map = [r[:] for r in grid.get_utilities()]
    iter = 0

    while(iter < 1000):
        # Policy Evaluation
        # for i in range(2):
        while theta > DIFF_THRESHOLD:
            theta = -float("inf")
            for r in range(ROWS):
                for c in range(COLS):
                    if grid.get_state(r, c) == States.WALL:
                        policy_map[r][c] == Actions.NONE
                        continue
                    a = policy_map[r][c]

                    # Policy evaluation
                    u_1, r_1 = grid.get_next_state(r, c, a) # Straight
                    u_2, r_2 = grid.get_next_state(r, c, a.prev()) # Left
                    u_3, r_3 = grid.get_next_state(r, c, a.next()) # Right
                        
                    # Calculate expected utility
                    v = get_expected_utility([u_1, u_2, u_3], [r_1, r_2, r_3], [P_STRAIGHT, P_LEFT, P_RIGHT])

                    # Get current value
                    v_prev = grid.get_utility(r, c)

                    # Get max diff
                    theta = max(theta, (abs(v_prev - v)))
                    utility_map[r][c] = v
        
        grid.update_utilities(utility_map)
        
        # Policy Improvement
        policy_stable = True
        for r in range(ROWS):
            for c in range(COLS):
                a_prev = policy_map[r][c]

                if grid.get_state(r, c) == States.WALL:
                    policy_map[r][c] == Actions.NONE
                    continue

                v_max = -float("inf")
                a_max = Actions.UP

                for a in Actions:
                    if a == Actions.NONE:
                        continue

                    u_1, r_1 = grid.get_next_state(r, c, a) # Straight
                    u_2, r_2 = grid.get_next_state(r, c, a.prev()) # Left
                    u_3, r_3 = grid.get_next_state(r, c, a.next()) # Right
                        
                    # Calculate expected utility
                    v = get_expected_utility([u_1, u_2, u_3], [r_1, r_2, r_3], [P_STRAIGHT, P_LEFT, P_RIGHT])

                    # Get best action
                    if v > v_max:
                        v_max = v
                        a_max = a

                if a_prev != a_max:
                    policy_stable = False
                policy_map[r][c] = a_max
        grid.update_policies(policy_map)

        # Break when policies converge
        if policy_stable:
            break
            

    
    #

    # Policy Improvement
    # policy iteration function