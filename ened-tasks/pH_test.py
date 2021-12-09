#tests the acidity/basicity of a solution based on the inputted value for pH

u = 'hi'

#test solution
while u != 'exit' and u != 'quit':
    u = input("pH of solution:  ")
    user = float(u)
    if user in range (0,7):
        print("Acidic")
    elif user == 7:
        print("Neutral")
    elif user in range (8,14):
        print("Basic")
    else:
        print("Invalid input")
