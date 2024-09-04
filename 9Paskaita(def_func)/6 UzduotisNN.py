# Develop a function that schedules tasks based on their deadlines and durations. Each task should be represented as a dictionary, which includes keys for 'name', 'deadline', and 'duration' (in days). The function should calculate the start date for each task by subtracting the duration from the deadline, and return a list of tasks sorted by their start dates.
#
# Functionality:
#
# Input Handling: Prompt the user to enter the number of tasks they wish to schedule. For each task, the user should provide a name, a deadline (in YYYY-MM-DD format), and a duration (in days).
#
# Scheduling Logic: Calculate the start date for each task by subtracting the task duration from its deadline. Handle this using Python's datetime module.
#
# Sorting: Sort tasks based on their calculated start dates to ensure tasks are listed in the order they should be started.
#
# User Feedback: Display the list of tasks in the order they should be started, showing the task names sorted by start dates.
#
# Enter number of tasks: 2
# Enter task name: Project Report
# Enter deadline (YYYY-MM-DD): 2024-05-20
# Enter duration (days): 3
# Enter task name: Research Phase
# Enter deadline (YYYY-MM-DD): 2024-05-18
# Enter duration (days): 2
# Scheduled Tasks: ['Research Phase', 'Project Report']