"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In: A list of procurement budgets in euros.
# 2. Process: The function adds all the budget amounts together.
# 3. Out: The total procurement budget as a number.
# 4. My function is called calculate_total_budget because
# its name clearly explains its purpose.
# I use return because it gives the result back so I can
# reuse it in other calculations. Print only displays it.


# Your code below
# Create the procurement budget list from Exercise 4.0
procurement_budgets = [1200, 850, 1500, 950, 1100, 700, 1350, 1000]

# This function calculates and returns the total budget.
def calculate_total_budget(budgets):
    total = sum(budgets)
    return total


# Call the function three times with different inputs.
total_all = calculate_total_budget(procurement_budgets)
total_first_three = calculate_total_budget(procurement_budgets[:3])
total_last_three = calculate_total_budget(procurement_budgets[-3:])

# Display the three results.
print("Total of all budgets:", total_all)
print("Total of first three budgets:", total_first_three)
print("Total of last three budgets:", total_last_three)

# Test the function with an empty list.
empty_total = calculate_total_budget([])

# An empty list returns 0, which is acceptable because
# there are no budget amounts to add.
print("Total of an empty list:", empty_total)