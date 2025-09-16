Sequences

- Strings are sequence type
    - ie: list("hello") = ['h','e','l','l','o']

- Lists
    - mutable data type
    - objects can be reached in multiple ways
    - mutating an object affects all variables with paths to tht object
    - .copy() method only creates a shallow copy of a list. References of nested lists are unchanged.
    - from copy import deepcopy

    - a list is not like a box containing objects. it holds references to objects in the object space.