
# Time Complexity: O(n log n), where n is the number of meetings. This is primarily due to the sorting step.
# Space Complexity: O(n), as we are storing the start and end times of each meeting in a separate list `meetingTime`.

# INTUITION:
# We need to schedule the maximum number of meetings such that no two meetings overlap. 
# The key to solving this problem is to select meetings that finish the earliest. By doing so, we leave more time for subsequent meetings. 
# This approach can be thought of as a greedy algorithm, where at each step, we choose the meeting that ends first among the remaining ones.

# ALGO:
# 1. **Create a List of Meeting Times**:
#    - Store the start and end times of each meeting as a pair.
# 2. **Sort Meetings by End Time**:
#    - Sort the meetings based on their end times. This allows us to select the earliest finishing meeting first, leaving room for more meetings.
# 3. **Schedule Meetings**:
#    - Initialize the first meeting as scheduled and track the time the first meeting finishes (`freetime`).
#    - Iterate through the remaining meetings:
#       - If a meeting starts after the current meeting's `freetime`, schedule it and update `freetime`.
# 4. **Return the Number of Meetings**:
#    - The final answer is the number of non-overlapping meetings we can schedule.

from typing import List

def maximumMeetings(start: List[int], end: List[int]) -> int:
    # Step 1: Combine start and end times into a list of meeting times
    meetingTime = []
    for i in range(len(start)):
        meetingTime.append([start[i], end[i]])

    # Step 2: Sort the meeting times by their end time
    meetingTime.sort(key=lambda x: x[1])

    # Step 3: Schedule the first meeting and track the end time of the last meeting
    ans, freetime = 1, meetingTime[0][1]

    # Step 4: Iterate over the remaining meetings and schedule non-overlapping ones
    for time in meetingTime[1:]:
        if time[0] > freetime:  # Check if the meeting starts after the last scheduled meeting ends
            ans += 1
            freetime = time[1]  # Update freetime to the end of the current meeting

    # Step 5: Return the total number of non-overlapping meetings
    return ans
