
try:
    hour = int(input("Enter your working hours: "))
    rate = int(input("Enter Your rate: "))
    if hour > 40:
        pay = rate* (40 + (1.5 * (hour-40)))
        print(f"Pay: P{pay}")
    else:
        pay = hour * rate
        print(f"Pay: {pay}")

except:
    print("Error, please enter numeric input")