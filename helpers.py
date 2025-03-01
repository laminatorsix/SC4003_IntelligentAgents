from constants import *

# Takes in utility
def get_expected_utility(state, utility_list, prob_list):
    result = 0
    # First iteration, no discount
    # if iter != 1:
    for i in range(len(prob_list)):
        curr_utility = state.reward + utility_list[i] * DISCOUNT
        result += prob_list[i] * curr_utility
    # else:
    #     for i in range(len(prob_list)):
    #         curr_utility = state.reward + utility_list[i]
    #         result += prob_list[i] * curr_utility

    return result


