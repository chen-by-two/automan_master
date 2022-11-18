# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : Haoran
import pypinyin

def chn2Pinyin(word):
    str = ""
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        print(i)
        str = str + i[0].capitalize()
    print(str)
    return str

if __name__ == '__main__':
    chn2Pinyin("123上课课爱你made是的")