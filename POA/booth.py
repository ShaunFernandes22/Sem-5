# A -> accumulator, M -> Multiplicand, Q->Multiplier, Q1 -> extra_bit, count

# input M & Q in decimal
M = int(input("Enter the multiplicand in decimal form : "))
Q = int(input("Enter the multiplier in decimal form : "))

# number of iterations according to binary length (zeroes in accumulator)
count = max(len(bin(abs(M))[2:]), len(bin(abs(Q))[2:]), 4)

def twosComplement(num):
    comp = ""
    for i in range(len(num)):
        if num[i] == '0':
            comp += '1'
        else:
            comp += '0'
    comp = bin(int(comp, 2) + int('1', 2))[2:]
    return comp
    
# 4 combinations of M, Q being +ve and -ve    
if M < 0 and Q < 0:
    M = twosComplement(bin(abs(M))[2:].zfill(count))
    Q = twosComplement(bin(abs(Q))[2:].zfill(count))
elif M < 0 and Q >= 0:
    M = twosComplement(bin(abs(M))[2:].zfill(count))
    Q = bin(Q)[2:].zfill(count)
elif M >=0 and Q < 0:
    M = bin(M)[2:].zfill(count)
    Q = twosComplement(bin(abs(Q))[2:].zfill(count))
else:    
    M = bin(M)[2:].zfill(count)
    Q = bin(Q)[2:].zfill(count)
    
M_dash = twosComplement(M) # for negative M
A = "".zfill(count) # accumulator initialized 
Q1 = '0' # initialize

def rightShift(A, Q, Q1):
    if len(A) == count + 1:
        A = A[1:]
    Q1 = Q[-1]
    Q = A[-1] + Q[:count - 1]
    A = A[0] + A[:count -1] 
    
    return A, Q, Q1   
    
for _ in range(count):
    x = Q[-1] + Q1
    if x == '01':
        A = bin(int(A,2) + int(M, 2))[2:].zfill(count)
    elif x == '10':
        A = bin(int(A,2) + int(M_dash, 2))[2:].zfill(count)

    A, Q, Q1 = rightShift(A, Q, Q1)  
    print(A, Q, Q1)  
    
if (A[0] == '1'):
    print("A + Q = ", A+Q)
    num = twosComplement(A+Q).zfill(len(A+Q))
    dec = -int(num, 2)    
    print("2's complement of A+Q : ")
else:
    num = (A+Q)
    dec = int((A+Q), 2)         
    
print("The number in binary form is ", num)        
print("The decimal value of product of signed multiplication is ", dec)
