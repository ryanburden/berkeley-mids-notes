Random Variables

What is a random variable?
- Intiution: 
    - A model for where the numbers in data come from
    - Like a regular variable but with uncertainty about its value

-Definition:
- Given a probability space, a random variable is a measurable function from $\Omega$ to $\Reals$
- A random variable is really not random or a variable, its a function. We can still think of a random variable as a variable that takes on a value determiend by a random generative process.
- When the state of the world is $\omega$, the random variable takes on the value $X(\omega)$. 
- $X is understood to be X(\omega)$
- The event {X=1} should be understood to mean the set of states omega within w such that X(w)=1.
Functions, Events, and Operators

Functions of a random variable:
A function of a random variable is a random variable

Events from a random variable:
- You want to know whether the temperature is below 150. $T<150$ represents an event in the sample space $\Omega$

Operators applied to random variables
- You want to find the minimum possible temperature
- min[T] is an operator
- it takes as an input any random variable, and outputs a number.

Discrete Random Variables
- A random variable X is discrete if its range is a countable set
    - a countable set can be finite or countably infinite

The Bernoulli Distribution
    - A Bernoulli trial is a simple discrete random variable
    - It can represent a coinflip, a decision to buy or not to buy, a success or failure of experiment
    - Convention: 1 represents success, 0 failure

Probability Mass Function
- A function that gives the probability that a discrete random variable equals each number in R
- f(x) = P(X=x)

Cumulative Distribution Function
- Given random variable X
F:R->R F(x) = P(X<=x)
- cdf F is non-decreasing

Continuous Random Variables