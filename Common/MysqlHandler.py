# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : Haoran
import pymysql
import Common.ReadConfig as re
import yaml


class mysql:
    def __init__(self):
        self.conn = None
        self.host = None
        self.port = None
        self.username = None
        self.password = None
        self.database = None

    def getConn(self):
        print(self.host, self.port, self.username, self.password, self.database)
        if self.database == None:
            self.conn = pymysql.connect(connect_timeout = 20,read_timeout = 60,host=self.host, port=int(self.port), user=self.username, passwd=self.password,
                                        cursorclass=pymysql.cursors.DictCursor)
        else:
            self.conn = pymysql.connect(connect_timeout = 20,read_timeout = 60,host=self.host, port=int(self.port), user=self.username, passwd=self.password,
                                        db=self.database, cursorclass=pymysql.cursors.DictCursor)
        return self.conn

    def getCursor(self):
        return self.getConn().cursor()

    def closeConn(self):
        self.conn.close()


class mysqlHandler(mysql):
    def __init__(self, connName):
        super(mysqlHandler, self).__init__()
        self.connName = connName
        self.host = re.readConfig().get_db(connName, "host")
        self.port = int(re.readConfig().get_db(connName, "port"))
        self.username = re.readConfig().get_db(connName, "username")
        self.password = re.readConfig().get_db(connName, "password")
        try:
            self.database = re.readConfig().get_db(connName, "database")
        except Exception as e:
            print(e)
        self.sql = None
        # print(self.host,self.port,self.username,self.password,self.database)

    def excute(self):
        cursor = self.getCursor()
        cursor.execute(self.sql)
        self.conn.commit()
        # self.closeConn()

    def excuteSelect(self):
        cursor = self.getCursor()
        cursor.execute(self.sql)
        # resDict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        # self.closeConn()
        return cursor.fetchall()


if __name__ == '__main__':
    tt = mysqlHandler("DATABASE_TEST_ALl")
    f = open("/Users/liuhaoran/PycharmProjects/automan/TestFile/HaoRanOnly/lhrtest.yaml", "r", encoding="utf-8")
    tmp = yaml.load(f.read())
    # print(tmp["sql1"])
    # tt.sql = "SELECT captcha FROM `cn_uniondrug_module_data`.`captcha` WHERE `mobile` = '13262567886' AND `status` = '1' order by id LIMIT 0,1;"
    # tt.sql = "SELECT `data` FROM `cn_uniondrug_module_sms`.`message` WHERE mobile = '15005150023' ORDER BY gmtCreated DESC LIMIT 1;"
    tt.sql ="UPDATE `cn_uniondrug_module_data`.`captcha` SET `status` = 0 WHERE `mobile` = 13262567886;"
    # desc = tt.excute().description
    # data_dict = [dict(zip([col[0] for col in desc], row)) for row in tt.excute().fetchall()]
    # print(data_dict)
    # tt.sql = tmp["sql3"]
    # print(tt.excute().description)
    print(tt.excute())
