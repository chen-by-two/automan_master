# -*- coding: utf-8 -*-
# @Time    : 2020/10/19 14:54
# @Author  : Haoran
import os
class impotBKWApi:
    def do(self):
        path1 = os.path.join(os.path.dirname(__file__), "../ApiLib")
        path2 = os.path.join(os.path.dirname(__file__), "../KeyWordDriver/BusinesskeyWord.py")
        tagPy = []
        api = []
        exi = []
        need = []
        code = []
        #找apilib目录下所有接口文件
        for root,dirs,files in os.walk(path1):
            for f in files:
                if not f.__contains__(".pyc"):
                    tagPy.append(os.path.join(root,f))
        #遍历所有接口文件找出所有接口

        for p in tagPy:
            print(p)
            with open(p, mode="r+", encoding='UTF-8') as f:
                for line in f.readlines():
                    if line.startswith("class"):
                        api.append(os.path.split(p)[1].split(".")[0]+"_"+line.split(" ")[1].split("(")[0])
            f.close()
        #找出业务关键字所有接口
        with open(path2, mode="r+", encoding='UTF-8') as f1:
            for line in f1.readlines():
                if line.__contains__("(p, t):"):
                    exi.append(line.split(" ")[1].split("(")[0])
        f1.close()
        #取两个差集
        for a in api:
            if a not in exi:
                need.append(a)



        print(api.__len__(),exi.__len__(),need.__len__())
        for n in need:
            c = "\ndef "+n+"(p, t):" \
                        "\n\tmet = "+n.replace("_",".")+"()"\
                        "\n\treturn __defult(met, p, t)"
            # print(c)
            code.append(c)

        with open(path2, mode="a+", encoding='UTF-8') as f2:
            for qq in code:
                f2.write(qq)
        f2.close()
if __name__ == '__main__':
    BKW = impotBKWApi().do()