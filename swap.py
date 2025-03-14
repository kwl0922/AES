#交换数组中的两个数
def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp