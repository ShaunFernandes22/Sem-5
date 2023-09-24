# addition of binary strings
def add(A, M):
    carry = 0
    result = ""
    for i in range(len(A)-1,-1, -1):
        res = int(A[i]) + int(M[i]) + carry
        if res == 2:
            carry = 1
            res = 0
        elif res == 3:
            carry = 1    
            res = 1
        else:
            carry = 0
        result = str(res) + result   
    # -- here, carry is considered as separate bit --
    # if carry == 1:
        # result = '1' + result    
    return carry, result    
    
# converts to binary strings appropriately    
def binary(num, count):
    num = bin(num)[2:].zfill(count)
    return num

# all shift to the right by 1 and carry
def rightShift(C, A, Q, count):
    Q = A[-1] + Q[:count - 1]
    A = str(C) + A[:count -1] 
    C = 0
    return C, A, Q   

# ------Booth's algorithm-------
def boothUnsigned(M, Q):
    # iterations is max of both
    count = max(len(bin(abs(M))[2:]), len(bin(abs(Q))[2:]))
    
    # A -> accumulator, M -> Multiplicand, Q->Multiplier, C -> carry, count-> iterations
    M = binary(M, count)
    Q = binary(Q, count)
    A = "".zfill(count) # accumulator initialized 
    C = 0
    
    print(f"A = {A}, M = {M}, Q = {Q}, C = {C}")
    
    print(f"C  A   Q \tSteps:")
    for i in range(count):
        print(C, A, Q, f"\titr : {i}")  
        
        if Q[-1] == '1':
            C, A = add(A, M)
        print(C, A, Q, f"\tadd\titr : {i}")  
        
        C, A, Q = rightShift(C, A, Q, count)  
        print(C, A, Q, f"\tRS\titr : {i}")  
          
    bin_num = (A+Q)
    decimal_num = int((A+Q), 2)         
    return bin_num, decimal_num
    
# input M & Q in decimal (note : both have to be +ve)
M = int(input("Enter the multiplicand in decimal form : "))
Q = int(input("Enter the multiplier in decimal form : "))

binary_num, product = boothUnsigned(M, Q)
print("The number in binary form is ", binary_num)        
print("The decimal value of product of unsigned multiplication is ", product)
