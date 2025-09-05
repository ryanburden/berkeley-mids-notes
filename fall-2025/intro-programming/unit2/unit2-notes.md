Unit 2: Starting Python

Algorithm vs Program

- Algorithm: The sequence of steps to solve a program
    - Abstract
    - Not tied to a language

- Program: a sequence of commands in a computer language
    - precise syntax
    - implements an algorithm

High-level vs Low-level languages

- High-level 
    - abstract away computer details (memory, hardware etc)
    - close to human language
    - fast development 
    - R, Perl, Ruby, Python (java is lower on spectrum)

- Low-level
    - offer control over memory allocation, CPU operations, etc
    - hard to read by humans
    - fast execution
    - Machine code, assembly language (c, c++ is higher on spectrum)

Interpreted vs Compiled Languages

- Interpreted
    - source code -> interpreter -> output

- Compiled (Java, C, etc.)
    - source code -> compiler -> object/machine code -> machine/virtual machine -> output

Objects

- Everything in python is an object
- An object is a container for data
- Why is this important?
    - At low level, all data is stored as ones and zeros.
    - Data for different objects are kept separate.
    - Even code is held in objects
    - Types: int, string, function, file
- Python is strongly typed
    - python will restrict the operations you can perform based on the object's type

Representing Numbers

- int
    - can be positive or negative
    - no limit to how large the number can be
- float
    - float records to 16 decimal places. lost digits are called rounding error

Control/Flow Control
- "Control" where in the program that execution is happening

- Conditionals: if, elif, else

- Loops: while, for

