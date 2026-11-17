"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - Capitalisation is inconsistent.
# - There is an empty line.
# - Some names have leading spaces.
# - First and last names use inconsistent formatting.

# 1. In: The names.txt file containing names.
# 2. Process: Remove empty lines and extra spaces, standardise names, and sort them by last name.
# 3. Out: A new file containing the cleaned and sorted names.
# 4. How I decide which word is the last name: I use the final word in each person's name.


# Your code below
# Read the original names file and clean each name.
input_file = "names.txt"
output_file = "cleaned_names.txt"

try:
    with open(input_file, "r", encoding="utf-8") as file:
        names = file.readlines()

    # Remove empty lines, extra spaces and standardise capitalisation.
    cleaned_names = []

    for name in names:
        name = " ".join(name.split())

        if name:
            cleaned_names.append(name.title())

    # Sort the names alphabetically by the last word.
    cleaned_names.sort(key=lambda name: name.split()[-1].lower())

    # Save the cleaned names in a new file.
    with open(output_file, "w", encoding="utf-8") as file:
        for name in cleaned_names:
            file.write(name + "\n")

    print("Names cleaned and sorted successfully!")
    print("Original names:", len(names))
    print("Cleaned names:", len(cleaned_names))
    print("Output saved in:", output_file)

except FileNotFoundError:
    print("Error: names.txt was not found.")