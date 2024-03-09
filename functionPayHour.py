def computepay(hour, rate):
    try:
        hour = float(hour)
        rate = float(rate)
        if hour > 40:
            pay = rate* (40 + (1.5 * (hour-40)))
            print(f"Pay: P{pay}")
        else:
            pay = hour * rate
            print(f"Pay: {pay}")

    except:
        print("Error, please enter numeric input")

def computegrade(score):
    try:
        score = float(score)
        if score < 1.0:
            if score >= 0.9:
                print("A")
            elif score >= 0.8:
                print("B")
            elif score >= 0.7:
                print("C")
            elif score >= 0.6:
                print("D")
            elif score < 0.6:
                print("F")
        else: 
            print("Bad Score")
    except:
        print("Bad Grade")

computepay(45,10)
computegrade(0.6)