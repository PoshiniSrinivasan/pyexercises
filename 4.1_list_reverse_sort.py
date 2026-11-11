"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The original list of eight procurement budgets in euros.
# 2. Process: The program creates different reordered versions of the list.
# 3. Out: Four reordered lists and the original list at the end.
# 4. My four orders: Ascending, descending, reversed and reverse sorted.
# sorted() and reversed() create new results, while sort() and reverse() modify a list.


# Your code below
# Create the original list from exercise 4.0
procurement_budgets = [1200, 850, 1500, 950, 1100, 700, 1350, 1000]

# Display the original list
print("Original list:", procurement_budgets)

# 1. Display the list in ascending order
print("Ascending order:", sorted(procurement_budgets))

# 2. Display the list in descending order
print("Descending order:", sorted(procurement_budgets, reverse=True))

# 3. Display the list in reversed order
print("Reversed order:", list(reversed(procurement_budgets)))

# 4. Reverse a copy of the original list
reversed_list = procurement_budgets.copy()
reversed_list.reverse()
print("Reverse using reverse():", reversed_list)

# Check that the original list has not changed
print("Original list at the end:", procurement_budgets)