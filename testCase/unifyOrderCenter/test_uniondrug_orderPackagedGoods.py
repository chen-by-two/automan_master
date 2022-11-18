# -*- coding: utf-8 -*-

from Common.Basic_method.httpbuild import RequestsUtils
import pytest
import allure
from Common.Basic_method.get_yaml import ExtractYaml
import urllib3
urllib3.disable_warnings()




@allure.feature("实物商品使用优惠权益")
class Test_uniondrugPackagedGoods:
    #公众号登录
    @pytest.mark.parametrize('yaml_data', ExtractYaml('ZhuDengHu', 'packagedGoods.yaml').get_yaml_value()['token_01'])
    def test_one(self, yaml_data):
        res = RequestsUtils.request(yaml_data['method'], yaml_data['url'], data=yaml_data['data'], key=yaml_data['key'])
        print(res)

    @pytest.mark.parametrize('yaml_data', ExtractYaml('ZhuDengHu', 'packagedGoods.yaml').get_yaml_value()['token_02'])
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_two(self, yaml_data):
        global token
        res = RequestsUtils.request(yaml_data['method'], yaml_data['url'], data=yaml_data['data'], key=yaml_data['key'])
        token = res['data']['token']
        print('token:  ', token)

    @pytest.mark.parametrize('yaml_data', ExtractYaml('ZhuDengHu', 'packagedGoods.yaml').get_yaml_value()['unifyproduct'])
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_tree(self, yaml_data):
        res = RequestsUtils.request(yaml_data['method'], yaml_data['url'], data=yaml_data['data'], key=yaml_data['key'])
        assert res['errno'] == yaml_data['Assert']['errno']

    # @pytest.mark.parametrize('yaml_data', ExtractYaml('ZhuDengHu', 'packagedGoods.yaml').get_yaml_value()['count'])
    # @pytest.mark.flaky(reruns=2, reruns_delay=5)
    # def test_four(self, yaml_data):
    #     res = RequestsUtils.request(yaml_data['method'], yaml_data['url'], data=yaml_data['data'], key=yaml_data['key'])
    #     assert res['errno'] == yaml_data['Assert']['errno']


if __name__ == '__main__':
    pytest.main("-s")
