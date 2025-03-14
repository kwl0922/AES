import inverse_multiplication as inv_mul
'''
逆S盒的生成过程是：
先将字节到位列向量，再从位列向量到字节，最后求逆元
'''
a = 0x05#逆S盒的生成多项式
r_s = [0] * 256#r_s记录每个数，而后转化为逆s盒
c = [0] * 8#记录a的每一位二进制数
b = [0] * 8#记录s中每个字节的每一位二进制数
res = [0] * 8#记录最终逆s盒中每个字节的每一位二进制数

for i in range(8):#将a的每一位二进制数存入c中
    c[i] = a & 1
    a = a >> 1

for i in range(256):
    r_s[i] = i

    for j in range(8):#将s中每个乘法逆元的每一位二进制数存入b中
        b[j] = r_s[i] & 1
        r_s[i] = r_s[i] >> 1

    for j in range(8):#将b中每一位与c异或后存入res中，最终将res中的二进制数转化为逆s盒中的一个字节
        res[j] = b[(j+2)%8] ^ b[(j+5)%8] ^ b[(j+7)%8] ^ c[j]

    for j in range(8):#将最终每个字节的二进制数转化为十进制数
        if res[j] & 1:
            r_s[i] = r_s[i] + 2**j

'''
输出逆S盒，每行16个数，每个数之间用空格隔开，
每个数为两位十六进制数，不足两位的用0补齐，字母大写
'''
# print("逆S盒为:")
for i in range(256):
    # if i % 16 == 0 and i != 0 and i != 256:
    #     print()
    r_s[i] = hex(inv_mul.main(r_s[i]))
    r_s[i] = r_s[i].replace('0x','').upper()

    if len(r_s[i]) == 1:
        r_s[i] = '0' + r_s[i]

#     print(r_s[i], end = ' ')#end = ' '表示不换行输出
def generate_r_s_box():
    return r_s