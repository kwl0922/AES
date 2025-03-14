import encrypt as ec, decrypt as dc, format_print as f
import generate_round_key as g_r_k

'''
case1:
明文 = "hello,world!1234"
密钥 = "0123456789999999"
密文 = "CABD064B180259DA44A68BC7506DD136"
'''
#输入16位字符，每位字符转化为ascii码后转化为16进制，占8位，一共是128位

def main():
    print("=============AES-128加密算法=============")
    print("1.加密")
    print("2.解密")
    print("3.退出")
    choice = input("请选择：")
    if choice == "3":
        exit()
    elif choice != "2" and choice != "1":
        print("输入错误，请重新输入！")
        main()
    else:
        array= []
         #读取16位字符串，即128位
        if choice == "1":
            plaintext = input("请输入明文：")
            for i in range(16):
                array.append(hex(ord(plaintext[i])))
                array[i].replace("0x", "")#去掉0x
        else:
            plaintext = input("请输入密文：")
            for i in range(0, 32, 2):
                array.append(plaintext[i:i+2])

        round_key = input("请输入密钥：")
        
        key = []
        for i in range(16):#将明文与密钥分别每两个字符存入数组中
            key.append(hex(ord(round_key[i])))
            key[i].replace("0x", "")#去掉0x

        #由行排序转换为列排序
        f.row_to_column(array)
        f.row_to_column(key)
        
        rounds = 10#加解密轮数
        for i in range(16):
            array[i] = array[i].upper()#将明文中的每个字符转化为大写
            key[i] = key[i].upper()#将密钥中的每个字符转化为大写

        keys = g_r_k.generate_round_key(key, rounds)#生成10轮的轮密钥
        
        if choice == "1":#加密
            ec.encrypt(array, keys, rounds)
        else:#解密
            dc.decrypt(array, keys, rounds)

if __name__ == "__main__":
    main()
