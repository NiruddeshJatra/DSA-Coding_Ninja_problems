# Time Complexity: O(n log n), where n is the number of processes. The dominant factor is the sorting of the jobs based on arrival time and burst time.
# Space Complexity: O(n), as we are storing the job details and keeping track of waiting and turnaround times for each process.

# INTUITION:
# The idea is to schedule the processes based on the shortest job first (SJF) principle, i.e., always selecting the process with the shortest burst time for execution. Since this is a non-preemptive version, once a process starts executing, it runs till completion without interruption.
# We also need to keep track of waiting times and turnaround times:
# 1. Waiting Time: The amount of time a process has been in the ready queue before it gets executed.
# 2. Turnaround Time: The total time taken from arrival to completion of the process.

# ALGO:
# 1. Create a list `jobTimes` where each entry contains the process ID, arrival time, and burst time of each process.
# 2. Sort the list based on the arrival time, burst time, and then process ID, as we want to give priority to processes with earlier arrival times and shorter burst times.
# 3. Initialize variables for tracking completion time, waiting time, and turnaround time. Use a list `isProcessed` to mark processes that have been completed.
# 4. Loop through the sorted jobs:
#    4.1 For each process, calculate the turnaround time as the difference between completion time and arrival time.
#    4.2 Calculate the waiting time as the difference between turnaround time and burst time.
#    4.3 Mark the process as completed and append the details to the `jobSchedule`.
# 5. Return the final `jobSchedule` containing the process ID, arrival time, burst time, waiting time, and turnaround time for each process.

def shortestJobFirst(n, processId, arrivalTime, burstTime):
    # Step 1: Create a list of processes with processId, arrivalTime, and burstTime
    jobTimes = []
    for i in range(n):
        jobTimes.append([processId[i], arrivalTime[i], burstTime[i]])

    # Step 2: Sort jobs by arrival time, burst time, and processId
    jobTimes.sort(key=lambda x: (x[1], x[2], x[0]))

    # Step 3: Initialize variables for tracking completion time, waiting time, and turnaround time
    jobSchedule = []
    completionTime = 0
    waitingTimes = [0] * n
    turnaroundTimes = [0] * n
    isProcessed = [False] * n
    completedProcesses = 0

    # Step 4: Loop through the sorted jobs until all processes are completed
    while completedProcesses < n:
        # Step 4.1: Find available jobs that have already arrived
        availableJobs = []
        for i in range(n):
            if not isProcessed[i] and jobTimes[i][1] <= completionTime:
                availableJobs.append((jobTimes[i][2], i))  # Append (burstTime, index)

        # Step 4.2: Select the job with the shortest burst time
        if availableJobs:
            availableJobs.sort()
            idx = availableJobs[0][1]  # Get the index of the selected job

            # Step 4.3: Update completion time with the burst time of the selected process
            completionTime += jobTimes[idx][2]

            # Step 4.4: Calculate turnaround time and waiting time
            turnaroundTimes[idx] = completionTime - jobTimes[idx][1]
            waitingTimes[idx] = turnaroundTimes[idx] - jobTimes[idx][2]

            # Step 4.5: Mark the process as completed and increment completedProcesses
            isProcessed[idx] = True
            completedProcesses += 1

            # Step 4.6: Append process details to jobSchedule
            jobSchedule.append([jobTimes[idx][0], jobTimes[idx][1], jobTimes[idx][2], waitingTimes[idx], turnaroundTimes[idx]])

        else:
            # Step 4.7: If no jobs have arrived yet, increment the current time
            completionTime += 1

    # Step 5: Return the final job schedule with processId, arrivalTime, burstTime, waitingTime, and turnaroundTime
    return jobSchedule
