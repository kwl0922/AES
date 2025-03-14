#密钥与明文进行异或，即轮密钥加
def round_key_add(array, key):
    for i in range(16):
        array[i] = hex(int(array[i], 16) ^ int(key[i], 16))#将明文与密钥进行异或运算，结果转化为16进制，方便格式化输出
        array[i] = array[i].replace('0x', '').upper()