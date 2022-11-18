# -*- coding: utf-8 -*- 
# @Time : 2022/7/5 7:35 PM 
# @Author : feiyuanfeng 
# @File : DingdingHandler.py 
# @Copyright : uniondrug
import time
import hmac
import hashlib
import base64
import json
import urllib.parse

import requests


class DingDingHandler(object):
    def __init__(self, secret=None, url=None):
        """
        :param secret: 安全设置的加签秘钥
        :param url: 机器人没有加签的WebHook_url
        """
        if secret is not None:
            secret = secret
        else:
            secret = 'SECa0ab7f3ba9742c0*********'  # 加签秘钥
        if url is not None:
            url = url
        else:
            url = "https://oapi.dingtalk.com/robot/send?access_token=1554a3dd1e748*********"  # 无加密的url

        timestamp = round(time.time() * 1000)  # 时间戳
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))  # 最终签名

        self.webhook_url = url + '&timestamp={}&sign={}'.format(timestamp, sign)  # 最终url，url+时间戳+签名

    def send_meassage(self, data):
        """
        发送消息至机器人对应的群
        :param data: 发送的内容
        :return:
        """
        header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }
        send_data = json.dumps(data)  # 将字典类型数据转化为json格式
        send_data = send_data.encode("utf-8")  # 编码为UTF-8格式
        resp = requests.post(url=self.webhook_url, data=send_data, headers=header)  # 发送请求
        print(resp.text)  # 打印返回的结果


# if __name__ == '__main__':
#     my_secret = 'SEC0fceaceae11be82efe82e2dcc8f256bd9054af15374b65d3893867bcc69ef8f4'
#     my_url = 'https://oapi.dingtalk.com/robot/send?access_token=3cb5ac41ec444dee625ced38926be1139cbf79d2d328e3a48f866981323c50e9'
#     my_data = {
#         "msgtype": "markdown",
#         "markdown": {"title": "测试markdown样式",
#                      "text": "# 一级标题 \n## 二级标题 \n> 引用文本  \n**加粗**  \n*斜体*  \n[百度链接](https://www.baidu.com) "
#                              "\n![草莓](https://dss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1906469856,4113625838&fm=26&gp=0.jpg) "
#                              "\n- 无序列表 \n1.有序列表"},
#         "at": {
#             "atMobiles": [13072581629],
#             "isAtAll": False}  # 是否@所有人
#     }
#
#     dingding = DingDingHandler(secret=my_secret, url=my_url)
#     dingding.send_meassage(my_data)
