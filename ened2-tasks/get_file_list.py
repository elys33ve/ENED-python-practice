#python 6: file I/O
#ACT_Python_6p1
#get list from values in file

listc = []
listf = []

#open file C for read 
c = open("docs\TempC.txt","r")      #file with column of temp values in deg C

#save to list
for line in c:                      #for each line in file
    listc.append(line.strip())      #append list w values from each line (strip newline)

#get number of lines in file
#####lines = len(open("docs\TempC.txt").readlines())
lines = len(listc)                  #get number of values

#convert to F
for i in range(lines):
    listc[i] = int(listc[i])        #change list values from string to integers
    fval = (listc[i] * (9/5)) + 32  #convert C to F
    listf.append(fval)              #add each F value to list F

#write to file F
fw = open("docs\TempF.txt","w")     #open F file for write
    
for i in range(lines):              
    listf[i] = str(listf[i])        #change from int to str
    fval = listf[i] + "\n"          #add newline (to print each value on new line)
    fw.write(fval)                  #write value to file
fw.close()                          #close and save 

#read file F
fr = open("docs\TempF.txt","r")     #open F file for read
print(fr.read())                    #output converted values

