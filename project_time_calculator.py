def calculate_project_time_with_levels(tasks, programmers):
    task_times = {"Hard": 4, "Medium": 2, "Easy": 1}
    total_hours = sum(task_times[task] * count for task, count in tasks.items())
    
    # Calculate hours done by senior programmers
    senior_hours = min(programmers["Senior"] * 8, total_hours)
    remaining_hours = total_hours - senior_hours
    junior_hours = min(programmers["Junior"] * 8, remaining_hours)
    
    days_needed = (senior_hours + junior_hours + 7) // 8  # Round up to the next full day
    return days_needed

if __name__ == "__main__":
    tasks = {"Hard": 5, "Medium": 7, "Easy": 10}
    programmers = {"Senior": 2, "Junior": 5}
    print(calculate_project_time_with_levels(tasks, programmers))
