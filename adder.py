from conversion import  *
def adder(binaryNumList):
    binaryNum1 = binaryNumList[0]
    binaryNum2 = binaryNumList[1]
    sum_value=""
    carry_in=0    
    for i in range(len(binaryNum1)-1,-1,-1):
        upper_bit = int(binaryNum1[i] )
        lower_bit = int(binaryNum2[i] )
        xor_value= (upper_bit ^ lower_bit)
        sum =xor_value ^ carry_in
        carry_out = (upper_bit & lower_bit) | (xor_value & carry_in)
        carry_in=carry_out
        sum_value= str(sum)+sum_value
    return sum_value
