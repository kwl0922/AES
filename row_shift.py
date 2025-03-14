import swap as s

#行移位变换
def row_shift(array):
    #第一行不变
    #第二行左移一位
    temp = array[4]
    for i in range(5, 8):
        array[i-1] = array[i]
    array[7] = temp
    #第三行左移两位
    s.swap(array, 8, 10)
    s.swap(array, 9, 11)
    #第四行左移三位
    temp = array[15]
    for i in range(14, 11, -1):
        array[i+1] = array[i]
    array[12] = temp