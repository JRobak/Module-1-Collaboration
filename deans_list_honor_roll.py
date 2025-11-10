# Name: Jacob Robak
# File: deans_list_honor_roll.py
# Description:
# This program asks for student names and GPAs, then checks
# whether each student qualifies for the Dean's List or the Honor Roll.
# The program stops when the user enters 'ZZZ' as the last name.

while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")

    if last_name.upper() == "ZZZ":
        print("\nExiting program. Goodbye!")
        break

    first_name = input("Enter the student's first name: ")
    try:
        gpa = float(input("Enter the student's GPA: "))
    except ValueError:
        print("Invalid input. Please enter a numeric GPA.\n")
        continue

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.\n")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.\n")
    else:
        print(f"{first_name} {last_name} did not qualify for either list.\n")
