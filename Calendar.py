#Kennedi Wilson 
# Date: 10/22/24
# CS 141 Face-to-Face
# Calendar Project (Python Version)

import datetime

def main():
    # Prompt the user for a date
    date_input = input("Enter a date (mm/dd): ")

    try:
        month_str, day_str = date_input.strip().split("/")
        month = int(month_str)
        day = int(day_str)

        # Validate date input
        if not 1 <= month <= 12:
            print("Invalid month. Please enter a valid date in mm/dd format.")
            return
        if not 1 <= day <= 31:
            print("Invalid day. Please enter a valid date in mm/dd format.")
            return

        print(f"Month: {month}, Day: {day}")
        print(f"\nCalendar for Month: {month}\n")
        calendar(month)

        # Today's date
        today = datetime.datetime.now()
        current_month = today.month
        current_day = today.day

        print("\nCalendar for Today's Date:")
        calendar(current_month)
        print_date_left(current_month, current_day)

    except ValueError:
        print("Invalid input. Please enter a valid date in mm/dd format.")

def calendar(month):
    print(f"Month: {month}")
    begin = 1
    end = 7

    for _ in range(5):
        line()
        date_range(begin, end)
        spacing()
        spacing()
        begin += 7
        end += 7
    line()

def line():
    print("=" * 50)

def date_range(start, end):
    for i in range(start, end + 1):
        print(f"| {i:2}   ", end="")  # 2 digits, left-padded, with spaces for alignment
    print("|")

def spacing():
    print("|      " * 7 + "|")

def print_date_left(month, day):
    print(f"\nMonth: {month}, Day: {day}")

if __name__ == "__main__":
    main()

