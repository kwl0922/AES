import swap as s

#逆向行移位变换
def r_row_shift(array):
    #第一行不变
    #第二行右移一位
    temp = array[7]
    for i in range(6, 3, -1):
        array[i+1] = array[i]
    array[4] = temp
    #第三行右移两位
    s.swap(array, 8, 10)
    s.swap(array, 9, 11)
    #第四行右移三位
    temp = array[12]
    for i in range(13, 16):
        array[i-1] = array[i]
    array[15] = temp