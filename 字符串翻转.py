# 1、用python实现：
# 实现字符串反转，以逗号作为切割符，切割的子串以单词作为单元反转
# 输入：hello world, god bless you
# 输出：world hello, you bless god
def my_str(value):
    str_list = []
    for i in value.split(','):
        if i == '':
            i = ','
        str_list.append(i)

    new_str = ''
    for i in str_list:
        if i == ',':
            new_str += i
        else:
            new_str += ' '.join(i.split()[::-1]) + ','

    print(new_str.replace(',', '', 1))


if __name__ == '__main__':
    a = ',,hello world, god bless you,,,'
    my_str(a)

# 2、写一个js函数，实现对一个数字每3位加一个逗号，如输入100000， 输出100,000（不考虑负数，小数）
