#calculates the factorial of the inputted number

#input
num = int(input("number:  "))

#set variable
fac = 1

#for loop/calculate
for i in range (1,num+1):
    fac=fac*i

#output
print(fac)
