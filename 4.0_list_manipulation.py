"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of eight procurement budgets in euros.
# 2. Process: The program displays the list, selects one budget, sorts the list and calculates the total.
# 3. Out: The original list, selected budget, sorted list and total budget.
# 4. My list is about supply chain procurement budgets. I calculated the total spending to understand the overall procurement cost.


# Your code below
# Create a list of eight procurement budgets
procurement_budgets = [1200, 850, 1500, 950, 1100, 700, 1350, 1000]

# Display the original list
print("Original list:", procurement_budgets)

# Select and display the third budget
print("Selected budget:", procurement_budgets[2])

# Display the list in ascending order
print("Sorted list:", sorted(procurement_budgets))

# Calculate and display the total budget
total_budget = sum(procurement_budgets)
print("Total budget:", total_budget)