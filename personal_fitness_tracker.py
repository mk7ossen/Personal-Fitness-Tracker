import csv
import datetime
import matplotlib.pyplot as plt

def log_activity():
    date = input("Enter date (YYYY-MM-DD): ")
    activity = input("Enter activity name: ")
    duration = int(input("Enter duration (minutes): "))
    calories = int(input("Enter calories burned: "))
    with open("fitness_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, activity, duration, calories])
    print("Activity logged successfully!")

def weekly_summary():
    from datetime import datetime, timedelta
    today = datetime.today()
    last_week = today - timedelta(days=7)
    total_duration = 0
    total_calories = 0

    with open("fitness_data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row: 
                continue
            activity_date = datetime.strptime(row[0], "%Y-%m-%d")
            if last_week <= activity_date <= today:
                total_duration += int(row[2])
                total_calories += int(row[3])

    print(f"Weekly Summary: \nTotal Duration: {total_duration} minutes\nTotal Calories Burned: {total_calories}")

def set_goals():
    weekly_minutes = int(input("Set your weekly exercise goal (in minutes): "))
    daily_calories = int(input("Set your daily calorie burn goal: "))
    with open("fitness_goals.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Weekly Minutes", weekly_minutes])
        writer.writerow(["Daily Calories", daily_calories])
    print("Goals set successfully!")

def calculate_bmi():
    height = float(input("Enter height (in meters): "))
    weight = float(input("Enter weight (in kilograms): "))
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Normal weight")
    elif 25 <= bmi < 29.9:
        print("Overweight")
    else:
        print("Obesity")

def visualize_progress():
    dates = []
    durations = []
    with open("fitness_data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue
            dates.append(row[0])
            durations.append(int(row[2]))
    
    plt.plot(dates, durations, marker='o')
    plt.title("Fitness Progress")
    plt.xlabel("Date")
    plt.ylabel("Duration (Minutes)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("\nPersonal Fitness Tracker Menu:")
        print("1. Log a new activity")
        print("2. View weekly summary")
        print("3. Set fitness goals")
        print("4. Calculate BMI")
        print("5. Visualize progress")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            log_activity()
        elif choice == "2":
            weekly_summary()
        elif choice == "3":
            set_goals()
        elif choice == "4":
            calculate_bmi()
        elif choice == "5":
            visualize_progress()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
