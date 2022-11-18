# -*- coding: utf-8 -*-

from Common.Basic_method.httpbuild import RequestsUtils
import pytest
import allure
from Common.Basic_method.get_yaml import ExtractYaml


@allure.feature("许超测试")
class Test_De:

    @pytest.mark.parametrize('yaml_data', ExtractYaml('xuchao', 'clerk_module.yaml').get_yaml_value(),
                             ids=['assistantRefundCount', 'assistantRefundRiskManage', 'detail', 'ids', 'memberIds',
                                  'new_detail','store_count','storeRoleList','acFinish','account_detail'])
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_one(self, yaml_data):
        res = RequestsUtils.request(yaml_data['method'], yaml_data['url'], data=yaml_data['data'], key=yaml_data['key'])
        assert res['errno'] == yaml_data['Assert']['errno']


if __name__ == '__main__':
    pytest.main()
