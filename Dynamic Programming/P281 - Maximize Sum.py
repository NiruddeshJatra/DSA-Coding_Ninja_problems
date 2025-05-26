# Time Complexity:
# - Top-down (Memoization): O(n), where n is the array length
# - Each state (position, swap_status) is computed once, with 2n total states
# - Bottom-up (Tabulation): O(n), iterating through n positions with 2 states each
# - Space-optimized: O(n), same time complexity with reduced space usage
# Space Complexity:
# - Top-down: O(n) for memoization table + O(n) for recursion stack = O(n)
# - Bottom-up: O(n) for the 2D DP table storing all states
# - Space-optimized: O(1) auxiliary space, only storing current and previous states

# INTUITION:
# The problem involves maximizing sum by selectively swapping elements between two arrays
# Key insights:
# - At each position, we can either swap or not swap the elements between arrays
# - The cost/benefit depends on both the swap penalty and alignment with previous choice
# - We need to track whether the previous position was swapped to maintain consistency  
# - This creates overlapping subproblems perfect for dynamic programming
# - Each position has two states: previous was swapped (True) or not swapped (False)

# Example:
# first_array = [1, 3, 5], second_array = [2, 4, 6], array_length = 3
# At each position i, we calculate:
# - Cost of not swapping: |first_array[i] - second_array[i]| + alignment_cost
# - Cost of swapping: |first_array[i] - second_array[i]| + alignment_cost  
# - Alignment cost depends on difference with previous position's final choice
# Position 0: Choose between (1,2) vs (2,1) - no previous alignment
# Position 1: Consider previous choice and calculate alignment + swap costs
# Position 2: Continue pattern, maximizing total sum across all decisions

# ALGO:
# 1. Define state: (current_position, was_previous_swapped)
# 2. For each position, calculate two options:
#    - No swap: current cost + optimal solution from next position (no swap)
#    - Swap: current cost + optimal solution from next position (with swap)
# 3. Current cost includes:
#    - Absolute difference between elements at current position
#    - Alignment cost with previous position's final configuration
# 4. Use memoization/tabulation to avoid recomputing identical subproblems
# 5. Return maximum sum starting from position 0 with no initial swap

from os import *
from sys import *
from collections import *
from math import *

def calculateMaximisedSum(first_array, second_array, array_length):
    
    # TOP-DOWN APPROACH (Memoization)
    memoization_cache = {}

    def solve_recursive(current_position, was_previous_swapped):
        # Base case: reached end of arrays
        if current_position == array_length:
            return 0

        # Check if this state was already computed
        state_key = (current_position, was_previous_swapped)
        if state_key in memoization_cache:
            return memoization_cache[state_key]

        # Determine previous position's final configuration
        if current_position > 0:
            if was_previous_swapped:
                previous_first_value, previous_second_value = second_array[current_position-1], first_array[current_position-1]
            else:
                previous_first_value, previous_second_value = first_array[current_position-1], second_array[current_position-1]
        else:
            previous_first_value, previous_second_value = 0, 0

        # Option 1: No swap at current position
        no_swap_cost = abs(first_array[current_position] - second_array[current_position])
        if current_position > 0:
            no_swap_cost += abs(first_array[current_position] - previous_second_value)
        no_swap_total = no_swap_cost + solve_recursive(current_position + 1, False)

        # Option 2: Swap at current position
        swap_cost = abs(first_array[current_position] - second_array[current_position])
        if current_position > 0:
            swap_cost += abs(second_array[current_position] - previous_second_value)
        swap_total = swap_cost + solve_recursive(current_position + 1, True)

        # Store and return maximum of both options
        memoization_cache[state_key] = max(no_swap_total, swap_total)
        return memoization_cache[state_key]

    return solve_recursive(0, False)

    # BOTTOM-UP APPROACH (Tabulation)
    # dp_table[position][swap_state] = maximum sum from position onwards
    dp_table = [[0, 0] for _ in range(array_length + 1)]

    # Fill table from right to left (bottom-up)
    for current_position in range(array_length - 1, -1, -1):
        for was_previous_swapped in [0, 1]:  # 0 = False, 1 = True
            # Determine previous position's configuration
            if current_position > 0:
                if was_previous_swapped:
                    previous_first_value, previous_second_value = second_array[current_position-1], first_array[current_position-1]
                else:
                    previous_first_value, previous_second_value = first_array[current_position-1], second_array[current_position-1]
            else:
                previous_first_value, previous_second_value = 0, 0

            # Option 1: No swap at current position
            no_swap_cost = abs(first_array[current_position] - second_array[current_position])
            if current_position > 0:
                no_swap_cost += abs(first_array[current_position] - previous_second_value)
            no_swap_total = no_swap_cost + dp_table[current_position + 1][0]

            # Option 2: Swap at current position
            swap_cost = abs(first_array[current_position] - second_array[current_position])
            if current_position > 0:
                swap_cost += abs(second_array[current_position] - previous_second_value)
            swap_total = swap_cost + dp_table[current_position + 1][1]

            # Store maximum of both options
            dp_table[current_position][was_previous_swapped] = max(no_swap_total, swap_total)

    return dp_table[0][0]

    # SPACE-OPTIMIZED APPROACH
    # Only keep track of previous and current position states
    next_position_states, current_position_states = [0, 0], [0, 0]

    # Process from right to left
    for current_position in range(array_length - 1, -1, -1):
        for was_previous_swapped in [0, 1]:
            # Determine previous position's configuration
            if current_position > 0:
                if was_previous_swapped:
                    previous_first_value, previous_second_value = second_array[current_position-1], first_array[current_position-1]
                else:
                    previous_first_value, previous_second_value = first_array[current_position-1], second_array[current_position-1]
            else:
                previous_first_value, previous_second_value = 0, 0

            # Option 1: No swap at current position
            no_swap_cost = abs(first_array[current_position] - second_array[current_position])
            if current_position > 0:
                no_swap_cost += abs(first_array[current_position] - previous_second_value)
            no_swap_total = no_swap_cost + next_position_states[0]

            # Option 2: Swap at current position
            swap_cost = abs(first_array[current_position] - second_array[current_position])
            if current_position > 0:
                swap_cost += abs(second_array[current_position] - previous_second_value)
            swap_total = swap_cost + next_position_states[1]

            # Store maximum of both options
            current_position_states[was_previous_swapped] = max(no_swap_total, swap_total)

        # Move to next iteration: current becomes next
        current_position_states, next_position_states = next_position_states, current_position_states

    return next_position_states[0]
