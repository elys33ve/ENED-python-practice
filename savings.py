#calculates the amount of money saved after inputted value of years, if each day, one cent is added to the 
#previous day's amount that was put into savings

#input
Y = int(input('Please enter the number of years: '))

#set variables
Savings = 0
D = 1

#loop/calcuations
for D in range(Y*365):
    Savings = Savings + (D+1)
    
#output
print('Amount Saved: ${0:0.2f}'.format(Savings/100))
