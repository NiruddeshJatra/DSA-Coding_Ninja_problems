# INTUITION:
# Imagine you are a ninja training for 'n' days. Each day, you can do one of three tasks, 
# but you can’t do the same task two days in a row. Each task gives you some points, 
# and your goal is to maximize the total points you earn over all days.
# 
# HOW DOES THIS SOLUTION WORK?
# 1. **Initialization:** On the first day, we pick the best two tasks (excluding the one we can't repeat the next day) and store the results.
# 2. **Dynamic Programming:** For each day, we try all tasks, making sure not to repeat the task done the previous day. 
#    We keep track of the maximum points possible for each scenario.
# 3. **Result:** After iterating through all days, the maximum points are stored in `dp[3]`.

# TIME COMPLEXITY:
# - O(n * 3 * 3) → For every day, we check all 3 tasks against the previous day's tasks.
#
# SPACE COMPLEXITY:
# - O(4) → We only store the previous day’s results, reducing space usage.

from typing import List

def ninjaTraining(n: int, points: List[List[int]]) -> int:
    # Step 1: Initialize dp array for the first day
    dp = [-1] * 4
    dp[0] = max(points[0][1], points[0][2])  # If last task was 0, choose the best of tasks 1 or 2
    dp[1] = max(points[0][0], points[0][2])  # If last task was 1, choose the best of tasks 0 or 2
    dp[2] = max(points[0][0], points[0][1])  # If last task was 2, choose the best of tasks 0 or 1
    dp[3] = max(points[0])                   # If no restriction, choose the maximum of all tasks

    # Step 2: Iterate through each day
    for day in range(1, n):
        temp = [-1] * 4
        for last in range(4):  # last = 3 means no restriction
            temp[last] = 0
            for task in range(3):
                if task != last:  # Avoid doing the same task as the previous day
                    point = points[day][task] + dp[task]
                    temp[last] = max(temp[last], point)

        # Step 3: Update dp for the next iteration
        dp = temp

    # Step 4: Return the maximum points when no restriction on the last task
    return dp[3]
