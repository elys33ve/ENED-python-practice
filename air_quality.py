#output statement for air quality based on corresponding range of input value

user = float(input("Air quality input (AQI):  "))


if user in range(0,51):
    print("Good")
elif user > 50 and user <= 100:
    print("Satasfactory")
elif user > 100 and user <= 200:
    print("Moderate")
elif user in range (201,301):
    print("Poor")
elif user > 300 and user <= 400:
    print("Very poor")
elif user > 400 and user <= 500:
    print("Severe")
else:
    print("Invalid input")
