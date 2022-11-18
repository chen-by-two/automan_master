# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : Haoran
import Common.ExcelHandler as excel
import os,xlrd
class impotApi:
    def __init__(self, *args, path='../TestFile/ApiInfo.xlsx',ifall=True):
        self.apiInfo = xlrd.open_workbook(os.path.join(os.path.dirname(__file__), path))
        self.module_args=args
        self.ifall = ifall

    def readExcel(self):
        #通过sheet页获取功能模块,判断是否获取全部
        if self.ifall:
            modules = self.apiInfo.sheet_names()
        else:
            modules = self.module_args
        #按照sheet页遍历并且写入接口
        for module in modules:
            path = os.path.dirname(__file__)
            modulePath = os.path.join(path, "../ApiLib", module)
            #如果模块目录已经存在就不创建，如果不存在就创建一个模块目录
            if os.path.exists(modulePath):
                existsApis = []
                print(modulePath + "/" + module + "Api.py")
                with open(modulePath + "/" + module + "Api.py",mode="r+",encoding='UTF-8') as f0:
                    for line in f0.readlines():
                        if line.startswith("class"):
                            existsApis.append(line.split(" ")[1].split("(")[0])
                with open(modulePath + "/" + module + "Api.py",mode="a",encoding='UTF-8') as f:
                    codes = self.writeApiCode(module)
                    #需要加一个判断，不会重复写之前已经存在的接口
                    for apiName in codes.keys():
                        if apiName in existsApis:
                            pass
                        else:
                            f.write(codes[apiName])
                    f.close()
            else:
                os.makedirs(modulePath)
                # open(modulePath + "/" + module + "Api.py")
                with open(modulePath + "/" + module + "Api.py",mode="a+",encoding="UTF-8") as f:
                    codes = self.writeApiCode(module)
                    f.write("# -*- coding: utf-8 -*-\n")
                    f.write("from Common.HttpHandler import httpHandler")
                    for apiName in codes.keys():
                        f.write(codes[apiName])
                    f.close()


            # print(os.getcwd()+"/"+module)
            # print(os.path.exists(os.getcwd()+"/"+module))

    def writeApiCode(self,module):
        apis = self.apiInfo.sheet_by_name(module)
        resule = {}
        str = ""
        #获取行数,根据行数循环
        for i in range(apis.nrows):
            if i == 0:
                continue
            tmpapi = apis.row_values(i)
            tmpapiName = tmpapi[1]
            tmpapiHost = tmpapi[2]
            tmpapiPath = tmpapi[3]
            tmpapiMethod = "0"
            tmpapiHeaders = tmpapi[5]
            tmpapiParams = tmpapi[6]
            tmpapiData = tmpapi[7]
            tmpapiDesc = tmpapi[8]
            if tmpapi[4] == "GET":
                tmpapiMethod = "0"
            elif tmpapi[4] == "POST":
                tmpapiMethod = "1"
            # if tmpapi[6] == "None":
            #     tmpapiParams = None
            # else:
            #     tmpapiParams = tmpapi[6]
            # if tmpapi[7] == "None":
            #     tmpapiData = None
            # else:
            #     tmpapiData = tmpapi[7]


            str = "\n\n\nclass"+" "+tmpapiName +"(httpHandler):" +\
                  "\n\tdef __init__(self):"+\
                  "\n\t\tsuper("+tmpapiName+", self).__init__()"+\
                  "\n\t\tself.host = " + "\"" + tmpapiHost + "\""+\
                  "\n\t\tself.path = " + "\"" + tmpapiPath + "\""+\
                  "\n\t\tself.headers = "  + tmpapiHeaders +\
                  "\n\t\tself.params = "  + tmpapiParams +\
                  "\n\t\tself.data = "  + tmpapiData +\
                  "\n\n"+\
                  "\tdef changeEnv(self,env):"+\
                  "\n\t\tself.host = self.host.replace(\"turboradio.cn\",env)"+ \
                  "\n\n" + \
                  "\tdef excute(self):"+\
                  "\n\t\tif self.params != None:"+\
                  "\n\t\t\tfor k in self.params.keys():"+\
                  "\n\t\t\t\tself.path = self.path+self.params[k]"+\
                  "\n\t\tself.response = self.run("+tmpapiMethod+")"+\
                  "\n\t\tself.logger.info(self.path +\"\tdone\" + \"\t"+tmpapiDesc+"\")"+\
                  "\n\t\treturn self.response"

            resule[tmpapiName] = str

        # print(resule)
        return resule

if __name__ == '__main__':
    #ss = impotApi().readExcel()
    # with open("/Users/liuhaoran/PycharmProjects/automan/ApiLib/goodsCenter/goodsCenterApi.py",mode = "a") as f:
    #     lines = f.readlines()
    #     print(lines)
    apiInfo=xlrd.open_workbook(os.path.join(os.path.dirname(__file__), "../TestFile/ApiInfo.xls"))
    print(apiInfo, type(apiInfo))
    modules = apiInfo.sheet_names()
    print(modules, type(modules))