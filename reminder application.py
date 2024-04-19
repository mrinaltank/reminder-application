from player import notification
import datetime
import time

def set_reminder():
    reminder_time = input("Enter the time for the reminder (HH:MM AM/PM): ")
    reminder_message = input("Enter your reminder message: ")

    try:
        reminder_datetime = datetime.datetime.strptime(reminder_time, "%I:%M %p")
        current_datetime = datetime.datetime.now()

        if reminder_datetime < current_datetime:
            print("Invalid time! Please enter a future time.")
            return

        time_difference = (reminder_datetime - current_datetime).total_seconds()
        time.sleep(time_difference)  # Wait until reminder time

        notification.notify(
            title="Reminder",
            message=reminder_message,
            timeout=10  # Notification will stay for 10 seconds
        )
    except ValueError:
        print("Invalid time format! Please enter time in HH:MM AM/PM format.")

if __name__ == "__main__":
    set_reminder()
