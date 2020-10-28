distance = int(input("Distance (km) : "))
time = int(input("Time (h) : "))
if(distance < 1):
    print("Distance can not be less than 1 km")
elif(time < 1):
    print("Time can not be less than 1 hour")
else:
    result = distance / time
    print(result,"km/h")