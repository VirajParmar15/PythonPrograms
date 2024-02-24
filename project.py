#que how many days of temprature
#ans 5
#day 1 temp = input1
#day 2 temp = input2
#day 3 temp = input3
#day 4 temp = input4
#day 5 temp = input5
#print avearge of this all days temprature
#print how many days temprature is above average


days = int(input("how many days of temprature: "))
total = 0
temp = []
for i in range(days):
    nextday = int(input("day" + str(i+1) + "'s high temp"))
    temp.append(nextday)
    total += temp[i]

average = round(total / days)
print("average of temprature" + str(average))

above = 0
for i in temp:
    if i > average:
        above =+ 1

print(str(above) + "day(s) above average")





    




