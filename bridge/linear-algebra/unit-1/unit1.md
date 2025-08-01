1.1 Intro

This unit is about linear functions. We will start by defining a function.

1.2 What is a function?

Def. A function $f$ is a rule that assigns to each input $x$ in its domain an output $f(x)$ in its codomain

Terms:\
    - Domain = Set of all inputs\
    - Codomain = Superset of all outputs\
    - Range = Set of all outputs

Notation:\
$f:\Reals^n \to \Reals^m$ means..\
$\Reals^n$ = Domain of $f$\
$\Reals^m$ Codomain of $f$

Note: the codomain is the set of all possible output values, while the range is the subset of the codomain that contains only the actual output values produced by the function for a given domain

Formal definition: A function is a triple $<f, D, C>$ where $D$ is the domain, $C$ is to codomain, and $f$ is a subset of $D$ cross $C$ satisfying the function property

Representing Functions:\
formulas\
$f(x) = x^2$\
$y = x^2$\
$x \to x^2$\
$x^2$\
$\cdot^2$\
^2

sets\
${(x,y): y = x^2}$

graphs..

1.3 What is a linear function?

Single variable calculus.\
a linear function has the form $y=mx+b$

another property of "linear" functions\
line segments map proportionally to line segments

Now, we want to generalize this form to more dimensions\
Def: A function $f: \Reals^n -> \Reals^m$ is called affine if for every $u,v$ in $\Reals^n$ and for every $t \in [0,1]$
 $f((1-t)u + tv) = (1-t)f(u) + tf(v)$

Def: A function $f:\Reals^n \to \Reals^m$ is called linear if $f(u+v) = f(u)+f(v)$ and $f(au) = af(u)$ for every $u,v$ $\in$ $\Reals^n$ and for every $a$ $\in$ $\Reals$

Exercise $f$ is linear if and only if $f$ is affine and $f(0) = 0$

1.4 Affine Functions as Linear Functions

Linear algebra focuses on linear functions. It preserves addition and multiplication by real numbers. We can use linear algebra to study affine functions.

1) If $g:\Reals^n->\Reals^m$ is a fixed affine function, then $g(x) - g(o)$ is a linear function.\
We can apply linear algebra theorems to $g(x) - g(o)$ and add back $g(o)$

2) For the class of affine functions from $\Reals^{n} \to \Reals^m$\
This class is isomorphic to the class of linear functions from $\Reals^{n+1} \to \Reals^m$

1.5 Operations on Real Matrices

Def: A real matrix is an $n$ x $m$ rectangular array of real numbers. Capital $A$ represent a matrix, lower case $a$ is the entry, and you include the ranges of the subscripts, $i$ and $j$. Each $a_{ij}$ is an entry of $A$ representing the number in the $i^{th}$ row and $j^{th}$ column 

Primary operations on real matrices:
- matrix addition: add each element component-wise to form new matrix. Note: you cannot add matrices of different dimensions\
- matrix scalar multiplication: example: $2 \cdot A$

1.6 Summations and Applications

Summation\
$	\displaystyle\sum_{k=m}^{n+1}a_k = 	\displaystyle\sum_{k=m}^{n}a_k + a_{n+1}$ 

Inner product\
$<u,v>$ = $\displaystyle\sum_{k=1}^{n}u_k{\cdot}v_k$

Vector Components\
For $i=1, ..., n$ define $e_i$ = the vector in $\Reals^n$ with $1$ in the $i^{th}$ position and $0$ elsewhere.

For any $x\in \Reals^n$ we can write $\overline{x}=\displaystyle\sum_{k=1}^{n}x_k\cdot\overline{e_k}$

Rule: $x_k = <x,e_k>$

1.7 Vectors as Single-Valued Linear Functions

Theorem: Every linear function $f:\Reals^n\in\Reals$ can be uniquely represented as $f(u)=<a,u>$ for some $a \in \Reals$

1.8 Operations on Real Vectors

Def: A real vector is an ordered list of real numbers.\
eg: 
$
\begin{pmatrix}
   2 \\
   3 \\
   \pi \\
   2.5
\end{pmatrix} \in \Reals^4$

Primary operations on real vectors

Vector additon\
Scalar multiplication\
Inner Product\
Note: In linear algebra, we don't define vector multiplication

1.9 The Matrix Vector Product

If $A \in \Reals^{m x n} $ and $v \in \Reals^n$\
Define $Av$ to be the vector in $\Reals^m$: $\displaystyle\sum_{i=1}^{m}\displaystyle\sum_{j=1}^{n}a_{ij}v_j\overline{e_i}$

1.10 Matrices as Linear Functions

Theorem: If $f: \Reals^n \to \Reals^m$ is a linear function then $f$ is uniquely represented by a matrix $A \in \Reals^{m x n}$ such that $f(x) = Ax$ for every $x \in \Reals^n$

1.11 Composition of Linear Functions

Suppose $f:\Reals^n\to\Reals^m$ and $g:\Reals^p\to\Reals^n$\
Then the composition $(f\circ g):\Reals^p\to\Reals^m$ is defined by $(f\circ g)(u) = f(g(u))$\
$(f\circ g)$ is linear. 

Since $f\circ g$ is linear, it is uniquely represented by a matrix $C \in \Reals^{m x p}$

1.12 The Matrix Product

For $A \in \Reals^{mxn}$ and $B \in \Reals^{nxp}$\
$A$ represents a liner function $f:\Reals^n\to \Reals^m$
$B$ represents a liner function $f:\Reals^p\to \Reals^n$

Define the matrix product $AB$ to be the matrix $C$ representing $f\circ g:\Reals^p\to\Reals^m$

In practice:\
$A_i =$ the $i^{th}$ row of $A$
$B_k =$ the $k^{th}$ row of $B$

Then $c_{ik}$ = $<A_i, B_k>$