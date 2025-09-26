# explore_datetime.py
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtain the current date/time, save it in `current_date`,
    print it as "YYYY-MM-DD HH:MM:SS", and return it.
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(days, base_date=None):
    """
    Calculate the date after adding `days` to `base_date` (or now if base_date is None).
    Save the result in `future_date` and print it as "YYYY-MM-DD".
    Returns the future_date (datetime object).
    """
    if base_date is None:
        base_date = datetime.now()
    future_date = base_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def prompt_for_int(prompt_text):
    """Prompt repeatedly until the user enters a valid integer; then return it."""
    while True:
        user_input = input(prompt_text).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer (e.g., 10 or -5).")

def main():
    # Part 1: display current date/time
    current_date = display_current_datetime()

    # Part 2: ask user and compute future date (use current_date as base)
    days_to_add = prompt_for_int("Enter the number of days to add to the current date: ")
    calculate_future_date(days_to_add, base_date=current_date)

if __name__ == "__main__":
    main()