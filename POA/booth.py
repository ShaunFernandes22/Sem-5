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
    # ----------Discard carry right here----------
    # if carry == 1:
        # result = '1' + result    
    return result    
    
def twosComplement(num):
    # one's complement 
    n = len(num)
    comp = ""
    for i in range(n):
        if num[i] == '0':
            comp += '1'
        else:
            comp += '0'
    # adding 1        
    comp = add(comp, '1'.zfill(n))
    return comp
    
# converts to binary strings appropriately    
def binary(num, count):
    if num >= 0 :
        num = bin(num)[2:].zfill(count)
    else:
        num = - num
        num = bin(num)[2:].zfill(count)
        num = twosComplement(num)
    return num

# all shift to the right by 1 and A_msb stays put
def rightShift(A, Q, Q1, count):
    Q1 = Q[-1]
    Q = A[-1] + Q[:count - 1]
    A = A[0] + A[:count -1] 
    return A, Q, Q1   

# ------Booth's algorithm-------
def boothSigned(M, Q):
    # iterations is 1 more than 
    count = max(len(bin(abs(M))[2:]), len(bin(abs(Q))[2:])) + 1
    
    # A -> accumulator, M -> Multiplicand, Q->Multiplier, Q1 -> extra_bit, count-> iterations
    M = binary(M, count)
    Q = binary(Q, count)
    M_neg = twosComplement(M) # for negative M
    A = "".zfill(count) # accumulator initialized 
    Q1 = '0' # initialized 

    for i in range(count):
        print(A, Q, Q1)  
        
        x = Q[-1] + Q1
        if x == '01':
            A = add(A, M)
        elif x == '10':
            A = add(A, M_neg)
        print(A, Q, Q1)  

        A, Q, Q1 = rightShift(A, Q, Q1, count)  
        print(A, Q, Q1)  
    
    if (A[0] == '1'): # negative answer
        print("A + Q = ", A+Q)
        bin_num = twosComplement(A+Q)
        decimal_num = -int(num, 2)    
        print("2's complement of A+Q : ")
    else:
        bin_num = (A+Q)
        decimal_num = int((A+Q), 2)         
    return bin_num, decimal_num
    
# input M & Q in decimal
M = int(input("Enter the multiplicand in decimal form : "))
Q = int(input("Enter the multiplier in decimal form : "))

binary_num, product = boothSigned(M, Q)
print("The number in binary form is ", binary_num)        
print("The decimal value of product of signed multiplication is ", product)
