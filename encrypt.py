import byte_replace as b_r, round_key_add as r_k_a
import row_shift as rs, column_mix as c_m, format_print as f

#AES加密
def encrypt(array, keys, rounds):
    for round in range(rounds):
        #密钥与明文进行异或
        r_k_a.round_key_add(array, keys[round*16:(round+1)*16])
        #print("第", round+1, "轮异或：\n", array)

        #字节替代
        b_r.byte_replace(array)
        #print("第", round+1, "轮字替：\n", array)

        #正向行移位变换
        rs.row_shift(array)
        #print("第", round+1, "轮行移：\n", array)

        #正向列混淆变换
        c_m.column_mix(array)
        #print("第", round+1, "轮列混：\n", array)  

    r_k_a.round_key_add(array, keys[(round+1)*16:(round+2)*16])
    f.row_to_column(array)

    code = str()
    for i in range(16):
        if len(array[i]) == 1:
            array[i] = '0' + array[i]
        code = code + array[i]
    print("加密的密文：" + code)