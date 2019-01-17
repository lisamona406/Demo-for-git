# exponent functiom

#print(2**3)

#def raise_to_power(base_num,pow_num):
    #result=1
    #for index in range(pow_num):
        #result=result*base_num
        #print(pow_num)
    #return result
base_num=int(input("enter base_num:"))
pow_num=int(input("enter the power you want to raise to:"))
def raise_to_power(base_num,pow_num):
    result=1
    for index in range(pow_num):
        result=result*base_num
    return result
print(raise_to_power(base_num,pow_num))