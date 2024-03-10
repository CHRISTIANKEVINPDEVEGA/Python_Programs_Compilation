def minmax(input_dict):
    maxVal = None
    minVal = None
    for val in input_dict:
        if maxVal is None or val > maxVal:
            maxVal= val
        if minVal is None or val < minVal:
            minVal = val
    return maxVal, minVal

print(minmax([2,3,0,4,5]))