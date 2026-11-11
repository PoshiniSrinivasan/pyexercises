"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user enters a positive whole number N.
# 2. Process: The program checks every number from 1 to N using % 2.
# 3. Out: The program displays whether each number is odd or even.
# 4. If N is 0 or negative, display a message. If N is very large, limit it to 1000.


# Your code below
n = int(input("Enter a positive number: "))

if n <= 0:
    print("Please enter a positive number.")
elif n > 1000:
    print("Please enter a number less than or equal to 1000.")
else:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, "is Even")
        else:
            print(i, "is Odd")