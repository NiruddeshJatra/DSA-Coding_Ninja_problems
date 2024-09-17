# Time Complexity: O(n log n) 
# This is due to the sorting step for both arrival and departure times, which dominates the time complexity.

# Space Complexity: O(1)
# We only use a few extra variables (`minDt`, `ans`, and `platform_needed`), all of which take constant space.

# INTUITION:
# The idea is to track when a train arrives and when a train departs, ensuring that we keep count of how many platforms are required at any given time. 
# If a train arrives before the next train departs, a new platform is needed. If a train departs before the next train arrives, one platform can be freed up.

# ALGO:
# 1. **Sort both arrival and departure times** to process them in the correct order.
# 2. **Initialize tracking variables**:
#    - `minDt` to track the earliest departure time.
#    - `ans` to track the maximum number of platforms needed at any time.
#    - `platform_needed` to track the platforms currently in use.
# 3. **Iterate through the arrival times**:
#    - If a train arrives before the next earliest train departs, increase the platform count.
#    - If a train departs before the next train arrives, reduce the platform count.
#    - Keep track of the maximum number of platforms required at any time.
# 4. **Return the result** as the maximum number of platforms required.

def calculateMinPlatforms(at, dt, n):
    # Step 1: Sort arrival and departure times
    at.sort()
    dt.sort()

    # Step 2: Initialize tracking variables
    minDt = 0  # To track the next train's departure time
    ans = 1  # Minimum number of platforms needed
    platform_needed = 1  # Keep track of platforms currently required

    # Step 3: Iterate through the sorted arrival times
    for i in range(1, len(at)):
        # If the current arrival happens after or when the next departure occurs
        if at[i] > dt[minDt]:
            minDt += 1  # Train departs, reduce platform_needed
        else:
            platform_needed += 1  # Train arrives before departure, increase platform_needed

        # Track maximum platforms required
        ans = max(ans, platform_needed)

    # Step 4: Return the result
    return ans
