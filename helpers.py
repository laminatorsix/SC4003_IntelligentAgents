from constants import *

# Takes in utility
def get_expected_utility(utility_list, reward_list, prob_list):
    result = float(0)

    for i in range(len(prob_list)):
        result += (float(reward_list[i]) + DISCOUNT * float(utility_list[i])) * float(prob_list[i])

    return round(result,5)

# Print 2D array
def print_2d_arr(arr):
    for r in range(len(arr)-1, -1, -1):
        line = ""
        for c in range(len(arr[0])):
            if (isinstance(arr[r][c], float)):
                # line += " " + str(round(arr[r][c], 1))
                line += " " + str(round(arr[r][c], 3))
            elif (isinstance(arr[r][c], Actions)):
                line += " " + str(arr[r][c].name)
            else:
                line += " " + str(arr[r][c])
            
        print(line + "\n")

