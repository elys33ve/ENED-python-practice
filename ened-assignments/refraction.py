# Description:
# This python script opens a file (Refraction.txt), adding each line to a list
# before separating each item and adding the values to their respective lists
# (n1, theta1, n2). It then loops though the lists, calculating the theta 2
# value for each row, adding to the theta 2 list. Lastly, it creates/overwrites
# a file (HW_2p1_Task2.txt), creating strings of each row of values and writing
# them to the file, after the first line with the column headers (n1, theta1,
# n2, theta2)

import math as m

#OPEN FILE
r = open("Refraction.txt", "r")         #open file for read
#(^ file with column headers on 1st line, and 3 columns of values)
w = open("HW_2p1_Task2.txt", "w")       #create/write to file

#CREATE LIST
l = []              #list of each row of values

for line in r:
    l.append(line.strip())

del l[0]                    #delete column headers

r.close()   #close read file

#SEPARATE VALUES/CREATE COLUMN LISTS
l_len = len(l)          #length of list/number of rows
n1 = []             #n1 values
theta1 = []         #theta1 values
n2 = []             #n2 values

for i in range(l_len):
    x = l[i].split(" ")     #split item into list at space 
    for ii in range(len(x)):
        while '' in x:      #remove black items
            x.remove('')
        if ii == 0:
            n1.append(x[ii])        #add 1st item to n1
        if ii == 1:
            theta1.append(x[ii])    #add 2nd item to theta1
        if ii == 2:
            n2.append(x[ii])        #add 3rd item to n2

for i in range(len(l)):     #convert items to float
    n1[i] = float(n1[i])
    theta1[i] = float(theta1[i])
    n2[i] = float(n2[i])
    
#CALCULATE THETA 2   -->   (n1*sin(theta1)=n2*sin(theta2))
theta2 = []         #theta2 values

for i in range(len(l)):
    t1 = m.radians(theta1[i])       #convert theta 1 to rad
    t2 = m.asin((n1[i] * m.sin(t1)) / n2[i])    #math shits
    t2 = m.degrees(t2)              #convert theta 2 to deg
    t2 = f"{t2:.1f}"
    theta2.append(t2)       #add values to theta 2 list

#OUTPUT TO FILE (HW_2p1_Task2.txt)
refractedShit = "n1\tTheta1\tn2\tTheta2"  #column headers
w.write(refractedShit)  #write headers to file

for i in range(len(l)):             #write values to file
    w.write(f"\n{n1[i]:.3f}\t{theta1[i]}\t{n2[i]:.3f}\t{theta2[i]}")

w.close()   #close write file


#MORE STUFF
o = open("HW_2p1_Task2.txt", "r")

print("First 10 lines of HW_2p1_Task2.txt:\n")

for i in range(10):
    print(o.readline())

o.close()

#(ok idk what else to do without it just being annoying so thats it)
