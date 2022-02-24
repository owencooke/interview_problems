def PlusMinus(num):
    # First digit must be positive
    runSum = int(num[0])
    numDigits = len(num)
    strOut = ""
    # Each subsequent digit can be added/subtracted
    strOut = recurse(num[1:numDigits], runSum, strOut, numDigits)
    return strOut


def recurse(num, runSum, strOut, numDigits):
    if len(num) < 1:
        return "not possible"
    nextDig = int(num[0])
    add = runSum + nextDig
    sub = runSum - nextDig
    # Base cases: sum reaches zero after using last digit
    if (sub == 0) and (len(num) == 1):
        strOut += "-"
    elif (add == 0) and (len(num) == 1):
        strOut += "+"
    # No base case reached, recurse further
    else:
        subStr = recurse(num[1:numDigits], sub, strOut + "-", numDigits)
        addStr = recurse(num[1:numDigits], add, strOut + "+", numDigits)
        # Desc. specifies to return str with more minus characters
        # Prioritize utilizing string from subtraction if possible
        if subStr == "not possible":
            strOut = addStr
        else:
            strOut = subStr
    return strOut

if __name__ == "__main__":
    print(PlusMinus(input()))