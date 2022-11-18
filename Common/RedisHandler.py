# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : Haoran
import redis


class redisHandler:
    def __init__(self):
        self.conn = None
        self.host = None
        self.port = None
        self.password = None
        self.db = None
        self.decode_responses = None

    def getConn(self):
        self.conn = redis.Redis(host=self.host, port=self.port, password=self.password, db=self.db, decode_responses = True)
        return self.conn

    def set(self, k, v):
        self.conn.set(k, v)

    def get(self, k):
        return self.conn.get(k)

    def close(self):
        self.conn.close()
