1.3 History of Computation

In the 1600's, ocean-going ships used logarithms for navigation. These logarithms
turned multiplication into addition, speeding up computations.

Computers started off as humans. Then it was mechanized and automated by the Difference Engine by Charles Babbage.

What are the different logical layers of a computer?
1. Hardware
2. Operating System: coordinates use of the hardware
3. Applications
4. Users: could be people or other computers

1.4 Hardware and Data Representation

A bit is a binary digit, {0,1}. Byte is 8 bits. It is our usual basic unit of storage in a computer. Kilobyte is $2^{10}$ bytes. Megabyte is $2^{20}$ bytes.

Different encodings are used to store other types of data as bytes. For example, ASCII and UTF-8 for text encoding.

1.5 Python as a Programming Language

CPU can be seen as an arithmetic logic unit. Computers deploy layers of abstraction to hide the complexity of low-level computer functions.

A program is a sequence of instructions to manipulate digital objects. Digital objects = data, numbers, text, etc represented by the object space.

What instructions make up a programming language?
1. Syntax
2. Semantics - What the instructions mean

Then, what is Python? Python is an interpreted, high-level programming language. 

In an interpeted language, you are using source code. This is the human-readable language. The source code then goes into a checker (syntax/form check). The source code then passes on to an interpreter, which is the part of Python that actually executes the instructions and generates output.

A compiled language is a little different. We also start with source code, but this time the source code goes into a compiler which translates the source code into object code. Object code is closer to machine-level instructions. These languages are faster and more efficient.

A high-level language is a language that tries to hide the interior details of the computer. It includes a lot of user-facing optimizations such as garbage collection. Python is a high-level language, it has somewhat worse performance then C or Java. It purposely hides many of the lower-level data structures.

1.6 Memory: Objects and Indirection 

Everything in Python is an object- even the code itself!
Every object has a type/class. This type tells you what type of data the object is storing. Python is a "strongly typed" language, meaning that what you can do with different objects is constrained by its type.

Two main types: Scalar, Non-scalar (composite)

Integer
Floats. Floats are an approximation of a real number up to 16 decimal places.
Boolean
String
Fraction. Create rational numbers with perfect precision
List
Set. Collection with no particular order.
Dict

Variables/Names are used to access objects. Name space connects to object space in memory.

Names dont have types. Names could be reassigned to different objects. This is reffered to as "Dynamic Typing". Python is a dynamically typed language, meaning that the types associated with each name are determined at runtime.

New definition of Python, given this information: Python is a high-level, interpreted, strongly typed, dynamically typed programming language.