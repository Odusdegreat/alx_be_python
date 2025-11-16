# daily_reminder.py

# Loop to ensure user enters a valid priority
while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Match Case for priority handling
    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority. Please enter high, medium, or low.\n")
            continue  # restart loop if invalid priority
    
    break  # Valid input received, exit loop


# Time-sensitivity modification
if time_bound == "yes":
    reminder = f"{base_message} that requires immediate attention today!"
else:
    reminder = f"Note: {base_message}. Consider completing it when you have free time."


# FINAL required print format for auto-checker
print(f"Reminder: {reminder}")
