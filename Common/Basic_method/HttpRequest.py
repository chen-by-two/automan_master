# -*- coding: utf-8 -*-
from testCase.unifyOrderCenter.test_uniondrug_attachInfo import Test_unifyOrderintegralselfPaid

import KeyWordDriver.CommonKeyWord as ckw



class HttpRequest:

    token_dict = {}

    @staticmethod
    def get_host(key=None):
        if key.upper() == 'DSTORE':
            host = 'https://pm-dstore-member.uniondrug.net'
        elif key.upper() == 'TAKE':
            host = 'https://take-backend.uniondrug.net'
        elif key.upper() == 'APP':
            host = 'https://app.uniondrug.net'
        elif key.upper() == 'CLERK':
            host = 'https://clerk.module.uniondrug.net'
        elif key.upper() == 'PHARMACIST':
            host = 'https://ps-dstore-pharmacist.uniondrug.net'
        elif key.upper() == 'TOKEN':
            host = 'http://token.module.turboradio.cn'
        elif key.upper() == 'TURAPP':
            host = 'http://app.turboradio.cn'
        elif key.upper() == 'TURPM':
            host = 'https://pm-dpsp-tc-order.turboradio.cn'
        elif key.upper() == 'ES':
            host = 'https://ps-dstore-es.uniondrug.net'
        elif key.upper() == 'DRUGSTORE':
            host = 'https://drugstore.user.backend.uniondrug.net'
        elif key.upper() in ['UNIFYCART','CONFIRMCREATE','SPECQUERY']:
            host = 'https://wx.uniondrug.net'
        elif key.upper() == 'MSGBACKEND':
            host = 'http://msg.backend.uniondrug.net'
        elif key.upper() == 'LOGIN':
            host = 'https://auth-backend.uniondrug.net'
        elif key in ['queryTradeOrder','goPay']:
            host = 'http://java.pmc.wechat.uniondrug.net'
        return host


    @staticmethod
    def get_tokenwithSSL():
        return Test_unifyOrderintegralselfPaid.test_drug_login(1)

    @staticmethod
    def get_token(key=None):

        if key == 'DSTORE':
            if 'DSTORE' not in HttpRequest.token_dict:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                sqlToken = "SELECT token FROM `cn_uniondrug_backend_auth`.`member_token` WHERE `memberId` = '16235631' AND `channel` = 'mobile'  LIMIT 1 "
                newToken = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_uniondrug_module_sms", sqlToken)[0]['token']
                token = f'Bearer {newToken}'
                HttpRequest.token_dict['DSTORE'] = token
                return token
            else:
                return HttpRequest.token_dict['DSTORE']


        elif key.upper() == 'TURPM':
            if 'TURPM' not in HttpRequest.token_dict:
                sqlToken = "SELECT token FROM `cn_uniondrug_backend_auth`.`member_token` WHERE `memberId` = '15970572' AND `channel` = 'assistant'  LIMIT 1 "
                newToken = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", sqlToken)[0]['token']
                token = f'Bearer {newToken}'
                HttpRequest.token_dict['TURPM'] = token
                return token
            else:
                return HttpRequest.token_dict['TURPM']



    @staticmethod
    def get_header(key=None):
        if key.upper() == 'DSTORE':
            token = HttpRequest().get_token(key)
            header = {
                "content-type": "application/json",
                "authorization": token}
        elif key.upper() == 'TAKE':
            header = {
                "content-type": "application/json",
                "authorization": "Bearer ab6d6cc9-075e-419b-9b3e-af4864606e5d"
            }
            #cn_uniondrug_backend_app.token
        elif key.upper() == 'APP' or key.upper() == 'DRUGSTORE':
            header = {
                "content-type": "application/json",
                "authorization": "Bearer ab6d6cc9-075e-419b-9b3e-af4864606e5d"
            }
        elif key.upper() == 'TURAPP':
            header = {
                "content-type": "application/json",
                "authorization": "Bearer 7786f102-3c40-4f34-ae8d-e904cf38c314",
                "version": "5.4.2.2"
            }
        elif key.upper() == 'TURPM':
            token = HttpRequest().get_token(key)
            header = {
                "content-type": "application/json",
                "authorization": token
            }
        else:
            header = {
                "content-type": "application/json"
            }

        return header


if __name__ == '__main__':
    sqlToken = "SELECT token FROM `cn_uniondrug_backend_auth`.`member_token` WHERE `memberId` = '16235631' AND `channel` = 'mobile'  LIMIT 1 "
    newToken = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_uniondrug_module_data", sqlToken)[0]['token']
    token = f'Bearer {newToken}'
