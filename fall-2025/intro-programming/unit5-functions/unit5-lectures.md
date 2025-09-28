Unit 5: Functions

Function: piece of code to reuse in a project
- 1. Define the function
- 2. Call the function

Functions and the Call Stack

- Object that keeps track of where control is supposed to go
- Ex:

- In Main at line 25
- In geometric_mean at Line 12
- In sqrt at Line 8

- In stacks, you can only add one item to the top of the stack, or remove one item from the top of the stack

The Stack Trace
- shows you the call/execution stack and goes through it

Value of functions
- Decomposition
- Modularity
    - flexible, reusable, readable
- Abstraction
    - hide implementation details
    - create layers for low-level and high-level tasks

Namespaces
- Local / Global namespaces
- Local variable changes do not affect global variables
- Local namespaces are made when functions are executed

Accessing Global Variables
- Global variables are accessible from within functions
- Steps in running a function
    - Create a new local namespace
    - For each parameter, create a new local variable and bind it to the argument
    - For each assignment statement, if name is not local namespace, create a new local variable
    - Execute the statements

Recursion
- Two elements for a recursive algo:
    - 1. base case
    - 2. recursive rule

