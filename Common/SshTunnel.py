import pymysql
import time
from sshtunnel import SSHTunnelForwarder
import Common.ReadConfig as re


class sshTunnel:
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

        self.Host = None
        self.port = None
        self.server = None
        self.conn = None
        self.User = None
        self.passwd = None
        self.db = None

    def StartServerWithPassword(self):
        print(self.sshHost, self.sshPort, self.sshUsername, self.sshPassword, self.remoteAddress, self.remotePort,
              self.localAddress, self.localPort)
        self.server = SSHTunnelForwarder(
            (self.sshHost, self.sshPort),
            ssh_username=self.sshUsername,
            ssh_password=self.sshPassword,
            remote_bind_address=(self.remoteAddress, self.remotePort),
            local_bind_address=(self.localAddress, self.localPort)
        )
        try:
            self.server.start()
        except:
            self.server.start()

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
        self.sleep(1)
        # print("本地端口是：" + self.server.local_bind_host)

    def StartConn(self):
        print(self.Host, self.localAddress, self.User, self.passwd, self.db)
        self.conn = pymysql.connect(
            host=self.Host,
            port=self.localPort,
            user=self.User,  # 数据库账号
            passwd=self.passwd,  # 数据库密码
            db=self.db) # 可以限定，只访问特定的数据库,否则需要在mysql的查询或者操作语句中，指定好表名
        cur = self.conn.cursor()
        cur.execute("select version()")
        result = cur.fetchone()
        # print("Database version: %s" % result)
        return cur

    def StartConnDB(self):
        self.conn = pymysql.connect(
            host=self.Host,
            port=self.localPort,
            user=self.User,  # 数据库账号
            passwd=self.passwd,  # 数据库密码
            db=self.db,cursorclass=pymysql.cursors.DictCursor)
        cur = self.conn.cursor()
        return cur

    def CloseConn(self):
        self.server.close()
        print("连接关闭成功！")

class MysqlSshHandler(sshTunnel):
    def __init__(self, connName):
        super(MysqlSshHandler, self).__init__()
        self.connName = connName
        self.sshHost = re.readConfig().get_db(connName, "sshhost")
        self.sshPort = int(re.readConfig().get_db(connName, "sshport"))
        self.sshUsername = re.readConfig().get_db(connName, "username")
        self.sshPassword = re.readConfig().get_db(connName, "password")
        self.remoteAddress = re.readConfig().get_db(connName, "remoteAddress")
        self.remotePort = int(re.readConfig().get_db(connName, "remotePort"))
        self.localAddress = re.readConfig().get_db(connName, "localAddress")
        self.localPort = int(re.readConfig().get_db(connName, "localPort"))

        self.Host = re.readConfig().get_db(connName, "host")
        self.Port = (re.readConfig().get_db(connName, "port"))
        self.User = re.readConfig().get_db(connName, "user")
        self.passwd = re.readConfig().get_db(connName, "passwd")
        self.db = re.readConfig().get_db(connName, "db")

        try:
            self.database = re.readConfig().get_db(connName, "database")
        except Exception as e:
            print(e)
        self.sql = None

    def SshExcute(self):
        cursor = self.StartConn()
        cursor.execute(self.sql)
        self.conn.commit()
        return cursor.fetchall()

    def SshExcuteSelectAll(self):
        cursor = self.StartConnDB()
        cursor.execute(self.sql)
        self.conn.commit()
        return cursor.fetchall()

if __name__ == '__main__':
    #sshTunnel().StartServerWithPassword()
    sshTunnel().StartConn()
    sshTunnel().CloseConn()