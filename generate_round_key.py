import format_print as f, S_box as s
#生成轮密钥

def generate_round_key(key, rounds):#key是密钥，rounds是轮数
    #生成S盒
    s_box = s.generate_s_box()
    keys = []#存放所有轮密钥
    #轮常量
    round_constant = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]
    keys[0:16] = key
    for round in range(rounds):
        #翻转数组，为了与p126的例子保持一致
        f.row_to_column(key)

        w0 = key[0:4]
        w1 = key[4:8]
        w2 = key[8:12]
        w3 = key[12:16]

        #第4行字左移1位
        z1 = w3[1:] + w3[:1]

        #第4行字替代
        for i in range(4):
            z1[i] = s_box[int(z1[i], 16)]
        
        #将数组转化为整型，方便异或
        for i in range(4):
            z1[i] = int(z1[i], 16)
            w0[i] = int(w0[i], 16)
            w1[i] = int(w1[i], 16)
            w2[i] = int(w2[i], 16)
            w3[i] = int(w3[i], 16)
        
        #第4行字与轮常量异或
        z1[0] = z1[0] ^ round_constant[round]

        #生成下一轮的轮密钥
        temp = []
        for i in range(4):
            temp.append(w0[i] ^ z1[i])
        key[0:4] = temp
        for i in range(4):
            temp[i] = temp[i] ^ w1[i]
        key[4:8] = temp
        for i in range(4):
            temp[i] = temp[i] ^ w2[i]
        key[8:12] = temp
        for i in range(4):
            temp[i] = temp[i] ^ w3[i]
        key[12:16] = temp

        #格式化轮密钥
        for i in range(16):
            key[i] = hex(key[i])
            key[i] = key[i].replace('0x', '').upper()
            if len(key[i]) == 1:
                key[i] = '0' + key[i]
        
        #翻转数组
        f.row_to_column(key)
        keys[i * 16: (i + 1) * 16] = key
    return keys