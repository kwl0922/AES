import inverse_multiplication as i_m

#列混淆变换
def column_mix(array):
    asist = [0] * 16#辅助数组,用于存储行移位变换后的结果
    for i in range(16):
        asist[i] = int(array[i], 16)
    for i in range(16):
        if i / 4 == 0:
            array[i] = i_m.multiply(0x02, asist[i]) ^ i_m.multiply(0x03, asist[i+1*4]) ^ asist[i+2*4] ^ asist[i+3*4]
        elif i / 4 == 1:
            array[i] = asist[i-1*4] ^ i_m.multiply(0x02, asist[i]) ^ i_m.multiply(0x03, asist[i+1*4]) ^ asist[i+2*4]
        elif i / 4 == 2:
            array[i] = asist[i-2*4] ^ asist[i-1*4] ^ i_m.multiply(0x02, asist[i]) ^ i_m.multiply(0x03, asist[i+1*4])
        else:
            array[i] = i_m.multiply(0x03, asist[i-3*4]) ^ asist[i-2*4] ^ asist[i-1*4] ^ i_m.multiply(0x02, asist[i])
        array[i] = hex(array[i])#将结果转化为16进制，方便格式化输出
        array[i] = array[i].replace('0x', '').upper()