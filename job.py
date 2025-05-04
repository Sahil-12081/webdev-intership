# Function to schedule jobs to maximize profit
def printJobScheduling(arr, t):
    n = len(arr)

    # Step 1: Sort all jobs in descending order of profit
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Step 2: Initialize the result array to keep track of free time slots
    result = [False] * t  # To check if time slot is filled
    job = ['-1'] * t      # To store result (sequence of jobs)

    # Step 3: Iterate through all given jobs
    for i in range(n):
        # Find a free slot for this job (starting from the last possible slot)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break

    # Step 4: Print the scheduled jobs
    print("Following is the maximum profit sequence of jobs:")
    print(" -> ".join(job))


# Driver code
if __name__ == "__main__":
    # Each job is represented as [Job ID, Deadline, Profit]
    arr = [['a', 2, 100], ['b', 1, 19], ['c', 2, 27],
           ['d', 1, 25], ['e', 3, 15]]
    
    t = 3  # Number of time slots
    printJobScheduling(arr, t)
