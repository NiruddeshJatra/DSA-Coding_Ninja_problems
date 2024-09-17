# Time Complexity: O(n log n + n * m), where n is the number of jobs and m is the maximum deadline. The O(n log n) comes from sorting the jobs, and the O(n * m) comes from trying to find an available slot for each job in the schedule.
# Space Complexity: O(m), where m is the maximum deadline, because of the schedule array.

# INTUITION:
# The problem can be approached by greedily selecting the jobs with the highest profit first and assigning them to the latest available slot (before or on their deadline). By sorting jobs by profit in descending order, we can ensure we maximize profit while filling up the available time slots.

# ALGO:
# 1. Sort the jobs based on profit in descending order (i.e., prioritize the most profitable jobs).
# 2. Determine the maximum deadline from all jobs to set the maximum length of the scheduling period.
# 3. Create an array 'schedule' to track which time slots are filled (-1 means the slot is empty).
# 4. Initialize variables 'jobCount' to track the number of scheduled jobs and 'profit' to track total profit.
# 5. For each job:
#     5.1 Check if there is an available time slot for this job (starting from its deadline and moving backwards).
#     5.2 If an available slot is found, assign the job to that slot, increase the job count, and add its profit.
# 6. Return the total number of scheduled jobs and the maximum profit.

def jobScheduling(jobs):
    # Step 1: Sort jobs by profit in descending order
    jobs.sort(key=lambda x: -x[2])
    
    # Step 2: Determine the maximum deadline
    maxJob = 0
    for i in range(len(jobs)):
        maxJob = max(jobs[i][1], maxJob)
    
    # Step 3: Create schedule array initialized to -1 (no jobs assigned yet)
    schedule = [-1] * (maxJob + 1)
    
    # Step 4: Initialize job count and total profit
    jobCount = 0
    profit = 0
    
    # Step 5: For each job, try to assign it to an available time slot
    for i in range(len(jobs)):
        for j in range(jobs[i][1], 0, -1):  # Start from the job's deadline and move backwards
            if schedule[j] == -1:  # If the slot is available
                jobCount += 1      # Increment the number of jobs scheduled
                profit += jobs[i][2]  # Add the job's profit
                schedule[j] = i  # Mark the slot as filled by this job
                break  # Move to the next job once assigned
    
    # Step 6: Return the total job count and profit
    return [jobCount, profit]
