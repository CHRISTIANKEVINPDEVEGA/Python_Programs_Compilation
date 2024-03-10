def minmax(maxVal, minVal, val):
    if maxVal is None or val > maxVal:
        maxVal= val
    if minVal is None or val < minVal:
        minVal = val
    return maxVal, minVal

maxVal = None
minVal = None

while True:
    userInput = input("Enter a number: ")
    try:
        number = int(userInput)
        maxVal_eval , minVal_eval = minmax(maxVal, minVal, number)
        maxVal = maxVal_eval
        minVal = minVal_eval
        continue

    except:
        if userInput == "done":
            print(f"Max Value: {maxVal}, Min Value: {minVal}")
            break
        else:
            print("Invalid, Please Enter a number")
            continue

        # userInput = input("Enter a number: ")
        # number = int(userInput)
        # minmax(number)
        # continue