import calendar


def days_in_month(year, month):
    """
    Returns the number of days in a specific month of a given year.

    Args:
        year (int): The specified year.
        month (int): The specified month (1-12).

    Returns:
        int: Number of days in the given month of the specified year.
    """
    return calendar.monthrange(year, month)[1]


if __name__ == "__main__":
    """
    Main program to demonstrate the use of the `days_in_month` function.
    Prompts the user for a year and a month, and displays the corresponding number of days.
    """
    # Prompt the user for the year and the month
    year = int(input("Enter the year: "))
    month = int(input("Enter the month number (1-12): "))

    # Calculate the number of days in the month
    days = days_in_month(year, month)

    # Display the result
    print(f"Month {month} of year {year} has {days} days.")
