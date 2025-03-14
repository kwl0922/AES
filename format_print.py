import swap as sp
#对16进制表示的字符型数组格式化输出
def format_print(array):
    for i in range(16):#输出明文，方便查看
        if i % 4 == 0 and i != 0 :
            print()
        if len(array[i]) == 1:
            array[i] = '0' + array[i]
        print(array[i], end=' ')
    print('\n')

#将行排序转换为列排序
def row_to_column(array):
    sp.swap(array, 1, 4)
    sp.swap(array, 2, 8)
    sp.swap(array, 3, 12)
    sp.swap(array, 6, 9)
    sp.swap(array, 7, 13)
    sp.swap(array, 11, 14)