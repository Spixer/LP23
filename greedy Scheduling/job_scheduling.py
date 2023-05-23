# Jobs, Profit, Slot
profit = [15,27,10,100, 150]
jobs = ["j1", "j2", "j3", "j4", "j5"]
deadline = [2,3,3,3,4] 

profitNJobs = list(zip(profit,jobs,deadline))
profitNJobs = sorted(profitNJobs, key = lambda x: x[0], reverse = True)
slot = []
for _ in range(len(jobs)):
    slot.append(0)

profit = 0
ans = []

for i in range(len(jobs)):
    ans.append('null')

for i in range(len(jobs)):
        job = profitNJobs[i]
        #check if slot is occupied
        for j in range(job[2], 0, -1):
            if slot[j] == 0:
                ans[j] = job[1]
                profit += job[0]
                slot[j] = 1
                break
        
print("Jobs scheduled buddy:",ans[1:])
print(profit)





# def schedule_jobs(jobs):
#     # sort jobs by their deadlines in ascending order
#     jobs.sort(key=lambda x: x[1])
    
#     # initialize empty result list and a set to keep track of assigned job ids
#     result = []
#     assigned_jobs = set()
    
#     # iterate through each job in the sorted list
#     for job in jobs:
#         job_id, deadline, profit = job
#         # check if there is still time to assign the job
#         for i in range(deadline, 0, -1):
#             if i not in assigned_jobs:
#                 # assign the job to the latest available slot before its deadline
#                 result.append(job)
#                 assigned_jobs.add(i)
#                 break
    
#     # calculate the total profit earned from the scheduled jobs
#     total_profit = sum(job[2] for job in result)
#     return result, total_profit

# # take user input for number of jobs and their details
# n = int(input("Enter the number of jobs: "))
# jobs = []
# for i in range(n):
#     job_id = i+1
#     deadline = int(input(f"Enter the deadline for job {job_id}: "))
#     profit = int(input(f"Enter the profit for job {job_id}: "))
#     jobs.append((job_id, deadline, profit))

# # call the job scheduling function and print the results
# scheduled_jobs, total_profit = schedule_jobs(jobs)
# print("Scheduled Jobs: ", scheduled_jobs)
# print("Total Profit: ", total_profit)
