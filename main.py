from getInput import *
from conversion import *
from adder import *

def main():
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("x                                                                                                                          x")
    print("x                       ***Welcome To the Byte adder Program!***                              x")
    print("x                                                                                                                          x")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    flag=False
    while(not flag):
        binaryNumList = getBinaryData()
        print("The eight bit binary digit of the given input are: "+binaryNumList[0] + " and "+binaryNumList[1]+"\n")
        binary_sum=adder(binaryNumList)
        decimal_sum = binaryToDecimal(binaryNumList[0])+ binaryToDecimal(binaryNumList[1])
        print("Adding in binary\t\t\tAdding in  Decimal")
        print("   "+binaryNumList[0]+"\t\t\t          ",binaryToDecimal(binaryNumList[0]))
        print(" +"+binaryNumList[1]+"\t\t\t        +",binaryToDecimal(binaryNumList[1]))
        print("   --------------     \t\t\t          -----")
        print("   "+binary_sum+"\t\t\t          ",decimal_sum)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("The binary sum is given input is "+binary_sum  )                                         
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("Do you want to continue or exit the program?")
        correct_input=False
        while(not correct_input):
            doContinue=input("Press \"c\" or \"C\" to continue or \"e\" or \"E\" to exit: ")
            if(doContinue.lower()==""):
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("x                                                  Value Error!!                                                      x")
                print("x                                              No command Found!!                                            x")
                print("x                              please give a command to procced further!!                           x")
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                continue
            elif(doContinue.lower()=="e"):
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("x                                               Exiting Program!!                                                x")
                print("x                                     Thank you for using  the program!                                x")
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                flag=True
                correct_input=True
            elif(doContinue.lower()=="c"):                
                flag=False
                correct_input=True
            else:
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("x                                            Wrong Command!!                                               x")
                print("x             Please input valid Command to exit or continue the program!              x")
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
main()
