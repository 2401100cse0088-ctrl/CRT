'''
Debugging:
Bug is an error in a program that prevents it from running as expected.
Finding and fixing bugs is called debugging.
Types of errors:
1. Syntax Errors: Mistakes in the code that violate the rules of the programming language.
ex)Missing colon, misspelled keywords, missing of indentation etc.
2. Runtime Errors: Errors that occur while the program is running, often due to invalid operations
ex) Division by zero, accessing invalid index in a list etc.
3. Logical Errors: Errors in the program's logic that lead to incorrect results.
ex) Using wrong formula, incorrect conditions in loops or if statements etc.
Debugging Techniques:
1. Print Statements: Inserting print statements at various points in the code to check the values of variables and the flow of execution.
ex) print("Value of x:", x)
2. Try-Except Blocks: Using try-except blocks to catch and handle exceptions gracefully.
ex)try:
    a=int(input("Enter a number: "))
    print(10/a)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
3. Using pdb Module: Python's built-in debugger module that allows you to set breakpoints, step through code, and inspect variables.
Python Debugger:
   Main purpose is:
   1)To pause the execution of code at certain points (breakpoints).
   2)To run the code line by line (step execution).
   3)To inspect the values of variables at different stages of execution.
Pdb Commands:
    - n (next): Execute the next line of code.
    - c (continue): Continue execution until the next breakpoint.
    - q (quit): Exit the debugger and terminate the program.
    - p (print): Print the value of a variable.
    - l (list): Display the current location in the code.
    - s (step): Step into a function call.
    - r (return): Continue execution until the current function returns.
    - help: Display a list of available commands or get help for a specific command.
Example of using pdb:
import pdb
def add(a, b):
    pdb.set_trace()  # Set a breakpoint here
    return a + b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Sum:", add(a, b))

'''