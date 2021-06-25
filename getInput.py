from conversion import  *

def getBinaryData():
    binaryNumList=[]
    flag=False
    while(not flag):
        mode=input("Press \"1\" to input Integer Number and press \"2\" to input Binary Number: ")
        if(mode ==""):
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("x                                                  Value Error!!                                                      x")
            print("x                                              No command Found!!                                            x")
            print("x                              please give a command to procced further!!                           x")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            continue
            
        elif(mode =="1"):
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("x                                                 **NOTE**                                                    x")
            print("x                       Only Enter positive number from 0 to 255                             x")
            print("x               Decimal numbers and Alphabet are not allowed to enter!               x")
            print("x                The sum of two numbers should not be more than 255                 x")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            isCorrectInput=False
            while(not isCorrectInput):
                isFirstInputCorrect = False
                while (not isFirstInputCorrect):
                    firstInput = input("\nEnter the first Integer number : ")
                    if(isInteger(firstInput)):
                        firstNumber =int(firstInput)
                        if(firstNumber<0 or firstNumber>255):
                            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                            print("x                                            Input Out of Range!!                                               x")
                            print("x                             Please input positive number less than 256!                           x")
                            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                            continue
                        else:
                            isFirstInputCorrect=True
                    else:
                        continue
                isSecondInputCorrect = False
                while (not isSecondInputCorrect):
                    secondInput = input("\nEnter the second Integer number :")
                    if(isInteger(secondInput)):
                        secondNumber =int(secondInput)
                        if(secondNumber<0 or secondNumber>255):
                            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                            print("x                                            Input Out of Range!!                                               x")
                            print("x                             Please input positive number less than 256!                           x")
                            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                            continue
                        else:
                            isSecondInputCorrect=True
                    else:
                        continue
                if((firstNumber + secondNumber)>255):
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    print("x                                            Sum out of range!!                                                 x")
                    print("x                  The sum of two number should not be more that 255                     x")
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    continue
                else:
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    print("x                                        Thank you for correct input!                                      x")
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    isCorrectInput=True
                    
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("x                                 Converting to Eight Bit Binary Digit                                   x")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            binaryNumList.append(decimalToBinary(firstNumber))
            binaryNumList.append(decimalToBinary(secondNumber))
            flag=True
            return binaryNumList
        elif(mode=="2"):
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("x                                                 **NOTE**                                                    x")
            print("x                       Only enter binary number from 0 to 11111111                     x")
            print("x               Decimal numbers and Alphabet are not allowed to enter!               x")
            print("x          The sum of the two numbers should not be more than 11111111      x")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            isCorrectInput=False
            while(not isCorrectInput):
                isFirstInputCorrect = False
                while (not isFirstInputCorrect):
                    firstBinaryDigit = input("\nEnter the first binary number:  ")
                    if(validBinaryDigit(firstBinaryDigit) ):
                        if(binaryToDecimal(firstBinaryDigit)<0 or binaryToDecimal(firstBinaryDigit)>255):
                            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                            print("x                                            Input Out of Range!!                                               x")
                            print("x                   Please input binary number from 0 to 11111111!                           x")
                            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                            continue
                        else:
                            isFirstInputCorrect=True
                    else:
                        continue
                isSecondInputCorrect = False
                while (not isSecondInputCorrect):
                    secondBinaryDigit = input("\nEnter the second binary number:  ")
                    if(validBinaryDigit(secondBinaryDigit) ):
                        if(binaryToDecimal(firstBinaryDigit)<0 or binaryToDecimal(secondBinaryDigit)>255):
                            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                            print("x                                            Input Out of Range!!                                               x")
                            print("x                   Please input binary number from 0 to 11111111!                           x")
                            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                            continue
                        else:
                            print
                            isSecondInputCorrect=True
                    else:
                        continue
                if(binaryToDecimal(firstBinaryDigit)+ binaryToDecimal(secondBinaryDigit)>255):
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    print("x                                            Sum out of range!!                                                 x")
                    print("x             The sum of two number should not be more that 11111111               x")
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    continue
                else:
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    print("x                                        Thank you for correct input!                                      x")
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    isCorrectInput=True
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("x                                Converting to Eight Bit Binary Digit                                    x")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            binaryNumList.append(convertToEightBit(firstBinaryDigit))
            binaryNumList.append(convertToEightBit(secondBinaryDigit))
            flag=True
            return binaryNumList
        else:
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("x                                            Wrong Command!!                                               x")
            print("x       Please input valid Command to to choose binary or decimal input!!            x")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


def isInteger(number):
    if(number ==""):
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("x                                                  Value Error!!                                                      x")
        print("x                                              Empty Field Found!!                                               x")
        print("x                                           Do not give empty values!!                                        x")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        return False
    try:
        int(number)
        return True
    except:
        try:
            float(number)
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("x                                                  Invalid Input!!                                                   x")
            print("x                                    Float and Double values found!!                                      x")
            print("x                                      Only enter positive integer!!                                         x")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            return False
        except:
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("x                                                  Invalid Input!!                                                   x")
            print("x                                  Alphabetes and Special Character Found!!                       x")
            print("x                                     Do not enter alphabets or characters !!                         x")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            return False
        
    
def validBinaryDigit(binaryNum):
    if(binaryNum ==""):
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("x                                                  Value Error!!                                                      x")
        print("x                                              Empty Field Found!!                                               x")
        print("x                                           Do not give empty values!!                                        x")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        return False
    try:
        int(binaryNum)
    except:
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("x                                                  Invalid Input!!                                                   x")
        print("x                             Alphabetes and Special Character Found Found!!                  x")
        print("x                                     Do not enter alphabets or characters !!                         x")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        return False
    for digit in binaryNum:
        if(digit not in ["0","1"]):
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("x                                                  Invalid Input!!                                                   x")
            print("x                              Invalid numbers for binary value entered!!                           x")
            print("x                               Only enter 1s and 0s as binary Number!!                            x")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            return False
    return True
