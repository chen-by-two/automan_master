# -*- coding: utf-8 -*-

import json
from pprint import pprint
import requests
import urllib3
from Common.Basic_method.HttpRequest import HttpRequest
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



class RequestsUtils:
    @staticmethod
    def request(method, url, data=None, parmer=None, key=None):
        urllib3.disable_warnings()
        new_url = HttpRequest.get_host(key) + url
        headers = HttpRequest.get_header(key)
        if key in ['UNIFYCART','CONFIRMCREATE']:
            token = str(HttpRequest.get_tokenwithSSL())
            headers = HttpRequest.get_header(key)
            headers["authorization"] = token
        data = json.dumps(data)
        if method.upper() == 'GET':
            resq = requests.session().get(new_url, parmer=parmer, headers=headers, timeout=30, verify=False)
        elif method.upper() == 'POST':
            resq = requests.session().post(url=new_url, data=data, json=parmer, headers=headers, timeout=30,
                                           verify=False)
        res = resq.json()
        print(f'request_head:------------{resq.headers}')
        print(f'request_url:-------------{resq.url}')
        print(f'request_data:-------------{data}')
        pprint(f'request_json:------------{res}')
        print(f'headers:------------{headers}')
        return res


if __name__ == '__main__':
    res_data = { "operate": "set",
        "key": "verifyCode_valid_13813904992",
        "data": 123456}
    data = json.dumps(res_data)
    print(data)
    res = RequestsUtils.request('POST', '/extTemplate/operate', data=data, key='MSGBACKEND')
    print(res)
