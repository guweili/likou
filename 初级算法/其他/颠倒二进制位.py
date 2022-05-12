#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : 颠倒二进制位.PY
# @Time      : 2022/1/6 17:21
# @Author    : weilig
'''


'''


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        '''
        用一个新的变量去接受位运算变化，res
        将原数 n 右位运算，依次添加到 res开头顺序排列，最后的结构就是颠倒后的结果,
        n & 1 按位运算 当前位都为 1 则返回 1

        :param n:
        :return:
        '''
        res = 0
        for i in range(32):
            res <<= 1  # 新增一位
            print('res--------', bin(res))
            res += n & 1  # 取出来最后一位，并加到res
            print('res--------', bin(res))
            n >>= 1  # 去除最后一位
            print('n--------', bin(n))
        return res


if __name__ == '__main__':
    n = 0b00000010100101000001111010011100
    res = Solution().reverseBits(n)
    print(res)
