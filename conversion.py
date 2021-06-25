def binaryToDecimal(binaryNum):
    decimal_num=0
    j=0
    for i in range(len(binaryNum)-1,-1,-1):
        decimal_num += int(binaryNum[i]) * (2**j)
        j+=1
    return decimal_num  
        
def decimalToBinary(decimalNum):
    binaryNum=""
    if(decimalNum==0):
        binaryNum="0"
    else:
        while(decimalNum!=0):
            r=decimalNum%2
            binaryNum=str(r)+binaryNum
            decimalNum//=2
    eightBitBinary=convertToEightBit(binaryNum)
    return eightBitBinary

def convertToEightBit(binaryNum):
    eightBit=binaryNum
    if(len(binaryNum)!=8):
        for i in range(len(binaryNum),8):
            eightBit="0"+eightBit
    return eightBit

