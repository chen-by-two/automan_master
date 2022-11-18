# coding: utf-8
# @author: chen
# @time: 2022/11/15 18:07

import kafka
import ReadConfig


class KafkaHandler(object):
    def __init__(self,kafkaName):
        ck=ReadConfig.readConfig().get_kafka(kafkaName)
        self.topic = ck.topic
        self.bootstrap_servers=ck.bootstrap_servers

    def getConn(self):
        connect = kafka.KafkaConsumer(self.topic,bootstrap_servers=self.bootstrap_servers,auto_offset_reset='earliest')
        return connect



if __name__=='__main__':
    _kafka=KafkaHandler(kafkaName='CHEN_TEST_KAFKA_SUN').getConn()
    for i in _kafka:
        print(i)