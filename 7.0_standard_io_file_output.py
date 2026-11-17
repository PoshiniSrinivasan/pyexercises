"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In:
# The program asks for the student's first name, last name,
# email address, study programme and year of study.

# 2. Process:
# It checks that the information is valid and saves each
# student's details as a new row in a CSV file.

# 3. Out, file name and columns:
# The output file is student_records.csv.
# Columns: first_name, last_name, email, programme, year_of_study.

# 4. Why these columns, and what this file is for:
# I chose these columns to organise student information.
# With 200 records, the file could help manage student contacts
# and organise communication for academic activities.


# Your code below
# First-time file behaviour:
# If student_records.csv does not exist, create it and write the column headers once.

# Invalid input behaviour:
# If a required field is empty or the study year is not a number,
# ask the user to enter the information again.

import csv
import os

filename = "student_records.csv"

fieldnames = ["first_name", "last_name", "email", "programme", "year_of_study"]

# Create the CSV file with headers if it does not exist.
if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

print("Student records file is ready.")

# Collect student information
while True:
    first_name = input("Enter first name: ").strip()
    if first_name:
        break
    print("First name cannot be empty.")

while True:
    last_name = input("Enter last name: ").strip()
    if last_name:
        break
    print("Last name cannot be empty.")

while True:
    email = input("Enter email: ").strip()
    if email:
        break
    print("Email cannot be empty.")

while True:
    programme = input("Enter programme: ").strip()
    if programme:
        break
    print("Programme cannot be empty.")

while True:
    try:
        year_of_study = int(input("Enter year of study: "))
        if year_of_study > 0:
            break
        print("Enter a positive number.")
    except ValueError:
        print("Please enter a number.")

# Save the student details in the CSV file
with open(filename, "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writerow({
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "programme": programme,
        "year_of_study": year_of_study
    })

print("Student information saved successfully.")