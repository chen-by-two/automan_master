# -*- coding: utf-8 -*-

from Common.Basic_method.httpbuild import RequestsUtils
import pytest
import allure
from Common.Basic_method.get_yaml import ExtractYaml


@allure.feature("许超测试")
class Test_De:

    @pytest.mark.parametrize('yaml_data', ExtractYaml('xuchao', 'demo.yaml').get_yaml_value(),
                             ids=['order/confirm/prescription'
                                 , 'order/index'
                                 , 'order/paging'
                                 , 'assistant/get/status'
                                 , 'order/detail'
                                 , '/assistant/assistant/list'
                                 , '/teacher/consult'
                                 , '/teacher/mine'
                                 , '/teacher/displayTab'
                                 , '/teacher/recommend'
                                 , '/project/getProjectAdvertising'
                                 , '/teacher/startChat'
                                 , '/teacher/isShowSwitch'
                                 , '/teacher/existRelate'
                                 , '/release/detail'
                                 , '/evaluate/choice'
                                 , '/teacher/advisorDetail'
                                 , '/teacher/relate'
                                 ,'/member/getPushLink'
                                 ,'/adviser/sendWaitPayNotice'
                                 # ,'/wx/isSub'
                                 ,'/adviser/toHomePushRel'])
    @pytest.mark.flaky(reruns=2, reruns_delay=5)
    def test_one(self, yaml_data):
        res = RequestsUtils.request(yaml_data['method'], yaml_data['url'], data=yaml_data['data'], key=yaml_data['key'])
        assert res['errno'] == yaml_data['Assert']['errno']


if __name__ == '__main__':
    pytest.main()
