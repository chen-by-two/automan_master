# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : Haoran
import json, yaml, re, time, datetime
import os

import Common.JsonTools as jsonTools
import Common.MysqlHandler as mysqlHandler
from Common.ReadConfig import readConfig as readConfig
from Common.LoggerHandler import MyLog as Log
import Common.RedisHandler as redisHandler
import Common.SshTunnel as MysqlSshHandler


import ctypes

class CommonKeyWord:
    def __init__(self):
        self.logger = Log.get_log().logger



    def Var_NewStr(self, s):
        oo = "*15005150023*"
        res = s
        if s.startswith("*") and s.endswith("*"):
            tmp = s[1:]
            res = tmp[:-1]
        return res

    def Var_NewArray(self, *kargs):
        res = []
        for k in kargs:
            res.append(k)
        return res

    def Var_NewDict(self, d):
        return d

    def Str_Replace(self, s1, s2, s3):
        if type(s2) != str:
            s2 = str(s2)
        if type(s3) != str:
            s3 = str(s3)
        s1 = s1.replace(s2, s3)
        return s1

    def Array_Append(self, a, v):
        a.append(v)
        return a

    def Array_ModifyByIndex(self, a, i, v):
        a[int(float(i))] = v
        return a

    def Array_GetByIndex(self, a, i):
        return a[int(float(i))]

    def Dict_ModifyByKey(self, d, k, v):
        d[k] = v
        return d

    def Dict_GetByKey(self, d, k):
        return d[k]

    def Print_ToControl(self, *kargs):
        fins = ""
        for k in kargs:
            fins += str(k)
        print("打印信息:", str(fins))

    def Print_ToLog(self, *kargs):
        fins = ""
        for k in kargs:
            fins += str(k)
        self.logger.info(str(fins))

    def Json_GetJsonValue(self, jsonDict, k):
        return jsonTools.getJsonValue(jsonDict, k)

    def Json_GetJsonValues(self, jsonDict, keyList):
        return jsonTools.getJsonValues(jsonDict, keyList)

    def Yaml_Read(self, path):
        f = open(path, "r", encoding="utf-8")
        y = yaml.load(f.read(),Loader=yaml.FullLoader)
        f.close()
        return y

    def Yaml_ReadNew(path):
        f = open(path, "r", encoding="utf-8")
        y = yaml.load(f.read(),Loader=yaml.FullLoader)
        f.close()
        return y

    def Yaml_Write(self, path, token, keyid, userid):
        f = open(path, "w+", encoding="utf-8")
        w = yaml.dump({'token': token, keyid: userid}, f)
        f.close()
        return w

    def Yaml_Write_Any(self, path, *data):
        with open(path, mode='w+', encoding='utf-8') as f:
            # 获取到传入多个变量的个数总长度
            a = len(data)
            # 循环遍历多个变量的总数的数值
            for j in range(a):
                # 如果是偶数就跳过,否则打印出来的会重复
                if j % 2 == 0:
                    pass
                # 数据写入yaml文件，k从0开始取偶数，v取奇数
                else:
                    print(j)
                    k = data[j - 1]
                    v = data[j]
                    w = yaml.dump({k: v}, f)
                    return w

    def Yaml_Write_Any_Add(self, path, *data):
        with open(path, mode='a+', encoding='utf-8') as f:
            a = len(data)
            for j in range(a):
                if j % 2 == 0:
                    pass
                else:
                    print(j)
                    k = data[j - 1]
                    v = data[j]
                    w = yaml.dump({k: v}, f)
                    return w

    def Yaml_GetByKey(self, y, k):
        return y[k]

    def Db_MysqlSelect(self, p):
        host = None
        port = None
        username = None
        password = None
        database = None
        sql = None
        if p["host"].__len__() > 0:
            host = p["host"]
        if p["port"].__len__() > 0:
            port = p["port"]
        if p["username"].__len__() > 0:
            username = p["username"]
        if p["password"].__len__() > 0:
            password = p["password"]
        if p["database"].__len__() > 0:
            database = p["database"]
        if p["sql"].__len__() > 0:
            sql = p["sql"]
        db = mysqlHandler.mysql()
        db.host = host
        db.port = port
        db.username = username
        db.password = password
        db.database = database
        cursor = db.getCursor()
        cursor.execute(sql)
        # resDict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        # print(resDict)
        return cursor.fetchall()


    def Db_MysqlExecute(self, p):
        host = None
        port = None
        username = None
        password = None
        database = None
        sql = None
        if p["host"].__len__() > 0:
            host = p["host"]
        if p["port"].__len__() > 0:
            port = p["port"]
        if p["username"].__len__() > 0:
            username = p["username"]
        if p["password"].__len__() > 0:
            password = p["password"]
        if p["database"].__len__() > 0:
            database = p["database"]
        if p["sql"].__len__() > 0:
            sql = p["sql"]
        db = mysqlHandler.mysql()
        db.host = host
        db.port = port
        db.username = username
        db.password = password
        db.database = database
        cursor = db.getCursor()
        cursor.execute(sql)



    def Db_ConfMysqlSelect(self, dbName, sql):
        db = mysqlHandler.mysqlHandler(dbName)
        db.sql = sql
        return db.excuteSelect()

    def Db_ConfMysqlExecute(self, dbName, sql):
        db = mysqlHandler.mysqlHandler(dbName)
        db.sql = sql
        db.excute()

    def Db_SshConfMysqlExecute(self, dbName, sql):
        db = MysqlSshHandler.MysqlSshHandler(dbName)
        db.sql = sql
        db.StartServerWithPassword()
        result =db.SshExcute()
        db.CloseConn()
        return result

    def Db_SshConfRCMysqlExecute(self, dbName, sql):
        db = MysqlSshHandler.MysqlSshHandler(dbName)
        db.sql = sql
        # db.StartServerWithPassword()
        db.StartServerWithPrivateKey()
        result = db.SshExcuteSelectAll()
        db.CloseConn()
        return result

    def Db_SshConfRCMysqlConnect(self, dbName):
        db = MysqlSshHandler.MysqlSshHandler(dbName)
        db.StartServerWithPassword()
        return db

    def Db_SshConfRCMysqlExecuteAfterConnect(self,db , sql):
        db.sql = sql
        result = db.SshExcuteSelectAll()
        return result

    def Db_SshConfRCMysqlClose(self, db ):
        db.CloseConn()



    def Db_RedisGet(self, p):
        host = None
        port = None
        password = None
        db = None
        key = None
        if p["host"].__len__() > 0:
            host = p["host"]
        if p["port"].__len__() > 0:
            port = p["port"]
        if p["password"].__len__() > 0:
            password = p["password"]
        if p["db"].__len__() > 0:
            db = p["db"]
        if p["key"].__len__() > 0:
            key = p["key"]
        redisObj = redisHandler.redisHandler()
        redisObj.host = host
        redisObj.port = port
        redisObj.password = password
        redisObj.db = db
        redisObj.conn = redisObj.getConn()
        result = redisObj.get(key)
        redisObj.close()
        return result

    def Db_RedisSet(self, p):
        host = None
        port = None
        password = None
        db = None
        key = None
        value = None
        if p["host"].__len__() > 0:
            host = p["host"]
        if p["port"].__len__() > 0:
            port = p["port"]
        if p["password"].__len__() > 0:
            password = p["password"]
        if p["db"].__len__() > 0:
            db = p["db"]
        if p["key"].__len__() > 0:
            key = p["key"]
        if p["value"].__len__() > 0:
            value = p["value"]
        redisObj = redisHandler.redisHandler()
        redisObj.host = host
        redisObj.port = port
        redisObj.password = password
        redisObj.db = db
        redisObj.conn = redisObj.getConn()
        redisObj.set(key, value)
        redisObj.close()

    def Db_ConfRedisGet(self,name,k):
        host = readConfig().get_db(name,"host")
        port = readConfig().get_db(name,"port")
        password = readConfig().get_db(name,"password")
        db = readConfig().get_db(name,"db")
        key = k
        redisObj = redisHandler.redisHandler()
        redisObj.host = host
        redisObj.port = port
        redisObj.password = password
        redisObj.db = db
        redisObj.conn = redisObj.getConn()
        result = redisObj.get(key)
        redisObj.close()
        return result

    def Db_ConfRedisSet(self,name,k,v):
        host = readConfig().get_db(name, "host")
        port = readConfig().get_db(name, "port")
        password = readConfig().get_db(name, "password")
        db = readConfig().get_db(name, "db")
        key = k
        value = v
        redisObj = redisHandler.redisHandler()
        redisObj.host = host
        redisObj.port = port
        redisObj.password = password
        redisObj.db = db
        redisObj.conn = redisObj.getConn()
        redisObj.set(key, value)
        redisObj.close()

    def Re_MatchOne(self, str, reStr):
        return re.findall(reStr, str)[0]

    def Re_MatchAll(self, str, reStr):
        return re.findall(reStr, str)

    def Time_UnixTimestamp(self):
        return round(time.time() * 1000)

    def Time_Timestamp(self, s):
        return time.strftime(s, time.localtime())

    def Time_Sleep(self, s):

        time.sleep(int(float(s)))

    def Assert_DictAndDict(self, d1, d2):
        finRe = []
        f = None
        if d1.__len__() >= d2.__len__():
            for k in d1.keys():
                tmpV1 = d1[k]
                tmpV2 = d2[k]
                if type(tmpV1) == list:
                    flag = self.Assert_ListAndList(tmpV1, tmpV2)
                elif type(tmpV1) == dict:
                    flag = self.Assert_DictAndDict(tmpV1, tmpV2)
                else:
                    flag = self.Assert_ObjAndObj(tmpV1, tmpV2)
                finRe.append(flag)
                if flag == True:
                    f = True
                    continue
                else:
                    break
        if f == True:
            return True
        else:
            return False

    def Assert_ObjAndObj(self, o1, o2):
        if o1 == o2:
            return True
        else:
            return False

    def Assert_ListAndList(self, l1, l2):
        if l1 == l2:
            return True
        else:
            return False

    def Assert_BcharInAchar(self, l1, l2):
        A = '%s' % l1
        B = '%s' % l2
        if B in A:
            return True
        else:
            return False

    def Json_oneCharList2json(self,l):
        return json.dumps(l[0])

    def Time_TodayTime(self):
        time = datetime.datetime.today()
        today = time.strftime('%Y-%m-%d')
        return today

    def Time_NowTime(self):
        time = datetime.datetime.now()
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        return now_time

    def Time_Yesterday(self):
        time = datetime.datetime.today()
        yesterday = time - datetime.timedelta(days=1)
        yester_time = yesterday.strftime('%Y-%m-%d')
        return yester_time

if __name__ == '__main__':
    # CommonKeyWord().Db_ConfRedisSet("test_redis","verifyCode_valid_18946788878","12345")
    # print(CommonKeyWord().Db_ConfRedisGet("test_redis","verifyCode_valid_18946788878"))
    p = {'host':'121.41.2.158','port':'6379','password':'','db':'1','key':'abcd'}
    redisget=CommonKeyWord().Db_RedisGet(p)
    print(redisget,type(redisget))