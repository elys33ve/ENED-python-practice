# Determine min & max from list of data points:
# This python script asks the number of data points a user will input, then
# allows the user to enter each value into a list one-by-one. It will test each
# list value to determine the min and max, before outputting the number of
# data points entered, min value, and max value.

def mm():
#(^ to make it easier to rerun and test)
    dp = []         #data points list

#input -- # of data points
    points = int(input("Number of data points:  "))

#enter data loop
    for i in range(points):
        n = i + 1
        d = float(input(f"Data point {n}:  "))
        dp.append(d)
    
#find max/min
    max_ = dp[0]
    min_ = dp[0]

    for i in range(points):
        if dp[i] >= max_:
            max_ = dp[i]
        if dp[i] <= min_:
            min_ = dp[i]

#verify
    Max = max(dp)
    Min = min(dp)

#outputs
    print(f"Data points entered:  {points}")
    print(f"Minimum value:  {min_}")
    print(f"Maximum value:  {max_}")
    print(f"\n\nMin: {Min}\tMax: {Max}")            #verify

mm()
