# -*- coding: utf-8 -*-
import json
from pprint import pprint

from Common.Basic_method.httpbuild import RequestsUtils
import pytest
import allure
from Common.Basic_method.get_yaml import ExtractYaml




@allure.feature("扫码直付流程")
class Test_Scan_ZF:

    @pytest.mark.parametrize('yaml_data', ExtractYaml('xuchao', 'scan_zf.yaml').get_yaml_value()['token_issue'])
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_ZF(self, yaml_data):
        global token
        res = RequestsUtils.request(yaml_data['method'], yaml_data['url'], data=yaml_data['data'], key=yaml_data['key'])
        token = res['data']['token']
        # print('code:  ',token)

    @pytest.mark.parametrize('yaml_data', ExtractYaml('xuchao', 'scan_zf.yaml').get_yaml_value()['qrcode_scan'])
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_qrcode_scan(self, yaml_data):
        global memberId, requestNo,tid
        yaml_data['data']['code'] = token
        res = RequestsUtils.request(yaml_data['method'], yaml_data['url'], data=yaml_data['data'], key=yaml_data['key'])
        memberId = res['data']['memberId']
        requestNo = eval(res['data']['entrance'])['requestNo']
        tid = res['data']['tid']
        # print('memberId:  ', memberId)
        # print('requestNo:  ', requestNo)
        # print('tid' , tid)

    @pytest.mark.parametrize('yaml_data', ExtractYaml('xuchao', 'scan_zf.yaml').get_yaml_value()['addCart'])
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_addCart(self, yaml_data):
        global waterNo
        yaml_data['data']['scanResult']['code'], \
        yaml_data['data']['scanResult']['memberId'], \
        yaml_data['data']['scanResult']['requestNo'],\
        yaml_data['data']['tid']    = token, memberId, requestNo, tid
        yaml_data['data']['scanResult'] = json.dumps(yaml_data['data']['scanResult'])
        res = RequestsUtils.request(yaml_data['method'], yaml_data['url'], data=yaml_data['data'], key=yaml_data['key'])
        waterNo = res['data']['waterNo']
        # print('waterNo:   ', waterNo)

    @pytest.mark.parametrize('yaml_data', ExtractYaml('xuchao', 'scan_zf.yaml').get_yaml_value()['drugsActivities'])
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_drugsActivities(self, yaml_data):
        yaml_data['data']['memberId'], \
        yaml_data['data']['scanResult']['code'], \
        yaml_data['data']['scanResult']['memberId'], \
        yaml_data['data']['scanResult']['requestNo'] = memberId, token, memberId, requestNo
        RequestsUtils.request(yaml_data['method'], yaml_data['url'], data=yaml_data['data'], key=yaml_data['key'])

    @pytest.mark.parametrize('yaml_data', ExtractYaml('xuchao', 'scan_zf.yaml').get_yaml_value()['createPreOrder'])
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_createPreOrder(self, yaml_data):
        global pre_order_id
        yaml_data['data']['waterNo'], \
        yaml_data['data']['scanResult']['code'], \
        yaml_data['data']['scanResult']['memberId'], \
        yaml_data['data']['scanResult']['requestNo'] = waterNo, token, memberId, requestNo
        yaml_data['data']['scanResult'] = json.dumps(yaml_data['data']['scanResult'])
        res = RequestsUtils.request(yaml_data['method'], yaml_data['url'], data=yaml_data['data'], key=yaml_data['key'])
        pre_order_id = res['data']['pre_order_id']


    @pytest.mark.parametrize('yaml_data', ExtractYaml('xuchao', 'scan_zf.yaml').get_yaml_value()['addJudge'])
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_addJudge(self, yaml_data):
        yaml_data['data']['requestNo'] = pre_order_id
        res = RequestsUtils.request(yaml_data['method'], yaml_data['url'], data=yaml_data['data'], key=yaml_data['key'])
        # print('res-----', res)

    @pytest.mark.parametrize('yaml_data', ExtractYaml('xuchao', 'scan_zf.yaml').get_yaml_value()['applyRx'])
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_applyRx(self, yaml_data):
        yaml_data['data']['requestNo'] = pre_order_id
        res = RequestsUtils.request(yaml_data['method'], yaml_data['url'], data=yaml_data['data'], key=yaml_data['key'])
        # print('res-----', res)



    @pytest.mark.parametrize('yaml_data', ExtractYaml('xuchao', 'scan_zf.yaml').get_yaml_value()['init'])
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_init(self, yaml_data):
        yaml_data['data']['requestNo'] = pre_order_id
        res = RequestsUtils.request(yaml_data['method'], yaml_data['url'], data=yaml_data['data'], key=yaml_data['key'])
        # print('res-----', res)


    @pytest.mark.parametrize('yaml_data', ExtractYaml('xuchao', 'scan_zf.yaml').get_yaml_value()['createOrder'])
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_createOrder(self, yaml_data):
        yaml_data['data']['requestNo'] = pre_order_id
        res = RequestsUtils.request(yaml_data['method'], yaml_data['url'], data=yaml_data['data'], key=yaml_data['key'])
        # print('res-----', res)
        assert res['errno'] == '0'
        assert len(res['data']['mainOrderNo']) > 0


if __name__ == '__main__':
    Test_Scan_ZF().test_createOrder()
