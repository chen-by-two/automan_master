# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : Haoran
import os
import codecs,json
import configparser


proDir = os.path.dirname(__file__)
configPath = os.path.join(proDir, "../config.ini")

class readConfig:
    def __init__(self):
        fd = open(configPath, 'r', encoding='utf-8')  # chen 添加读取配置文件config.ini时encoding=utf8
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding='utf-8') # chen 添加读取配置文件config.ini时encoding=utf8

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, dbName, name):
        value = self.cf.get(dbName, name)
        return value

    def get_kafka(self, kafkaName ,name):
        value = self.cf.get(kafkaName,name)
        return value

if __name__ == '__main__':
    rdc=readConfig()
    print(rdc.get_kafka('CHEN_TEST_KAFKA_SUN','topic'))
    # host = readConfig().get_db("DATABASE_TEST_cn_uniondrug_middleend_ordercenter","host")
    # print(host)