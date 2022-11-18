import allure
import pytest

from Common.Basic_method.get_yaml import ExtractYaml
from Common.Basic_method.httpbuild import RequestsUtils


@allure.feature("订单单接口测试")
class Test_De:

    @pytest.mark.parametrize('yaml_data', ExtractYaml('ZhuDengHu', 'single_zdh.yaml').get_yaml_value(),
                             ids=['queryTradeOrder', 'goPay','SPECQUERY'])
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_one(self, yaml_data):
        res = RequestsUtils.request(yaml_data['method'], yaml_data['url'], data=yaml_data['data'], key=yaml_data['key'])
        assert res['errno'] == yaml_data['Assert']['errno']
