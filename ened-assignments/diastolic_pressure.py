# Description:
# This python script opens a file (HW2p1_Task1.txt) and adds the values into a 
# list. It then tests each list item and determines the amount of 'normal',
# 'at risk', and 'high' items there are. Next, it calculates the mean, standard
# deviation, and maximum & minumum values; outputting each value using print
# statements.
# (and also using the statistics module to verify the answers. but i did the
# math stuff myself too i swear)


#OPEN FILE 
o = open("HW2p1_Task1.txt", "r")   #open file for read
#(^ file with one column of values)

#CREATE LIST FROM FILE
v = []                  #list of values

for line in o:
    v.append(line.strip())

#TEST VALUES (normal, at risk, high)
normal, risk, high = 0, 0, 0    #sum of days
v_len = len(v)                  #length of list/number of values
v_sum = 0                       #sum of values

for i in range(v_len):
    v[i] = int(v[i])
    if v[i] < 80:                       #normal
        normal = normal + 1
    elif v[i] < 90 and v[i] > 79:       #at risk
        risk = risk + 1
    else:                               #high
        high = high + 1
    v_sum = v_sum + v[i]        #sum of values

#AVERAGE
average = v_sum / v_len                 #mean

#STANDARD DEVIATION
sd_sum = 0              #stdev numerator sum

for i in range(v_len):
    x = float(v[i])
    y = (x - average)**2
    sd_sum = sd_sum + y

st_dev = (sd_sum / v_len)**(1/2)        #standard deviation

#MAX
max_v = v[0]                    #max list value

for i in range(v_len):
    if v[i] >= max_v:
        max_v = v[i]
    else:
        pass

#MIN
min_v = v[0]                    #min list value

for i in range(v_len):
    if v[i] <= min_v:
        min_v = v[i]
    else:
        pass

o.close()

#OUTPUTS
print(f"Days diastolic pressure was normal:        {normal}")       #normal
print(f"Days diastolic pressure was at risk:       {risk}")         #risk
print(f"Days diastolic pressure was high:          {high}")         #high
print(f"Average diastolic pressure:                {average:.1f}")  #mean
print(f"Standard deviation of diastolic pressures: {st_dev:.1f}")   #st dev
print(f"Maximum diastolic pressure value:          {max_v}")        #max
print(f"Minimum diastolic pressure value:          {min_v}")        #min

#VERIFY ------------------------------------------------------------------------
import statistics as s

print("\n\nVERIFY------------------------------")
print(f"mean:               {s.mean(v):.1f}")
print(f"standard deviation: {s.stdev(v):.1f}")
print(f"max:                {max(v)}")
print(f"min:                {min(v)}")


#(i'd rather be doing this than physics hw so i'm making it fancy)
