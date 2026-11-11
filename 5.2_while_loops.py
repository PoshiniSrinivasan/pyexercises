"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user enters a shipment confirmation answer (yes or no).
# 2. Process: The program checks the answer and counts each attempt.
# 3. Out: A message showing whether the shipment is confirmed.
# 4. My stop condition, my attempt limit, my summary:
# The loop stops when the user enters yes or after 5 attempts.
# The summary contains the number of attempts and confirmation status.


# Your code below
attempt_limit = 5
attempts = 0
confirmed = False

while attempts < attempt_limit and not confirmed:

    answer = input("Is the shipment confirmed? (yes/no): ").strip().lower()
    attempts += 1

    if answer == "yes":
        confirmed = True
        print("Shipment confirmed successfully!")

    else:
        print("Shipment is not confirmed. Try again.")

print("\nShipment confirmation summary:")
print("Total attempts:", attempts)

if confirmed:
    print("Status: Confirmed")
else:
    print("Status: Not confirmed")