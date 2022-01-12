#ACT_Python_5p1


#input lists
unitsl = ['pa','psi']       #allowed units list

#inputs
press = float(input("pressure: "))          #pressure (numerical value)
units = input("units of entered value: ")   #entered units for pressure
dunits = input("desired units: ")           #desired units

units = units.lower()           #make lowercase to test
dunits = dunits.lower()

#test input validity                            (while loops for multi attemps)
while units not in unitsl:          #test units
    print("please enter pressure units in Pa or psi.\n")
    units = input("units: ")
    units = units.lower()

while dunits not in unitsl:
    print("please enter desired pressure units in Pa or psi.\n")
    dunits = input("desired units: ")
    dunits = dunits.lower()

while dunits == units:
    print("please enter different desired units. rn they match current units")
    dunits = input("desired units: ")
    dunits = dunits.lower()
        
#math
if units == 'psi':
    press2 = press * 6894.76     #psi to pa
elif units == 'pa':
    press2 = press / 6894.76     #pa to psi
else:
    print("how tf")         #dont think this should happen

#output
if units == 'pa':               #capitalize pa to Pa
    units = units.title()
else:
    dunits = dunits.title()
    
print(f"{press} {units} in {dunits} is: {press2:.3f}")
