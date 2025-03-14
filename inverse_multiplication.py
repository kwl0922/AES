#用扩展的欧几里得法算，求GF(2^8)域中的乘法逆元，不可约多项式为x^8+x^4+x^3+x+1
'''
当除数比被除数小的时候，将除数左移一位，直到除数大于被除数或二进制的最高位相同时停止
然后将除数与被除数异或，得到余数
同时每次左移都会使q左移一位
''' 
Q = 0#记录商
qi = 0#记录余数
res = 0#记录最终结果，即乘法逆元

def divide(dividend, divisor,q):#dividend被除数, divisor除数, quotient单次除法的商，remainder余数
    quotient = 1
    global Q, qi
    tem_divisor = divisor

    while tem_divisor ^ dividend > tem_divisor:
        tem_divisor = tem_divisor << 1
        quotient = quotient << 1

    remainder = dividend ^ tem_divisor
    q = q + quotient#q记录商，用于递归的传递
    Q = Q + quotient
    qi = remainder

    if(remainder > divisor or (remainder < divisor and remainder ^ divisor < remainder and divisor << 1 > remainder)):
        divide(remainder, divisor, q)

def multiply(a, b):#GF(2^8)域中的乘法
    result = 0

    if a == 0 or b == 0:
        return 0

    s = [0]*8#s记录a的每一位左移一位的结果，若最高位发生溢出则与0x1b异或
    s[0] = a

    for i in range(1, 8):
        s[i] = s[i-1] << 1
        if s[i] & 0x100:
            s[i] = s[i] - 0x100
            s[i] = s[i] ^ 0x1b

    for i in range(8):
        if b & 1:
            result = result ^ s[i]
        b = b >> 1

    return result

def extended_euclid(r0, r1, v0, v1, w0, w1):
    global Q, qi, res
    divide(r0, r1, 0)
    v = v0 ^ multiply(Q, v1)
    w = w0 ^ multiply(Q, w1)
    Q = 0

    if qi != 0:
        extended_euclid(r1, qi, v1, v, w1, w)
    else:
        res = w1
        #print("在GF(2^8)上的乘法逆元为：", hex(w1))

def main(num):
# print("请输出待求乘法逆元的16进制数:")
#num = input()
    if num == 0 or num == 1:#0,1的乘法逆元为自身
        #print(hex(num), "在GF(2^8)上的乘法逆元为：", hex(num))
        return num
    else:
        extended_euclid(0x11b, num, 1, 0, 0, 1)
        return res