#fibonacci sequence - remove values greater than input
import sys

#list
nlist = [0,1]       #origional list
uplist = []         #updated list

#input
x = int(input("x =  "))             #user input for x

#function
def fib (x):                  #define the function that recurs
    if x > 0:
        y = x + fib(x-1)      #recursion happens in + recursion(x-1)
        nlist.append(y)
    else:
        y = 0
    return y

fib(x)

#fix list
lenl = len(nlist)
for i in range(lenl):     #iterate thru list and remove values greater than input
    nl = nlist[i]
    if nl <= x:
      uplist.append(nlist[i])  
    else:
        pass

#output
print(uplist)
