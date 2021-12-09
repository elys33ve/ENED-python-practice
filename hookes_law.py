#calculates the distance a spring is compressed/stretched (x) and the force (f) of two springs
#either in a series or parallel; using Hooke's Law and the inputs for spring type, spring constants
#and total force

#lists for inputs
series = ['series','s']
parallel = ['parallel','p']

#inputs
spring_type = input("are the springs in a series or parallel?  ")
cons1 = float(input("spring 1 constant:  "))
cons2 = float(input("spring 2 constant: "))
total = float(input("total force of spring 1:  "))

#test inputs
if cons1 < 0 or cons2 < 0 or total < 0:
    print("invalid input(s).")
else:
    pass

#calculations
if spring_type in parallel:           #calculate for parallel
    Keq = cons1+cons2
    x = Keq/total
    x1 = x
    x2 = x
    f1 = cons1*x
    f2 = cons2*x
elif spring_type in series:           #calculate for series
    Keq = 1/(1/cons1 + 1/cons2)
    f1 = total
    f2 = total
    x1 = total/cons1
    x2 = total/cons2
    x = x1 + x2
else:
    print("invalid input for spring type.")

#outputs
print(f"x1: {x1:.2f}m\nx2: {x2:.2f}m\nx: {x:.2f}N\nF1: {f1:.2f}N\nF2: {f2:.2f}N\n")

