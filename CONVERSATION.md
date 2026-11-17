# Conversation with the AI

Written automatically by `tutor.py`. Add your own notes under any entry: what you tried, what broke, what you changed. Those notes are what is graded.

---
## 2026-11-11 13:40, in .

**Me:** Can you explain what a Python variable is with a simple example?

**Tutor:**

A variable is a name that refers to a value you can use and change later.

```python
# TODO: assign the string "hello" to a variable named greeting
greeting = "hello"

# TODO: assign the integer 42 to a variable named answer
answer = 42

# TODO: print both variables
print(greeting)
print(answer)
```

Which function prints a variable’s value?

---
## 2026-11-11 13:43, in .

**Me:** print()

**Tutor:**

Printing a variable’s value uses the built-in function `print()`.

```python
greeting = "hello"
answer = 42

# TODO: print both variables on separate lines
print(greeting)
print(answer)
```

Which argument does `print()` expect?

---
## 2026-11-11 13:47, in .

**Me:** A value or variable to display.

**Tutor:**

A variable can hold any data type; the value it refers to can be printed.

```python
# TODO: assign the string "hello" to a variable named greeting
greeting = "hello"

# TODO: assign the integer 42 to a variable named answer
answer = 42

# TODO: print both variables on separate lines
print(greeting)
print(answer)
```

What type does the variable `greeting` have?

---
## 2026-11-11 13:49, in .

**Me:** String (str), because hello is text.

**Tutor:**

A variable’s type is determined by the value it currently holds.

```python
# TODO: assign the string "hello" to a variable named greeting
greeting = "hello"

# TODO: assign the integer 42 to a variable named answer
answer = 42

# TODO: print the type of each variable
print(type(greeting))
print(type(answer))
```

Which function returns the type of a variable?

I learned what Python variables are and how to assign values.

I learned that "hello" is a string and 42 is an integer.

I learned how to use print() and type() in Python.

I also learned how to interact with the Python tutor.

---

Assignment 6.1 – Small Functions Working Together

Me: I need help understanding Exercise 6.1. The assignment asks me to create three small functions and one summary function using procurement budget data. Can you explain the task step by step?

Tutor: Certainly. The objective is to divide the program into small functions, with each function performing one specific task. You will create:

1. calculate_total() to calculate the total budget.
2. calculate_average() to calculate the average budget.
3. find_highest() to find the highest budget.
4. budget_summary() to call the first three functions and return a summary.

Me: Why do we need separate functions instead of writing everything in one block of code?

Tutor: Separate functions make the program easier to understand, test, reuse and maintain. If one calculation has an error, you can check that function independently.

Me: What should the functions return?

Tutor: The first three functions should return their calculated values. The fourth function should return all three results together as a tuple.

Me: How can I test whether my functions are working correctly?

Tutor: Use a list of procurement budgets and compare the program’s output with the expected results. Test each function separately before testing the summary function.

Me: I ran my program. These are the results:

* Total: 8650
* Average: 1081.25
* Highest: 1500
* Budget summary: (8650, 1081.25, 1500)

Are these results correct?

Tutor: Yes. These results are consistent with the expected calculations shown in your assignment tests.

Me: What did I learn from this exercise?

Tutor: You practised creating functions, passing data as arguments, returning values, combining functions and using a tuple to return multiple results.

My reflection: I learned that breaking a program into smaller functions makes the code easier to understand and test. I also improved my understanding of return statements, function calls and tuples in Python.

2026-11-17 – Assignment 7.0: Standard I/O and File Output

What I did:

* Created a Python program to collect student information.
* Asked for first name, last name, email, programme and year of study.
* Used CSV file handling to save the information in student_records.csv.
* Ran the program successfully and checked the saved output.

Result: Student information saved successfully.

2026-11-17 – Assignment 7.1: File Processing

What I did:

* Inspected names.txt and identified formatting issues.
* Cleaned extra spaces and standardised names.
* Sorted the names by last name.
* Saved the cleaned results in cleaned_names.txt.

Testing result:

* Original names: 10
* Cleaned names: 8
* Output file: cleaned_names.txt
* The program ran successfully.

My reflection: I learned how to read a text file, clean and standardise data, sort names, and save the results in a new file without modifying the original file.