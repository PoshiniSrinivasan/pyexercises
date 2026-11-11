"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user enters a product name and a quantity.
# 2. Process: Python collects the two inputs and converts the quantity into an integer.
# 3. Out: The program displays a sentence showing the product name and quantity.
# 4. My two fields are product name and quantity. I would use them in a supply chain order form to record customer orders.


# Your code below
# Ask the user for a product name and quantity
product_name = input("Enter product name: ")
quantity = int(input("Enter quantity: "))

# Display the order details
print(f"You ordered {quantity} units of {product_name}.")

# Add 1 to the quantity
print("Updated quantity:", quantity + 1)