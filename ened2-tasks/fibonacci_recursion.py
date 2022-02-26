#Fibonacci sequence (recursion)

#list
nlist = []               #fibonacci values

#input
n = int(input("\n\nn =  "))             #user input for n

#recursive function
def fib (n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))


#output
print("\n\nFibonacci sequence:")
for i in range(n+1):
    nlist.append(fib(i))            #add val to list
    print(fib(i))                   #print val

print(nlist)    #print list
