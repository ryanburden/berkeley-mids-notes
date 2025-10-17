Big-0
- computer scientists count steps to assess runtime     
- the number of steps is a function of the input size n
- comparing growth rates can be hard

Rule 1: Delete Lower-Order Terms
- Which term is most important?
    - 2n^2 + n + 100
    - 2n^2 is much more important, you can ignore the other terms.

Rule 2: Delete Constant Factors
    - how important is the 2 in front of 2n^2?
    - not very
    - some computers are twice as fast as others
    - some elementary steps take twice as long as others
    - there are techniques to reduce the 2

Rule 3: What about logs?
- 2n^2 + nlog10(n)
- log10(n) grows, but slowly, especially compared to n^2.
- n^2 -> nlog(n) -> n -> log(n) -> 1

Rule 4: Don't Worry About the Base of Logs

Bisection Search:
- growth rate is 0(log2n)

Big-O:
- Big O is an upper bound
- Big-Omega is a lower bound
- if f is O(g) and Omega(g), then f is 0(g)
- Theta is exact long term growth rate of algorithm

- Modules: single python file that contains vars, functions, classes that you can import and use
- Packages: directories that contain a collection of modules