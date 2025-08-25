"""Write a script that prompts the user for their phone number, x. Then carry out the following steps:
 
1. Compute x minus the sum of the digits of x. Call this result y. (hint: to find the sum of the digits of x, check to see what x//10 and x%10 give you)
2. Compute the sum of the digits of y, and store the result back in y.
3. Repeat step 2 until y has just one digit, then display it."""

def sum_dig(x):
  sum = 0
  while x > 0:

    sum += x % 10
    x = x // 10

  return sum

x = int(input("enter your 10-digit telephone number: "))

y = x - sum_dig(x)

while y >= 10:
  y = sum_dig(y)

print(y)