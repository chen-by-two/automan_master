import allure
from ApiLib.shareCenter import shareCenterApi as shareCenter


class TestShareCenter:

    @allure.feature("查询商户信息")
    @allure.severity("normal")
    def partner_detail_by_id(self):
        partner_detail = shareCenter.PartnerDetail()
        partner_detail.headers = {"Content-Type": "application/json;charset=UTF-8"}
        partner_detail.data = {"organizationId": "578"}
        partner_detail_res = partner_detail.excute()
        assert partner_detail_res.text.__contains__("沪宁大药房")
