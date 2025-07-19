1.1 Intro

This unit is about linear functions. We will start by defining a function.

1.2 What is a function?

Def. A function f is a rule that assigns to each input x in its domain an output f(x) in its codomain

Terms:\
    - Domain = Set of all inputs\
    - Codomain = Superset of all outputs\
    - Range = Set of all outputs\

Notation:\
$f:R^n -> R^m$ means..\
$R^n$ = Domain of f\
$R^m$ Codomain of f

Note: the codomain is the set of all possible output values, while the range is the subset of the codomain that contains only the actual output values produced by the function for a given domain

Formal definition: A function is a triple <f, D, C> where D is the domain, C is to codomain, and f is a subset of D cross C satisfying the function property

Representing Functions:\
formulas\
$f(x) = x^2$\
$y = x^2$\
$x -> x^2$\
$x^2$\
$(.)^2$\
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
Def: A function $f: R^n -> R^m$ is called affine if for every $u,v in R^n$ and for every $t in [0,1]$
 $f((1-t)u + tv) = (1-t)f(u) + tf(v)$

Def: A function $f:R^n -> R^m$ is called linear if $f(u+v) = f(u)+f(v)$ and $f(au) = af(u)$ for every $u,v in R^n$ and for every $a in R$

Exercise f is linear if and only if f is affine and f(0) = 0

1.4 Affine Functions as Linear Functions

Linear algebra focuses on linear functions. It preserves addition and multiplication by real numbers. We can use linear algebra to study affine functions.

1) If $g:R^n->R^m$ is a fixed affine function, then $g(x) - g(o)$ is a linear function.\
We can apply linear algebra theorems to $g(x) - g(o)$ and add back $g(o)$

2) For the class of affine functions from $R^n -> R^m$\
This class is isomorphic to the class of linear functions from $R^(n+1) -> R^m$