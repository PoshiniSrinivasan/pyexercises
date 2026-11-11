"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user enters two numbers.
# 2. Process: Python performs four arithmetic operations.
# 3. Out: The program displays the calculation results.
# 4. If the second number is zero, display a message instead of dividing by zero.


# Your code below
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Addition
print("Addition:", first_number + second_number)

# Subtraction
print("Subtraction:", first_number - second_number)

# Multiplication
print("Multiplication:", first_number * second_number)

# Division
if second_number == 0:
    print("Cannot divide by zero.")
else:
    print("Division:", first_number / second_number)

    # Check it yourself:
# I tested the program with 7 and 2.
# The division result was 3.5, which is correct.
# I also tested 7 and 0.
# The program displayed "Cannot divide by zero."
# Both tests worked correctly.