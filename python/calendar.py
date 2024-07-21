from datetime import datetime, timedelta
import sys


# Checking shared argument matches the format of the month
def get_date():
    # Return current month if No argument provided
    if len(sys.argv) <= 1:
        return datetime.now().replace(day=1)

    # Displayed an error, if less than 2 command line arguments or the first argument is not "-m"
    if len(sys.argv) <= 2 or sys.argv[1] != "-m":
        print("Usage: python calendar.py -m <month>")
        sys.exit(1)

    # The handling of the second command line argument to determine whether it is an integer or not
    try:
        month = int(sys.argv[2])
    except ValueError as e:
        print(f"Error: {e} is not allowed. Month must be an integer")
        sys.exit(1)

    # Display an error message if the second command line argument is not between 1 and 12
    if not 1 <= month <= 12:
        print("Error: Month must be between 1 and 12")
        sys.exit(1)

    return datetime(datetime.now().year, month, 1)


first_day_of_month = get_date()
days_of_week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

# Calculating the number of days in the month
if first_day_of_month.month == 12:
    first_day_next_month = datetime(first_day_of_month.year + 1, 1, 1)
else:
    first_day_next_month = datetime(first_day_of_month.year, first_day_of_month.month + 1, 1)

last_day_of_month = first_day_next_month - timedelta(days=1)
start_date = first_day_of_month.weekday()

date_list = []
for i in range(last_day_of_month.day):
    date_list.append(first_day_of_month + timedelta(days=i))

# formatting and printing the calendar
print(first_day_of_month.strftime("   %B  %Y   "))
print(" ".join(days_of_week))
print("   " * start_date, end="")


for date in date_list:
    print(f"{date.day:2}", end=" ")

    if date.weekday() == 6:
        print()

