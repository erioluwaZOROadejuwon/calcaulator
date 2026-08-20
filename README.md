## BASIC CALCULATOR
    A command line calculator that lets user calculate the addition, subtraction, multiplication and division between two numbers. You input the two numbers and pick the operator you want to use and perform the calculation.
## Features
- Enter the two numbers i.e the first and the second number
- Menu-driven commands:
- CALC — perform a calculation
- C — clear
- OFF — exit the program
- Supports all four basic operations: +, -, *, /
- Handles divide-by-zero without crashing
- Validates number input using try/except — won't crash if you type letters instead of numbers
- Catches invalid operation symbols and invalid commands gracefully
## How to run
- Type CALC to start a calculation
- Enter your first and second numbers
- Choose an operation: +, -, *, or /
- See your result
- Type CALC again for another calculation, or OFF to exit
## What I learned
- Using a while True loop with a command menu to control program flow
- Handling divide-by-zero with a conditional check before dividing
- Using try/except to catch invalid number input (ValueError) instead of crashing
- Why continue is necessary after catching an exception — without it, the program tries to keep running with variables that were never successfully created, causing a second error (NameError)

## Tech stack
Python 3, standard library only

## Possible improvements
- Make the C (clear) command actually reset a stored/running result
- Support chaining calculations (using the previous result as the next input)
- working with more than three numbers all at once
- Add more operations (exponents, modulo, etc.)

