''' Problem Description:
Have the function PlusMinus(num) read the num parameter being passed which will be a combination of 1 or more single digits,
and determine if it's possible to separate the digits with either a plus or minus sign to get the final expression to equal zero. 
For example: if num is 35132 then it's possible to separate the digits the following way, 3 - 5 + 1 + 3 - 2, and this expression 
equals zero. Your program should return a string of the signs you used, so for this example your program should return -++-. If it's 
not possible to get the digit expression to equal zero, return the string not possible. If there are multiple ways to get the final 
expression to equal zero, choose the one that contains more minus characters. For example: if num is 26712 your program should return 
-+-- and not +-+-. 
Sample Test Cases: 
Input: 199 Output: not possible 
Input: 26712 Output: -+--
'''

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
