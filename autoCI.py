# -*- coding: utf-8 -*- 
# @Time : 2022/8/4 3:42 PM 
# @Author : feiyuanfeng 
# @File : autoCI.py 
# @Copyright : uniondrug
import pymysql
import requests
import sys
import time
from sshtunnel import SSHTunnelForwarder


class SshTunnel():
    def __init__(self):
        self.sshHost = None
        self.sshPort = None
        self.sshUsername = None
        self.sshPassword = None
        self.sshPrivateKey = None
        self.remoteAddress = None
        self.remotePort = None
        self.localAddress = None
        self.localPort = None

    def StartServerWithPassword(self):
        self.server = SSHTunnelForwarder(
            (self.sshHost, self.sshPort),
            ssh_username=self.sshUsername,
            ssh_password=self.sshPassword,
            remote_bind_address=(self.remoteAddress, self.remotePort),
            local_bind_address=(self.localAddress, self.localPort)
        )
        self.server.start()
        print('创建ssh连接成功')
        # print("本地端口是：" + self.server.local_bind_host)

    def StartServerWithPrivateKey(self):
        self.server = SSHTunnelForwarder(
            (self.sshHost, self.sshPort),
            ssh_username=self.sshUsername,
            ssh_pkey=self.sshPrivateKey,
            remote_bind_address=(self.remoteAddress, self.remotePort),
            local_bind_address=(self.localAddress, self.localPort)
        )
        self.server.start()
        print('创建ssh连接成功')
        # print("本地端口是：" + self.server.local_bind_host)

    def CloseConn(self):
        self.server.close()
        print('关闭ssh连接成功')

class MysqlHandler():
    def __init__(self):
        self.conn = None
        self.host = None
        self.port = None
        self.username = None
        self.password = None
        self.database = None
        self.sql=None

    def getConn(self):
        if self.database == None:
            self.conn = pymysql.connect(connect_timeout = 20,read_timeout = 60,host=self.host, port=int(self.port), user=self.username, passwd=self.password,
                                        cursorclass=pymysql.cursors.DictCursor)
            print('创建数据库连接成功')
        else:
            self.conn = pymysql.connect(connect_timeout = 20,read_timeout = 60,host=self.host, port=int(self.port), user=self.username, passwd=self.password,
                                        db=self.database, cursorclass=pymysql.cursors.DictCursor)
            print('创建数据库连接成功')
        return self.conn

    def getCursor(self):
        return self.getConn().cursor()

    def closeConn(self):
        self.conn.close()
        print('关闭数据库连接成功')

    def excute(self):
        cursor = self.getCursor()
        cursor.execute(self.sql)
        print('执行SQL:{}'.format(self.sql))
        self.conn.commit()

    def excuteSelect(self):
        cursor = self.getCursor()
        cursor.execute(self.sql)
        print('执行SQL:{}'.format(self.sql))
        res=cursor.fetchall()
        # resDict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        return res

class HttpHandler:

    def __init__(self):
        self.url=None
        self.method=None
        self.headers = None
        self.params=None
        self.data = None
        self.files= None
        self.timeout = None
        self.session=requests.session()

    def send(self,paramdict):
        self.url=paramdict.get('url')
        self.method = paramdict.get('method')
        self.headers = paramdict.get('headers')
        if isinstance(self.headers,str):
            self.headers=eval(self.headers)
        self.data = paramdict.get('data')
        self.timeout = float(paramdict.get('timeout'))
        try:
            response = self.session.request(url=self.url,method=self.method,headers=self.headers,params=self.params,data=self.data,timeout=self.timeout)
            return response
        except TimeoutError:
            print("Time out!")
            return None

class autoCI:
    def __init__(self):
        self.mysqlhd = MysqlHandler()
        self.sshtunnel = SshTunnel()

        self.mysqlhd.host='127.0.0.1'
        self.mysqlhd.port=23055
        self.mysqlhd.username='rctest_iud'
        self.mysqlhd.password='tset@987#gurdnoinu'

        self.sshtunnel.sshHost = '47.110.156.126'
        self.sshtunnel.sshPort = 60022
        self.sshtunnel.sshUsername = 'fei.yuanfeng'
        self.sshtunnel.sshPassword = 'f13952776769'
        self.sshtunnel.remoteAddress = 'rm-bp1e8moojdesoq5dy.mysql.rds.aliyuncs.com'
        self.sshtunnel.remotePort = 3306
        self.sshtunnel.localAddress = '127.0.0.1'
        self.sshtunnel.localPort = 23055
        self.sshtunnel.StartServerWithPassword()

if __name__ == '__main__':
    module_name=sys.argv[1]
    autoci=autoCI()
    autoci.mysqlhd.sql="select b.id,b.autotest_url,b.last_autotest_time from `cn_ud_bkd_autotest`.`ci_module` a  LEFT JOIN `cn_ud_bkd_autotest`.`ci_sys`  b on a.sys_id=b.id where a.module_name='{}'".format(module_name)
    res=autoci.mysqlhd.excuteSelect()
    print(res.__len__())
    if res.__len__()>0:
        print('------输入项目模块有自动化测试任务，开始检测是否近期回归过--------')
        autotest_url=res[0].get('autotest_url')
        last_autotest_time=int(res[0].get('last_autotest_time'))
        id=int(res[0].get('id'))
        now=int(time.time())
        if (now-last_autotest_time)>600:
            print('------近期未回归，开始执行自动化回归-------')
            paramdict={'url':autotest_url,'method':'get','timeout':'10'}
            HttpHandler().send(paramdict)
            autoci.mysqlhd.sql="update `cn_ud_bkd_autotest`.`ci_sys` set last_autotest_time={} where id={} ".format(now,id)
            autoci.mysqlhd.excute()
        else:
            print('------近期已回归，退出-------')
    autoci.mysqlhd.closeConn()
    autoci.sshtunnel.CloseConn()

