#fibonacci sequence
import sys

#list
nlist = [0,1]

#input
x = int(input("x =  "))             #user input for x
x = x - 2

#function
def fib (x):                  #define the function that recurs
   if x > 0:
        y = x + fib(x-1)      #recursion happens in + recursion(x-1)
        nlist.append(y)
   else:
        y = 0
   return y

fib(x)

#output
print(nlist)
