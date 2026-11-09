hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
minscalc = mins + dura
if minscalc > 60:
    minscalc -= 60
    hour += 1
if minscalc >= 10:
    print(hour, ":", minscalc)
else:
#    print(hour, ":0",minscalc")
#redone below using F strings to remove the space between :0 and minscalc
    print(f"{hour}:0{minscalc}")
