"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of procurement budgets in euros.
#
# 2. Process, function by function:
# calculate_total adds all the budgets.
# calculate_average calculates the average budget.
# find_highest finds the largest budget.
# budget_summary uses these three functions to create a summary.
#
# 3. Out: The total, average and highest procurement budget.
#
# 4. The fourth function answers:
# What is the overall summary of our procurement budgets?
# Three small functions make it easier to test each calculation separately.

# Your code below
# Original procurement budget list from Exercise 4.0
procurement_budgets = [1200, 850, 1500, 950, 1100, 700, 1350, 1000]


# Function 1: Calculate the total of all budgets.
def calculate_total(budgets):
    return sum(budgets)


# Function 2: Calculate the average budget.
def calculate_average(budgets):
    if len(budgets) == 0:
        return 0
    return calculate_total(budgets) / len(budgets)


# Function 3: Find the highest budget.
def find_highest(budgets):
    if len(budgets) == 0:
        return 0
    return max(budgets)


# Function 4: Use the three small functions to create a summary.
def budget_summary(budgets):
    total = calculate_total(budgets)
    average = calculate_average(budgets)
    highest = find_highest(budgets)

    return total, average, highest


# Test function 1 separately: expected total is 8650.
print("Test total:", calculate_total(procurement_budgets))

# Test function 2 separately: expected average is 1081.25.
print("Test average:", calculate_average(procurement_budgets))

# Test function 3 separately: expected highest is 1500.
print("Test highest:", find_highest(procurement_budgets))

# Test the fourth function: expected summary is (8650, 1081.25, 1500).
print("Budget summary:", budget_summary(procurement_budgets))