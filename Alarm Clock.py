import time
from datetime import datetime

# Set alarm
def set_alarm():
    while True:
        alarm_time = input("Set the alarm time (HH:MM):")
        try:
            valid_time = datetime.strptime(alarm_time, "%H:%M")
            print(f"Alarm set for {valid_time.strftime('%H:%M')}.")
            return valid_time.time()
        except ValueError:
            print("Invalid time format! Please use 'HH:MM' (24-hour format).")

# Check the alarm
def alarm_check(alarm_time):
    print("Waiting for the alarm...")
    while True:
        now = datetime.now().time().replace(second=0, microsecond=0)
        if now == alarm_time:
            print("Alarm ringing! Wake up!")
            break
        time.sleep(1)  # Sleep for 1 second before checking again

# Main function
def main():
    """Main function to run the alarm clock."""
    alarm_time = set_alarm()  # Set the alarm
    alarm_check(alarm_time)   # Monitor the time until the alarm triggers

# Run the alarm clock if the script is executed directly
if __name__ == "__main__":
    main()
