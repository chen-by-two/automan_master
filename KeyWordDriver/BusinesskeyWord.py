# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : Haoran
import json, yaml
import Common.JsonTools as jsonTools
import Common.MysqlHandler as mysqlHandler
import KeyWordDriver.CommonKeyWord as ckw
import ApiLib.goodsCenter.goodsCenterApi as goodCenter
import ApiLib.newCleanCenter.newCleanCenterApi as newCleanCenter
import ApiLib.coinService.coinServiceApi as coinService
import ApiLib.financeReplace.financeReplaceApi as financeReplace
import ApiLib.orderCenter.orderCenterApi as orderCenter
import ApiLib.equityCenter.equityCenterApi as equityCenter
import ApiLib.auth.authApi as auth
import ApiLib.finance.financeApi as finance
import ApiLib.financeStatement.financeStatementApi as financeStatement
import ApiLib.billCenter.billCenterApi as billCenter
import ApiLib.insure.insureApi as insure
import ApiLib.financeBusiness.financeBusinessApi as financeBusiness
import ApiLib.thePublic.thePublicApi as thePublicApi
import ApiLib.financeData.financeDataApi as financeData
import ApiLib.compensate.compensateApi as compensate
from ApiLib.AssistantApprove import ApproveApi
from ApiLib.BusinessServices import BusinessServicesApi
from ApiLib.customerCenter import customerCenterApi
from ApiLib.drugapp import drugappApi
from ApiLib.equityCenter import equityCenterApi
from ApiLib.goodsCenter import goodsCenterApi
from ApiLib.insure import insureApi
from ApiLib.newCleanCenter import newCleanCenterApi
from ApiLib.coinService import coinServiceApi
from ApiLib.financeReplace import financeReplaceApi
from ApiLib.orderCenter import orderCenterApi
from ApiLib.promoteCenter import promoteCenterApi
from ApiLib.recommend import recommendApi
from ApiLib.searchCenter import searchCenterApi
from ApiLib.stagnation import stagnationApi
from ApiLib.tag import tagApi
from ApiLib.unifyorder import unifyorderApi
from ApiLib.userCenter import userCenterApi
from ApiLib.backendApp import backendApi
from ApiLib.creditCenter import creditCenterApi
from ApiLib.assistantapp import assistantappApi
from ApiLib.unifyOrderCenter import unifyOrderCenterApi
from ApiLib.im import imApi, im_group_chat
from ApiLib.auth import authApi
from ApiLib.finance import financeApi
from ApiLib.activity import activityApi
from ApiLib.im import imApi
from ApiLib.financeBusiness import financeBusinessApi
from ApiLib.financeStatement import financeStatementApi
from ApiLib.billCenter import billCenterApi
from ApiLib.financeData import financeDataApi
from ApiLib.O2OPlaceTheOrder import O2OPlaceTheOrderApi
# from ApiLib.DrugStoreTreasure import DrugstoreApi
from ApiLib.compensate import compensateApi

def newCleanCenterApi_goodsInsert(p, t):
    met = newCleanCenter.goodsInsert()
    return __defult(met, p, t)

def newCleanCenterApi_cleanOrderMainOrderSuccessPay(p, t):
    met = newCleanCenter.cleanOrderMainOrderSuccessPay()
    return __defult(met, p, t)

def newCleanCenterApi_healthOrderReceived(p, t):
    met = newCleanCenter.healthOrderReceived()
    return __defult(met, p, t)

def newCleanCenterApi_orderlistenOrderSnapshotFinishPage(p, t):
    met = newCleanCenter.orderlistenOrderSnapshotFinishPage()
    return __defult(met, p, t)

def newCleanCenterApi_orderlistenOrderSnapshotOrderPage(p, t):
    met = newCleanCenter.orderlistenOrderSnapshotOrderPage()
    return __defult(met, p, t)

def newCleanCenterApi_orderlistenCleanOrder(p, t):
    met = newCleanCenter.orderlistenCleanOrder()
    return __defult(met, p, t)

def financeBusiness_transactionOrdersPaging(p, t):
    met = financeBusiness.transactionOrdersPaging()
    return __defult(met, p, t)

def financeBusiness_userUuid(p, t):
    met = financeBusiness.userUuid()
    return __defult(met, p, t)

def coinServiceApi_mbsAuditCenter(p, t):
    met = coinService.mbsAuditCenter()
    return __defult(met, p, t)

def coinServiceApi_connectTransferCallBack(p, t):
    met = coinService.connectTransferCallBack()
    return __defult(met, p, t)

def coinServiceApi_fundAccountGetByHolder(p, t):
    met = coinService.fundAccountGetByHolder()
    return __defult(met, p, t)

def coinServiceApi_bankChaimPageByPayer(p, t):
    met = coinService.bankChaimPageByPayer()
    return __defult(met, p, t)

def newCleanCenterApi_erpUpdateErpSn(p, t):
    met = newCleanCenter.erpUpdateErpSn()
    return __defult(met, p, t)

def newCleanCenterApi_cleanRenewEquityMbs(p, t):
    met = newCleanCenter.cleanRenewEquityMbs()
    return __defult(met, p, t)

def newCleanCenterApi_replaceOrderSuccess(p, t):
    met = newCleanCenter.replaceOrderSuccess()
    return __defult(met, p, t)

def newCleanCenterApi_cleanRdxMbs(p, t):
    met = newCleanCenter.cleanRdxMbs()
    return __defult(met, p, t)


def newCleanCenterApi_cleanOrderFinish(p, t):
    met = newCleanCenter.cleanOrderFinish()
    return __defult(met, p, t)


# 公共数据-商户明细
def financeDataApi_workerSystemPaging(p, t):
    met = financeData.workerSystemPaging()
    print("测试URL", met.host + met.path)
    print("测试data", met.data)
    return __defult(met, p, t)

def financeDataApi_partnerDirectorAuditListing(p, t):
    met = financeData.partnerDirectorAuditListing()
    print("测试URL", met.host + met.path)
    print("测试data", met.data)
    return __defult(met, p, t)

def financeDataApi_partnerDiscountDetailByTime(p, t):
    met = financeData.partnerDiscountDetailByTime()
    print("测试URL", met.host + met.path)
    print("测试data", met.data)
    return __defult(met, p, t)

def financeDataApi_dictDetailByName(p, t):
    met = financeData.dictDetailByName()
    print("测试URL", met.host + met.path)
    print("测试data", met.data)
    return __defult(met, p, t)

def financeDataApi_partnerDetail(p, t):
    met = financeData.partnerDetail()
    print("测试URL", met.host + met.path)
    print("测试data", met.data)
    return __defult(met, p, t)

# 公共数据-换新服务协议
def financeDataApi_partnerRenewal(p, t):
    met = financeData.partnerRenewal()
    print("测试URL", met.host + met.path)
    print("测试data", met.data)
    return __defult(met, p, t)

# 公共数据-商品税收分类编码信息
def financeDataApi_taxClassification(p, t):
    met = financeData.taxClassification()
    print("测试URL", met.host + met.path)
    print("测试data", met.data)
    return __defult(met, p, t)

# 公共数据-用户管理用户信息
def financeDataApi_companyWorker(p, t):
    met = financeData.companyWorker()
    print("测试URL", met.host + met.path)
    print("测试data", met.data)
    return __defult(met, p, t)

# 公共数据-用户信息
def financeDataApi_workerExist(p, t):
    met = financeData.workerExist()
    print("测试URL", met.host + met.path)
    print("测试data", met.data)
    return __defult(met, p, t)

# 公共数据-商户结算配置
def financeDataApi_partnerSetting(p, t):
    met = financeData.partnerSetting()
    return __defult(met, p, t)

# 公共数据-版本控制信息
def financeDataApi_versionControl(p, t):
    met = financeData.versionControl()
    return __defult(met, p, t)

# 公共数据-核算单位的商业关系
def financeDataApi_unitRelationship(p, t):
    met = financeData.unitRelationship()
    return __defult(met, p, t)

# 公共数据-核算单位的基础信息和票据信息
def financeDataApi_unitBillInfo(p, t):
    met = financeData.unitBillInfo()
    return __defult(met, p, t)

def financeDataApi_merchantInfo(p, t):
    met = financeData.merchantInfo()
    return __defult(met, p, t)


def financeDataApi_partnerBillInfo(p, t):
    met = financeData.partnerBillInfo()
    return __defult(met, p, t)

def financeDataApi_vipDetail(p, t):
    met = financeData.vipDetail()
    return __defult(met, p, t)

def financeDataApi_partnerTodoList(p, t):
    met = financeData.partnerTodoList()
    return __defult(met, p, t)

def financeDataApi_insurerInfo(p, t):
    met = financeData.insurerInfo()
    return __defult(met, p, t)

# 权益中心项目列表
def compensateApi_projectList(p, t):
    met = compensate.projectList()
    return __defult(met, p, t)

def compensateApi_guaranteesActive(p, t):
    met = compensate.guaranteesActive()
    return __defult(met, p, t)

def compensateApi_groupSum(p, t):
    met = compensate.groupSum()
    return __defult(met, p, t)

def financeReplaceApi_replaceQueryJudeZghItem(p, t):
    met = financeReplace.replaceQueryJudeZghItem()
    return __defult(met, p, t)


def financeReplaceApi_replaceReplaceOne(p, t):
    met = financeReplace.replaceReplaceOne()
    return __defult(met, p, t)


def financeBusinessApi_systemRoleWorkertree(p, t):
    met = financeBusiness.systemRoleWorkertree()
    return __defult(met, p, t)

def financeBusinessApi_subscribeStatus(p, t):
    met = financeBusiness.subscribeStatus()
    return __defult(met, p, t)

def financeBusinessApi_applyOnlineUnitDetail(p, t):
    met = financeBusiness.applyOnlineUnitDetail()
    return __defult(met, p, t)

# def financeBusinessApi_wechatSubscribeStatus(p, t):
#     met = financeBusiness.wechatSubscribeStatus()
#     return __defult(met, p, t)

def financeBusinessApi_organizeFinanceAccountUnitDetail(p, t):
    met = financeBusiness.organizeFinanceAccountUnitDetail()
    return __defult(met, p, t)


def financeBusinessApi_announcementPartnerCountUnread(p, t):
    met = financeBusiness.announcementPartnerCountUnread()
    return __defult(met, p, t)


def financeBusinessApi_directPayoutStatementPaging(p, t):
    met = financeBusiness.directPayoutStatementPaging()
    return __defult(met, p, t)


def financeBusinessApi_payoutBillPaging(p, t):
    met = financeBusiness.payoutBillPaging()
    return __defult(met, p, t)

def financeBusinessApi_applyVipDetail(p, t):
    met = financeBusiness.applyVipDetail()
    return __defult(met, p, t)

def financeBusinessApi_announcementPartnerAvailable(p, t):
    met = financeBusiness.announcementPartnerAvailable()
    return __defult(met, p, t)

def financeBusinessApi_announcementPartnerPaging(p, t):
    met = financeBusiness.announcementPartnerPaging()
    return __defult(met, p, t)

def financeBusinessApi_businessCenterVersionDetail(p, t):
    met = financeBusiness.businessCenterVersionDetail()
    return __defult(met, p, t)


def financeStatementApi_mqAfterDirectCleaned(p, t):
    met = financeStatement.mqAfterDirectCleaned()
    return __defult(met, p, t)

def financeStatementApi_mqAfterDirectGoodsReplaced(p, t):
    met = financeStatement.mqAfterDirectGoodsReplaced()
    return __defult(met, p, t)

def financeStatementApi_mqAfterDirectGoodsReplaced(p, t):
    met = financeStatement.mqAfterDirectGoodsReplaced()
    return __defult(met, p, t)

def financeStatementApi_directEquityClaimSync(p, t):
    met = financeStatement.directEquityClaimSync()
    return __defult(met, p, t)


def billCenterApi_directStatementCreate(p, t):
    met = billCenter.directStatementCreate()
    return __defult(met, p, t)


def billCenterApi_directStatementAuditAccept(p, t):
    met = billCenter.directStatementAuditAccept()
    return __defult(met, p, t)

def billCenterApi_directPayoutStatementPaging(p, t):
    met = billCenter.directPayoutStatementPaging()
    return __defult(met, p, t)


def billCenterApi_payoutBillPaging(p, t):
    met = billCenter.payoutBillPaging()
    return __defult(met, p, t)

def billCenterApi_financePayoutBillPaging(p, t):
    met = billCenter.financePayoutBillPaging()
    return __defult(met, p, t)

def billCenterApi_mbsBillSaleSave(p, t):
    met = billCenter.mbsBillSaleSave()
    return __defult(met, p, t)

def billCenterApi_invoicePage(p, t):
    met = billCenter.invoicePage()
    return __defult(met, p, t)


def coinServiceApi_paymentCreate(p, t):
    met = coinService.paymentCreate()
    return __defult(met, p, t)


def newCleanCenterApi_OpenQueryVas(p, t):
    met = newCleanCenter.openQueryVas()
    return __defult(met, p, t)


def insureApi_mbsOrderClearing(p, t):
    met = insure.mbsOrderClearing()
    return __defult(met, p, t)

def insureApi_mbsGoodsReplace(p, t):
    met = insure.mbsGoodsReplace()
    return __defult(met, p, t)

def insureApi_mbsOrderAttach(p, t):
    met = insure.mbsOrderAttach()
    return __defult(met, p, t)

def insureApi_mbsClaimSattleClaim(p, t):
    met = insure.mbsClaimSattleClaim()
    return __defult(met, p, t)

def goodCenterApi_SpuQuery(p, t):
    met = goodCenter.spuQuery()
    return __defult(met, p, t)


def goodCenterApi_UnifyproductDetails(p, t):
    met = goodCenter.UnifyproductDetails()
    return __defult(met, p, t)


def goodCenterApi_UnifyproductBuyLimit(p, t):
    met = goodCenter.UnifyproductBuyLimit()
    return __defult(met, p, t)


def orderCenterApi_UnifyorderConfirmCreate(p, t):
    met = orderCenter.UnifyorderConfirmCreate()
    return __defult(met, p, t)


def orderCenterApi_UnifyorderConfirmInvoiceChange(p, t):
    met = orderCenter.UnifyorderConfirmInvoiceChange()
    return __defult(met, p, t)


def orderCenterApi_UnifyorderOrderCreate(p, t):
    met = orderCenter.UnifyorderOrderCreate()
    return __defult(met, p, t)


def orderCenterApi_UnifyorderCashierPayModes(p, t):
    met = orderCenter.UnifyorderCashierPayModes()
    return __defult(met, p, t)


def orderCenterApi_UnifyorderOrderDetail(p, t):
    met = orderCenter.UnifyorderOrderDetail()
    return __defult(met, p, t)


def orderCenterApi_UnifyorderCashierCheck(p, t):
    met = orderCenter.UnifyorderCashierCheck()
    return __defult(met, p, t)


def orderCenterApi_UnifyorderCashierCreate(p, t):
    met = orderCenter.UnifyorderCashierCreate()
    return __defult(met, p, t)


def equityCenterApi_UnifyorderMemberEquityQuery(p, t):
    met = equityCenter.UnifyorderMemberEquityQuery()
    return __defult(met, p, t)


def equityCenterApi_UnifyorderConfirmEquityChange(p, t):
    met = equityCenter.UnifyorderConfirmEquityChange()
    return __defult(met, p, t)


def equityCenterApi_RedeemAdd(p, t):
    met = equityCenter.RedeemAdd()
    return __defult(met, p, t)


def authApi_LoginSendCaptcha(p, t):
    met = auth.LoginSendCaptcha()
    return __defult(met, p, t)


def authApi_SmsSend(p, t):
    met = auth.SmsSend()
    return __defult(met, p, t)


def authApi_DdMobilelogin(p, t):
    met = auth.DdMobilelogin()
    return __defult(met, p, t)


def authApi_Ddlogin(p, t):
    met = auth.Ddlogin()
    return __defult(met, p, t)


def authApi_ThePublicLoginSendCaptcha(p, t):
    met = auth.ThePublicLoginSendCaptcha()
    return __defult(met, p, t)


def authApi_ThePublicLoginLogin(p, t):
    met = auth.ThePublicLoginLogin()
    return __defult(met, p, t)


def authApi_GetCaptcha(p):
    db = mysqlHandler.mysqlHandler(p["dbName"])
    f = open("/Users/liuhaoran/PycharmProjects/automan/TestFile/HaoRanOnly/lhrtest.yaml", "r", encoding="utf-8")
    tmp = yaml.load(f.read())
    f.close()
    oo = tmp["getLoginCaptcha"].replace("15005150023", p["mobile"])
    print(oo)
    db.sql = oo
    ww = db.excute().fetchall()
    print(ww[0][0])
    print(type(ww[0][0]))
    qq = ckw.CommonKeyWord().json_GetJsonValue(json.loads(ww[0][0]), [["sms", "code"]])
    print(qq)
    return qq


def authApi_LoginLogin(p, t):
    met = auth.LoginLogin()
    return __defult(met, p, t)


def financeApi_PasswordLogin(p, t):
    met = finance.PasswordLogin()
    return __defult(met, p, t)


def financeApi_UserPasswordlogin(p, t):
    met = finance.UserPasswordlogin()
    return __defult(met, p, t)


def financeApi_DdMobilelogin(p, t):
    met = finance.DdMobilelogin()
    return __defult(met, p, t)


def financeApi_Ddlogin(p, t):
    met = finance.Ddlogin()
    return __defult(met, p, t)



def thePublicApi_ThePublicLoginSendCaptcha(p, t):
    met = thePublicApi.ThePublicLoginSendCaptcha()
    return __defult(met, p, t)


def thePublicApi_ThePublicLoginLogin(p, t):
    met = thePublicApi.ThePublicLoginLogin()
    return __defult(met, p, t)


def thePublicApi_VMemberDetail(p, t):
    met = thePublicApi.VMemberDetail()
    return __defult(met, p, t)


def thePublicApi_VProjectUserCheck(p, t):
    met = thePublicApi.VProjectUserCheck()
    return __defult(met, p, t)


def thePublicApi_VProjectUserDetail(p, t):
    met = thePublicApi.VProjectUserDetail()
    return __defult(met, p, t)


def thePublicApi_VEquityNewActivate(p, t):
    met = thePublicApi.VEquityNewActivate()
    return __defult(met, p, t)


def thePublicApi_VWxUserinfo(p, t):
    met = thePublicApi.VEquityNewActivate()
    return __defult(met, p, t)


'''
haoran统一交易根据权益卡id提取信息
勿动    1000690099471315
'''


def getRsourceInfo_byCardNo(l, cardNo):
    for card in l:
        print(jsonTools.getJsonValue(card, [["rsourceId"]]), cardNo)
        if jsonTools.getJsonValue(card, [["rsourceId"]]) == str(cardNo):
            return card
    return None


def thePublicApi_ExtTemplateOperate(p, t):
    met = thePublicApi.ExtTemplateOperate()
    return __defult(met, p, t)


def thePublicApi_VProjectUserCondition(p, t):
    met = thePublicApi.VProjectUserCondition()
    return __defult(met, p, t)


def thePublicApi_VProjectUserGroup(p, t):
    met = thePublicApi.VProjectUserGroup()
    return __defult(met, p, t)


def equityCenter_RedeemDisable(p, t):
    met = equityCenter.RedeemDisable()
    return __defult(met, p, t)


def __defult(met, p, t):
    if p["header"].__len__() > 0:
        met.headers = p["header"]
    if p["parma"].__len__() > 0:
        met.params = p["parma"]
    if p["data"].__len__() > 0:
        met.data = p["data"]
    if p["env"].__len__() > 0:
        met.changeEnv(p["env"])
    res = met.excute()
    if t == "text":
        return res.text
    if t == "dict":
        return json.loads(res.text)
    if t == "code":
        return res.status_code


if __name__ == '__main__':
    pass


def customerCenterApi_PromoteSendcard(p, t):
    met = customerCenterApi.PromoteSendcard()
    return __defult(met, p, t)


def customerCenterApi_VoucherCreate(p, t):
    met = customerCenterApi.VoucherCreate()
    return __defult(met, p, t)


def drugappApi_AssistantCreate(p, t):
    met = drugappApi.AssistantCreate()
    return __defult(met, p, t)


def drugappApi_V4CodePicture(p, t):
    met = drugappApi.V4CodePicture()
    return __defult(met, p, t)


def drugappApi_V4CodeVerify(p, t):
    met = drugappApi.V4CodeVerify()
    return __defult(met, p, t)


def drugappApi_V4UsersSmslogin(p, t):
    met = drugappApi.V4UsersSmslogin()
    return __defult(met, p, t)


def equityCenterApi_RedeemDisable(p, t):
    met = equityCenterApi.RedeemDisable()
    return __defult(met, p, t)


def goodsCenterApi_SpuQuery(p, t):
    met = goodsCenterApi.SpuQuery()
    return __defult(met, p, t)


def goodsCenterApi_UnifyproductDetails(p, t):
    met = goodsCenterApi.UnifyproductDetails()
    return __defult(met, p, t)


def goodsCenterApi_UnifyproductBuyLimit(p, t):
    met = goodsCenterApi.UnifyproductBuyLimit()
    return __defult(met, p, t)


def orderCenterApi_paging(p, t):
    met = orderCenterApi.paging()
    return __defult(met, p, t)


def orderCenterApi_NeworderOrdercancelsub(p, t):
    met = orderCenterApi.NeworderOrdercancelsub()
    return __defult(met, p, t)


def recommendApi_AdvisorListRecommendAdv(p, t):
    met = recommendApi.AdvisorListRecommendAdv()
    return __defult(met, p, t)


def searchCenterApi_WordSuggesterSuggester(p, t):
    met = searchCenterApi.WordSuggesterSuggester()
    return __defult(met, p, t)


def searchCenterApi_GoodsSearchSearchGoodsAll(p, t):
    met = searchCenterApi.GoodsSearchSearchGoodsAll()
    return __defult(met, p, t)


def searchCenterApi_GoodsSearchSearchGoodsByTradeCode(p, t):
    met = searchCenterApi.GoodsSearchSearchGoodsByTradeCode()
    return __defult(met, p, t)


def searchCenterApi_GoodsSearchSearchGoodsGeo(p, t):
    met = searchCenterApi.GoodsSearchSearchGoodsGeo()
    return __defult(met, p, t)


def searchCenterApi_OtoManageSearch(p, t):
    met = searchCenterApi.OtoManageSearch()
    return __defult(met, p, t)


def searchCenterApi_GoodsSearchCorrectSearchContent(p, t):
    met = searchCenterApi.GoodsSearchCorrectSearchContent()
    return __defult(met, p, t)


def searchCenterApi_QueryGoodsQueryGoodsBaseInfo(p, t):
    met = searchCenterApi.QueryGoodsQueryGoodsBaseInfo()
    return __defult(met, p, t)


def searchCenterApi_SkuQuery(p, t):
    met = searchCenterApi.SkuQuery()
    return __defult(met, p, t)


def searchCenterApi_Sku(p, t):
    met = searchCenterApi.Sku()
    return __defult(met, p, t)


def searchCenterApi_SkuSimple(p, t):
    met = searchCenterApi.SkuSimple()
    return __defult(met, p, t)


def searchCenterApi_GoodsSearchSearchUnify(p, t):
    met = searchCenterApi.GoodsSearchSearchUnify()
    return __defult(met, p, t)


def searchCenterApi_GoodsSearchSearch(p, t):
    met = searchCenterApi.GoodsSearchSearch()
    return __defult(met, p, t)


def searchCenterApi_GoodsSearchSearchDtpGoods(p, t):
    met = searchCenterApi.GoodsSearchSearchDtpGoods()
    return __defult(met, p, t)


def tagApi_UserPackageBaseCreate(p, t):
    met = tagApi.UserPackageBaseCreate()
    return __defult(met, p, t)


def tagApi_UserPackageHighlevelCreate(p, t):
    met = tagApi.UserPackageHighlevelCreate()
    return __defult(met, p, t)


def tagApi_UserPackageUsersGet(p, t):
    met = tagApi.UserPackageUsersGet()
    return __defult(met, p, t)


def tagApi_MemberWideInsertMemberPackage(p, t):
    met = tagApi.MemberWideInsertMemberPackage()
    return __defult(met, p, t)


def tagApi_OrderWideInsertOrderPackage(p, t):
    met = tagApi.OrderWideInsertOrderPackage()
    return __defult(met, p, t)


def tagApi_UserPackageDelete(p, t):
    met = tagApi.UserPackageDelete()
    return __defult(met, p, t)


def tagApi_UserPackageListMember(p, t):
    met = tagApi.UserPackageListMember()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderConfirmCreate(p, t):
    met = unifyorderApi.UnifyorderConfirmCreate()
    return __defult(met, p, t)


# RC创建预订单接口
def unifyorderApi_UnifyorderConfirmCreateNew(p, t):
    met = unifyorderApi.UnifyorderConfirmCreateNew()
    return __defult(met, p, t)


# rc 查询预订单接口
def unifyorderApi_UnifyorderApi_UnifyorderqueryMulti(p, t):
    met = unifyorderApi.UnifyorderqueryMulti()
    return __defult(met, p, t)


# rc 查询权益卡id
def unifyorderApi_UnifyorderqueryChangeResourceId(p, t):
    met = unifyorderApi.UnifyorderqueryResourceId()
    return __defult(met, p, t)


# rc 统一交易创建订单
def unifyorderApi_UnifyorderOrdercreate(p, t):
    met = unifyorderApi.UnifyorderRCOrdercreate()
    return __defult(met, p, t)


# rc 支付
def unifyorderApi_UnifyorderPayModes(p, t):
    met = unifyorderApi.UnifyorderPayModes()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderConfirmInvoiceChange(p, t):
    met = unifyorderApi.UnifyorderConfirmInvoiceChange()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderOrderCreate(p, t):
    met = unifyorderApi.UnifyorderOrderCreate()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderCashierPayModes(p, t):
    met = unifyorderApi.UnifyorderCashierPayModes()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderOrderDetail(p, t):
    met = unifyorderApi.UnifyorderOrderDetail()
    return __defult(met, p, t)

def unifyorderApi_UnifyorderRCOrderDetail(p, t):
    met = unifyorderApi.UnifyorderRCOrderDetail()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderCashierCheck(p, t):
    met = unifyorderApi.UnifyorderCashierCheck()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderCashierCreate(p, t):
    met = unifyorderApi.UnifyorderCashierCreate()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderMemberEquityQuery(p, t):
    met = unifyorderApi.UnifyorderMemberEquityQuery()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderConfirmEquityChange(p, t):
    met = unifyorderApi.UnifyorderConfirmEquityChange()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderMemberIntegralUse(p, t):
    met = unifyorderApi.UnifyorderMemberIntegralUse()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderMemberIntegralStop(p, t):
    met = unifyorderApi.UnifyorderMemberIntegralStop()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderMemberResourceQuery(p, t):
    met = unifyorderApi.UnifyorderMemberResourceQuery()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderConfirmResouceChange(p, t):
    met = unifyorderApi.UnifyorderConfirmResouceChange()
    return __defult(met, p, t)


def unifyorderApi_UnifyproductDetails(p, t):
    met = unifyorderApi.UnifyproductDetails()
    return __defult(met, p, t)


def unifyorderApi_UnifyproductBuyLimit(p, t):
    met = unifyorderApi.UnifyproductBuyLimit()
    return __defult(met, p, t)

def unifyorderApi_UnifyRCproductBuyLimit(p, t):
    met = unifyorderApi.UnifyRCproductBuyLimit()
    return __defult(met, p, t)

def unifyorderApi_UnifyorderRCMemberCouponQuery(p, t):
    met = unifyorderApi.UnifyorderRCMemberCouponQuery()
    return __defult(met, p, t)

#rc用户规则查询
def unifyorderApi_UnifyorderRCUserRuleQuery(p, t):
    met = unifyorderApi.UnifyorderRCUserRuleQuery()
    return __defult(met, p, t)

#rc联合会员接口
def unifyorderApi_UnifyorderRCUserRole(p, t):
    met = unifyorderApi.UnifyorderRCUserRole()
    return __defult(met, p, t)

def unifyorderApi_UnifyorderConfirmRemark(p, t):
    met = unifyorderApi.UnifyorderConfirmRemark()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderAddressQueryInfos(p, t):
    met = unifyorderApi.UnifyorderAddressQueryInfos()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderConfirmShipmentChange(p, t):
    met = unifyorderApi.UnifyorderConfirmShipmentChange()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderAddressAdd(p, t):
    met = unifyorderApi.UnifyorderAddressAdd()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderMemberCouponQuery(p, t):
    met = unifyorderApi.UnifyorderMemberCouponQuery()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderConfirmCouponChange(p, t):
    met = unifyorderApi.UnifyorderConfirmCouponChange()
    return __defult(met, p, t)


def unifyOrderCenterApi_UnifyorderCashiercreate(p, t):
    met = unifyOrderCenterApi.UnifyorderCashiercreate()
    return __defult(met, p, t)


def unifyOrderCenterApi_UnifyorderCashierqueryCashier(p, t):
    met = unifyOrderCenterApi.UnifyorderCashierquery()
    return __defult(met, p, t)


def unifyOrderCenterApi_UnifyorderNotifyPaymentData(p, t):
    met = unifyOrderCenterApi.UnifyorderNotifyPayment()
    return __defult(met, p, t)

def unifyOrderCenterApi_UnifyorderQueryMain(p, t):
    met = unifyOrderCenterApi.UnifyorderQueryMain()
    return __defult(met, p, t)

def unifyOrderCenterApi_UnifyorderAttach(p, t):
    met = unifyOrderCenterApi.UnifyorderAttach()
    return __defult(met, p, t)

def unifyOrderCenterApi_UnifyorderQueryOriginalMain(p, t):
    met = unifyOrderCenterApi.UnifyorderQueryOriginalMain()
    return __defult(met, p, t)

def unifyOrderCenterApi_UnifyorderOrderCancelSubData(p, t):
    met = unifyOrderCenterApi.UnifyorderOrderCancelSub()
    return __defult(met, p, t)

def unifyOrderCenterApi_UnifyorderConfirmJudgeSkuNo(p, t):
    met = unifyOrderCenterApi.UnifyorderConfirmJudgeSkuNo()
    return __defult(met, p, t)

def unifyOrderCenterApi_UnifycartCartAdd(p, t):
    met = unifyOrderCenterApi.UnifycartCartAdd()
    return __defult(met, p, t)

def unifyOrderCenterApi_UnifycartCartCount(p, t):
    met = unifyOrderCenterApi.UnifycartCartCount()
    return __defult(met, p, t)

def unifyOrderCenterApi_UnifyproductBuyLimit(p, t):
    met = unifyOrderCenterApi.UnifyproductBuyLimit()
    return __defult(met, p, t)

def unifyOrderCenterApi_UnifyAddressDefault(p, t):
    met = unifyOrderCenterApi.UnifyAddressDefault()
    return __defult(met, p, t)

def unifyOrderCenterApi_UnifyCartQuery(p, t):
    met = unifyOrderCenterApi.UnifyCartQuery()
    return __defult(met, p, t)

def unifyOrderCenterApi_UnifyorderConfirmShoppingCreate(p, t):
    met = unifyOrderCenterApi.UnifyorderConfirmShoppingCreate()
    return __defult(met, p, t)

def unifyOrderCenterApi_UnifyorderConfirmDetail(p, t):
    met = unifyOrderCenterApi.UnifyorderConfirmDetail()
    return __defult(met, p, t)

def unifyOrderCenterApi_UnifyorderConfirmUserRuleQuery(p, t):
    met = unifyOrderCenterApi.UnifyorderConfirmUserRuleQuery()
    return __defult(met, p, t)

def unifyOrderCenterApi_UnifyorderMemberCouponQuery(p, t):
    met = unifyOrderCenterApi.UnifyorderMemberCouponQuery()
    return __defult(met, p, t)

def unifyOrderCenterApi_UnifyorderConfirmUserRoleContainsIdentity(p, t):
    met = unifyOrderCenterApi.UnifyorderConfirmUserRoleContainsIdentity()
    return __defult(met, p, t)

def unifyOrderCenterApi_UnifyorderMemberIntegralUse(p, t):
    met = unifyOrderCenterApi.UnifyorderMemberIntegralUse()
    return __defult(met, p, t)

def customerCenterApi_VoucherListing(p, t):
    met = customerCenterApi.VoucherListing()
    return __defult(met, p, t)


def customerCenterApi_PromoteCardlist(p, t):
    met = customerCenterApi.PromoteCardlist()
    return __defult(met, p, t)


def userCenterApi_MngUserUserSave(p, t):
    met = userCenterApi.MngUserUserSave()
    return __defult(met, p, t)


def userCenterApi_MngUserUserUpdate(p, t):
    met = userCenterApi.MngUserUserUpdate()
    return __defult(met, p, t)


def userCenterApi_MngUserUserUpdateStatus(p, t):
    met = userCenterApi.MngUserUserUpdateStatus()
    return __defult(met, p, t)


def userCenterApi_V2ApiUserCardAdd(p, t):
    met = userCenterApi.V2ApiUserCardAdd()
    return __defult(met, p, t)


def userCenterApi_MngUserUserCardApproveSetStatus(p, t):
    met = userCenterApi.MngUserUserCardApproveSetStatus()
    return __defult(met, p, t)


def userCenterApi_MngUserUserPage(p, t):
    met = userCenterApi.MngUserUserPage()
    return __defult(met, p, t)


def userCenterApi_MngUserUserTagAdd(p, t):
    met = userCenterApi.MngUserUserTagAdd()
    return __defult(met, p, t)


def userCenterApi_MngUserUserTagDetail(p, t):
    met = userCenterApi.MngUserUserTagDetail()
    return __defult(met, p, t)


def userCenterApi_MngUserUserTagGet(p, t):
    met = userCenterApi.MngUserUserTagGet()
    return __defult(met, p, t)


def userCenterApi_V2ApiOrgAdd(p, t):
    met = userCenterApi.V2ApiOrgAdd()
    return __defult(met, p, t)


def userCenterApi_V2ApiOrgQueryBy(p, t):
    met = userCenterApi.V2ApiOrgQueryBy()
    return __defult(met, p, t)


def userCenterApi_V2ApiOrgRemove(p, t):
    met = userCenterApi.V2ApiOrgRemove()
    return __defult(met, p, t)


def userCenterApi_MngUserUserTagRemove(p, t):
    met = userCenterApi.MngUserUserTagRemove()
    return __defult(met, p, t)


def userCenterApi_MngUserUserIdentityUpdate(p, t):
    met = userCenterApi.MngUserUserIdentityUpdate()
    return __defult(met, p, t)


def userCenterApi_MngUserUserCardAdd(p, t):
    met = userCenterApi.MngUserUserCardAdd()
    return __defult(met, p, t)


def userCenterApi_MngUserUserCardUpdate(p, t):
    met = userCenterApi.MngUserUserCardUpdate()
    return __defult(met, p, t)


def userCenterApi_V2ApiUserCardAddByNo(p, t):
    met = userCenterApi.V2ApiUserCardAddByNo()
    return __defult(met, p, t)


def orderCenterApi_OrderCacheDel(p, t):
    met = orderCenterApi.OrderCacheDel()
    return __defult(met, p, t)


def orderCenterApi_LogisticsDeliverNotify(p, t):
    met = orderCenterApi.LogisticsDeliverNotify()
    return __defult(met, p, t)


def orderCenterApi_NeworderRefundcashier(p, t):
    met = orderCenterApi.NeworderRefundcashier()
    return __defult(met, p, t)


def promoteCenterApi_PromoteSchemeAdd(p, t):
    met = promoteCenterApi.PromoteSchemeAdd()
    return __defult(met, p, t)


def promoteCenterApi_PromoteSendcard(p, t):
    met = promoteCenterApi.PromoteSendcard()
    return __defult(met, p, t)


def adminBackend_login(mobile, env):
    # 登录药联后台
    authApi_SmsSend(
        {"header": {"Content-Type": "application/json;charset=UTF-8"}, "parma": {}, "data": {"mobile": mobile},
         "env": env}, "dict")
    # 从数据库提取验证码-获取原始sql
    tmpSql = "SELECT captcha FROM `cn_uniondrug_module_data`.`captcha` where mobile = '15005150023' ORDER BY id desc LIMIT 1"
    # 从数据库提取验证码-修改sql where条件
    finSql = ckw.CommonKeyWord().Str_Replace(tmpSql, 15005150023, mobile)
    # 从数据库提取验证码-执行查询
    sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", finSql)

    code = ckw.jsonTools.getJsonValue(sqlRes[0], [["captcha"]])
    reslogin = authApi_DdMobilelogin({"header": {"Content-Type": "application/json;charset=UTF-8"}, "parma": {},
                                      "data": {"mobile": mobile, "code": code}, "env": env}, "dict")
    tmp = ckw.CommonKeyWord().Json_GetJsonValue(reslogin, [["data"]])
    tmpToken = ckw.CommonKeyWord().Json_GetJsonValue(tmp, [["token"]])
    bb = authApi_Ddlogin(
        {"header": {"Content-Type": "application/json;charset=UTF-8"}, "parma": {}, "data": {"token": tmpToken},
         "env": env}, "dict")
    backToken = ckw.jsonTools.getJsonValue(bb, [["data", "token"]])
    return backToken


def thePublic_login(mobile, env):
    # 登录发送验证码
    authApi_LoginSendCaptcha(
        {"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": {"mobile": mobile},
         "env": env}, "dict")
    # 从数据库提取验证码-获取原始sql
    tmpSql = "SELECT * FROM `cn_uniondrug_module_sms`.`message` WHERE mobile = '15005150023' ORDER BY gmtCreated DESC LIMIT 1;"
    # 从数据库提取验证码-修改sql where条件
    finSql = ckw.CommonKeyWord().Str_Replace(tmpSql, 15005150023, mobile)
    # 从数据库提取验证码-执行查询
    sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", finSql)
    # 打印查询结果到控制台
    ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
    # 打印查询结果到日志
    ckw.CommonKeyWord().Print_ToLog("sql查询结果：", sqlRes)
    # 从数据库提取验证码-提取验证码01
    captcha1 = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["data"]])
    # 从数据库提取验证码-提取验证码02
    captcha = ckw.CommonKeyWord().Json_GetJsonValue(captcha1, [["sms", "code"]])
    # 打印验证码到控制台
    ckw.CommonKeyWord().Print_ToControl("验证码：", captcha1)
    ckw.CommonKeyWord().Print_ToControl("验证码：", captcha)
    # 打印验证码到日志
    ckw.CommonKeyWord().Print_ToLog("验证码：", captcha)
    # 登录获取token-调取接口
    loginRes = authApi_LoginLogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},
                                   "data": {"mobile": mobile, "code": captcha}, "env": env}, "dict")
    token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "token"]])
    return token


def theRCPublic_login(mobile, env):
    # 登录发送验证码
    authApi_LoginSendCaptcha(
        {"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": {"mobile": mobile},
         "env": env}, "dict")
    # 从数据库提取验证码-获取原始sql
    tmpSql = "SELECT * FROM `cn_uniondrug_module_sms`.`message` WHERE mobile = '15005150023' ORDER BY gmtCreated DESC LIMIT 1;"
    # 从数据库提取验证码-修改sql where条件
    finSql = ckw.CommonKeyWord().Str_Replace(tmpSql, 15005150023, mobile)
    # 从数据库提取验证码-执行查询
    sqlRes = ckw.CommonKeyWord().Db_SshConfRCMysqlExecute("DATABASE_RC_cn_uniondrug_module_sms", finSql)
    # 打印查询结果到控制台
    ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
    # 打印查询结果到日志
    ckw.CommonKeyWord().Print_ToLog("sql查询结果：", sqlRes)
    # 从数据库提取验证码-提取验证码01
    captcha1 = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["data"]])
    # 从数据库提取验证码-提取验证码02
    captcha = ckw.CommonKeyWord().Json_GetJsonValue(captcha1, [["sms", "code"]])
    # 打印验证码到控制台
    ckw.CommonKeyWord().Print_ToControl("验证码：", captcha1)
    ckw.CommonKeyWord().Print_ToControl("验证码：", captcha)
    # 打印验证码到日志
    ckw.CommonKeyWord().Print_ToLog("验证码：", captcha)
    # 登录获取token-调取接口
    loginRes = authApi_LoginLogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},
                                   "data": {"mobile": mobile, "code": captcha}, "env": env}, "dict")
    print("loginRes", loginRes)
    token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "token"]])
    return token


def authApi_RegisterGs(p, t):
    met = auth.RegisterGs()
    return __defult(met, p, t)


def backendApi_OrdersCart(p, t):
    met = backendApi.OrdersCart()
    return __defult(met, p, t)


def backendApi_DtpOrdersCart(p, t):
    met = backendApi.DtpOrdersCart()
    return __defult(met, p, t)


def backendApi_MerhantVillageDoctor(p, t):
    met = backendApi.MerhantVillageDoctor()
    return __defult(met, p, t)


def backendApi_VillageDoctorOrdersCart(p, t):
    met = backendApi.VillageDoctorOrdersCart()
    return __defult(met, p, t)


def backendApi_Recipe(p, t):
    met = backendApi.Recipe()
    return __defult(met, p, t)


def backendApi_RecipeCart(p, t):
    met = backendApi.RecipeCart()
    return __defult(met, p, t)


def backendApi_RenewCart(p, t):
    met = backendApi.RenewCart()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngPaging(p, t):
    met = orderCenterApi.MngOrderOrderMngPaging()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngDetail(p, t):
    met = orderCenterApi.MngOrderOrderMngDetail()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngOrderallequity(p, t):
    met = orderCenterApi.MngOrderOrderMngOrderallequity()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngExpresslist(p, t):
    met = orderCenterApi.MngOrderOrderMngExpresslist()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngOrdercancelsub(p, t):
    met = orderCenterApi.MngOrderOrderMngOrdercancelsub()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngRefundlist(p, t):
    met = orderCenterApi.MngOrderOrderMngRefundlist()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngDeliver(p, t):
    met = orderCenterApi.MngOrderOrderMngDeliver()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngRefundgoods(p, t):
    met = orderCenterApi.MngOrderOrderMngRefundgoods()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngRefundcashier(p, t):
    met = orderCenterApi.MngOrderOrderMngRefundcashier()
    return __defult(met, p, t)


def creditCenterApi_CreditAccountTradeAdd(p, t):
    met = creditCenterApi.CreditAccountTradeAdd()
    return __defult(met, p, t)


def creditCenterApi_CreditAccountTradeBatchAdd(p, t):
    met = creditCenterApi.CreditAccountTradeBatchAdd()
    return __defult(met, p, t)


def creditCenterApi_CreditGoodsTradeTransfer(p, t):
    met = creditCenterApi.CreditGoodsTradeTransfer()
    return __defult(met, p, t)


def creditCenterApi_CreditPayTradeTrialCalculation(p, t):
    met = creditCenterApi.CreditPayTradeTrialCalculation()
    return __defult(met, p, t)


def creditCenterApi_CreditPayTradeLock(p, t):
    met = creditCenterApi.CreditPayTradeLock()
    return __defult(met, p, t)


def creditCenterApi_CreditPayTradeRelease(p, t):
    met = creditCenterApi.CreditPayTradeRelease()
    return __defult(met, p, t)


def creditCenterApi_CreditPayTradeConsume(p, t):
    met = creditCenterApi.CreditPayTradeConsume()
    return __defult(met, p, t)


def creditCenterApi_CreditPreAccountTradePreAdd(p, t):
    met = creditCenterApi.CreditPreAccountTradePreAdd()
    return __defult(met, p, t)


def creditCenterApi_CreditPreAccountTradeEdit(p, t):
    met = creditCenterApi.CreditPreAccountTradeEdit()
    return __defult(met, p, t)


def creditCenterApi_CreditPreAccountTradeEditBatch(p, t):
    met = creditCenterApi.CreditPreAccountTradeEditBatch()
    return __defult(met, p, t)


def creditCenterApi_CreditIntegralTradeWithdraw(p, t):
    met = creditCenterApi.CreditIntegralTradeWithdraw()
    return __defult(met, p, t)


def creditCenterApi_CreditIntegralTradeConfirmWithdraw(p, t):
    met = creditCenterApi.CreditIntegralTradeConfirmWithdraw()
    return __defult(met, p, t)


def creditCenterApi_CreditCompanySettleTradeCheckCompanyCredit(p, t):
    met = creditCenterApi.CreditCompanySettleTradeCheckCompanyCredit()
    return __defult(met, p, t)


def creditCenterApi_CreditCompanySettleTradePullCompanyRecords(p, t):
    met = creditCenterApi.CreditCompanySettleTradePullCompanyRecords()
    return __defult(met, p, t)


def creditCenterApi_CreditCompanySettleTradeSettleApply(p, t):
    met = creditCenterApi.CreditCompanySettleTradeSettleApply()
    return __defult(met, p, t)


def creditCenterApi_CreditCompanySettleTradeSettleConfirm(p, t):
    met = creditCenterApi.CreditCompanySettleTradeSettleConfirm()
    return __defult(met, p, t)


def creditCenterApi_CreditAccountQueryPreCount(p, t):
    met = creditCenterApi.CreditAccountQueryPreCount()
    return __defult(met, p, t)


def creditCenterApi_CreditAccountQueryCountHistory(p, t):
    met = creditCenterApi.CreditAccountQueryCountHistory()
    return __defult(met, p, t)


def creditCenterApi_CreditPreAccountTradeEditInfo(p, t):
    met = creditCenterApi.CreditPreAccountTradeEditInfo()
    return __defult(met, p, t)


def creditCenterApi_CreditAccountAdminExport(p, t):
    met = creditCenterApi.CreditAccountAdminExport()
    return __defult(met, p, t)


def creditCenterApi_CreditAccountQueryMemberAccountQuery(p, t):
    met = creditCenterApi.CreditAccountQueryMemberAccountQuery()
    return __defult(met, p, t)


def creditCenterApi_CreditAccountQueryPrePaging(p, t):
    met = creditCenterApi.CreditAccountQueryPrePaging()
    return __defult(met, p, t)


def assistantappApi_UserLogin(p, t):
    met = assistantappApi.UserLogin()
    return __defult(met, p, t)


def assistantappApi_CodeSend(p, t):
    met = assistantappApi.CodeSend()
    return __defult(met, p, t)


def assistantappApi_UserSmsLogin(p, t):
    met = assistantappApi.UserSmsLogin()
    return __defult(met, p, t)


def assistantappApi_CustomerAdd(p, t):
    met = assistantappApi.CustomerAdd()
    return __defult(met, p, t)


def assistantappApi_CustomerPaging(p, t):
    met = assistantappApi.CustomerPaging()
    return __defult(met, p, t)


def assistantappApi_CustomerInfo(p, t):
    met = assistantappApi.CustomerInfo()
    return __defult(met, p, t)


def assistantappApi_CustomerEdit(p, t):
    met = assistantappApi.CustomerEdit()
    return __defult(met, p, t)


def assistantappApi_CustomerDelete(p, t):
    met = assistantappApi.CustomerDelete()
    return __defult(met, p, t)


def assistantappApi_InspectCreate(p, t):
    met = assistantappApi.InspectCreate()
    return __defult(met, p, t)


def assistantappApi_VisitAddCommonVisit(p, t):
    met = assistantappApi.VisitAddCommonVisit()
    return __defult(met, p, t)


def assistantappApi_VisitArrivalVisit(p, t):
    met = assistantappApi.VisitArrivalVisit()
    return __defult(met, p, t)


def assistantappApi_VisitVisitComplete(p, t):
    met = assistantappApi.VisitVisitComplete()
    return __defult(met, p, t)


def assistantappApi_VisitAddInterimVisit(p, t):
    met = assistantappApi.VisitAddInterimVisit()
    return __defult(met, p, t)


def assistantappApi_VisitPaging(p, t):
    met = assistantappApi.VisitPaging()
    return __defult(met, p, t)


def assistantappApi_VisitInfo(p, t):
    met = assistantappApi.VisitInfo()
    return __defult(met, p, t)


def assistantappApi_InspectStart(p, t):
    met = assistantappApi.InspectStart()
    return __defult(met, p, t)


def assistantappApi_MerchantStoreUpdate(p, t):
    met = assistantappApi.MerchantStoreUpdate()
    return __defult(met, p, t)


def assistantappApi_InspectUpdate(p, t):
    met = assistantappApi.InspectUpdate()
    return __defult(met, p, t)


def assistantappApi_InspectList(p, t):
    met = assistantappApi.InspectList()
    return __defult(met, p, t)


def assistantappApi_InspectDetail(p, t):
    met = assistantappApi.InspectDetail()
    return __defult(met, p, t)


def assistantappApi_MerchantList(p, t):
    met = assistantappApi.MerchantList()
    return __defult(met, p, t)


def assistantappApi_MerchantInfo(p, t):
    met = assistantappApi.MerchantInfo()
    return __defult(met, p, t)


def assistantappApi_MerchantStoreList(p, t):
    met = assistantappApi.MerchantStoreList()
    return __defult(met, p, t)


def assistantappApi_MerchantStoreDetail(p, t):
    met = assistantappApi.MerchantStoreDetail()
    return __defult(met, p, t)


def assistantappApi_AssistantRegister(p, t):
    met = assistantappApi.AssistantRegister()
    return __defult(met, p, t)


def assistantappApi_V4CodeSend(p, t):
    met = assistantappApi.V4CodeSend()
    return __defult(met, p, t)


def assistantappApi_MerchantStoreIsCanAdd(p, t):
    met = assistantappApi.MerchantStoreIsCanAdd()
    return __defult(met, p, t)


def assistantappApi_MerchantStorePush(p, t):
    met = assistantappApi.MerchantStorePush()
    return __defult(met, p, t)


def assistantappApi_AssistantLists(p, t):
    met = assistantappApi.AssistantLists()
    return __defult(met, p, t)


def assistantappApi_AssistantDetail(p, t):
    met = assistantappApi.AssistantDetail()
    return __defult(met, p, t)


def assistantappApi_AssistantStoreTransfer(p, t):
    met = assistantappApi.AssistantStoreTransfer()
    return __defult(met, p, t)


def assistantappApi_AssistantUpdate(p, t):
    met = assistantappApi.AssistantUpdate()
    return __defult(met, p, t)


def assistantappApi_WorkList(p, t):
    met = assistantappApi.WorkList()
    return __defult(met, p, t)


def userCenterApi_UserBasicQuery(p, t):
	met = userCenterApi.UserBasicQuery()
	return __defult(met, p, t)
def userCenterApi_MngTaskUpdate(p, t):
	met = userCenterApi.MngTaskUpdate()
	return __defult(met, p, t)
def imApi_MyCustomers(p, t):
	met = imApi.MyCustomers()
	return __defult(met, p, t)
def imApi_GetRecommendAdvisor1(p, t):
	met = imApi.GetRecommendAdvisor1()
	return __defult(met, p, t)
def imApi_GetRecommendAdvisor2(p, t):
	met = imApi.GetRecommendAdvisor2()
	return __defult(met, p, t)
def imApi_GetAdvisorInfo(p, t):
	met = imApi.GetAdvisorInfo()
	return __defult(met, p, t)
def imApi_GetBindAdvisorInfo(p, t):
	met = imApi.GetBindAdvisorInfo()
	return __defult(met, p, t)


def userCenterApi_UserBasicQuery(p, t):
    met = userCenterApi.UserBasicQuery()
    return __defult(met, p, t)


def userCenterApi_MngTaskUpdate(p, t):
    met = userCenterApi.MngTaskUpdate()
    return __defult(met, p, t)


def unifyOrderCenterApi_UnifyorderGetConfirmNo(p, t):
    met = unifyOrderCenterApi.UnifyorderGetConfirmNo()
    return __defult(met, p, t)


def unifyOrderCenterApi_UnifyorderqueryMulti(p, t):
    met = unifyOrderCenterApi.UnifyorderqueryMulti()
    return __defult(met, p, t)


def unifyOrderCenterApi_UnifyorderResoucechange(p, t):
    met = unifyOrderCenterApi.UnifyorderResoucechange()
    return __defult(met, p, t)


def unifyOrderCenterApi_UnifyorderOrdercreate(p, t):
    met = unifyOrderCenterApi.UnifyorderOrdercreate()
    return __defult(met, p, t)


def unifyOrderCenterApi_UnifyorderCashierpayModes(p, t):
    met = unifyOrderCenterApi.UnifyorderCashierpayModes()
    return __defult(met, p, t)


def imApi_MyCustomers(p, t):
    met = imApi.MyCustomers()
    return __defult(met, p, t)


def imApi_GetRecommendAdvisor1(p, t):
    met = imApi.GetRecommendAdvisor1()
    return __defult(met, p, t)


def imApi_GetRecommendAdvisor2(p, t):
    met = imApi.GetRecommendAdvisor2()
    return __defult(met, p, t)


def imApi_GetAdvisorInfo(p, t):
    met = imApi.GetAdvisorInfo()
    return __defult(met, p, t)


def imApi_GetBindAdvisorInfo(p, t):
    met = imApi.GetBindAdvisorInfo()
    return __defult(met, p, t)


def authApi_makeLoginCaptcha(p, t):
    met = authApi.makeLoginCaptcha()
    return __defult(met, p, t)


def assistantappApi_WorkJob(p, t):
    met = assistantappApi.WorkJob()
    return __defult(met, p, t)


def assistantappApi_WorkCancel(p, t):
    met = assistantappApi.WorkCancel()
    return __defult(met, p, t)


def assistantappApi_WorkAccept(p, t):
    met = assistantappApi.WorkAccept()
    return __defult(met, p, t)


def assistantappApi_WorkRecordCreate(p, t):
    met = assistantappApi.WorkRecordCreate()
    return __defult(met, p, t)


def assistantappApi_WorkRecordComplete(p, t):
    met = assistantappApi.WorkRecordComplete()
    return __defult(met, p, t)


def stagnationApi_LoginImageCaptcha(p, t):
    met = stagnationApi.LoginImageCaptcha()
    return __defult(met, p, t)


def stagnationApi_LoginSendCaptchaNew(p, t):
    met = stagnationApi.LoginSendCaptchaNew()
    return __defult(met, p, t)


def stagnationApi_LoginLogin(p, t):
    met = stagnationApi.LoginLogin()
    return __defult(met, p, t)


def stagnationApi_StagnationUserStatistic(p, t):
    met = stagnationApi.StagnationUserStatistic()
    return __defult(met, p, t)


def stagnationApi_StagnationUserUserInfo(p, t):
    met = stagnationApi.StagnationUserUserInfo()
    return __defult(met, p, t)


def stagnationApi_StagnationUserRecordPaging(p, t):
    met = stagnationApi.StagnationUserRecordPaging()
    return __defult(met, p, t)
def userCenterApi_UserBasicQuery(p, t):
    met = userCenterApi.UserBasicQuery()
    return __defult(met, p, t)


def userCenterApi_MngTaskUpdate(p, t):
    met = userCenterApi.MngTaskUpdate()
    return __defult(met, p, t)


def goodsCenterApi_insertStandardGoods(p, t):
    met = goodsCenterApi.insertStandardGoods()
    return __defult(met, p, t)


def goodsCenterApi_StandardGoodsFindByPage(p, t):
    met = goodsCenterApi.StandardGoodsFindByPage()
    return __defult(met, p, t)


def goodsCenterApi_updateManualYaozs(p, t):
    met = goodsCenterApi.updateManualYaozs()
    return __defult(met, p, t)


def goodsCenterApi_QueryManualYaozs(p, t):
    met = goodsCenterApi.QueryManualYaozs()
    return __defult(met, p, t)


def goodsCenterApi_queryGcStandardGoods(p, t):
    met = goodsCenterApi.queryGcStandardGoods()
    return __defult(met, p, t)


def goodsCenterApi_GoodsSpuDetailsSave(p, t):
    met = goodsCenterApi.GoodsSpuDetailsSave()
    return __defult(met, p, t)


def goodsCenterApi_GoodsSpuDetailsQuery(p, t):
    met = goodsCenterApi.GoodsSpuDetailsQuery()
    return __defult(met, p, t)


def imApi_MyCustomers(p, t):
    met = imApi.MyCustomers()
    return __defult(met, p, t)


def imApi_GetRecommendAdvisor1(p, t):
    met = imApi.GetRecommendAdvisor1()
    return __defult(met, p, t)


def imApi_GetRecommendAdvisor2(p, t):
    met = imApi.GetRecommendAdvisor2()
    return __defult(met, p, t)


def imApi_GetAdvisorInfo(p, t):
    met = imApi.GetAdvisorInfo()
    return __defult(met, p, t)


def imApi_GetBindAdvisorInfo(p, t):
    met = imApi.GetBindAdvisorInfo()
    return __defult(met, p, t)


def assistantappApi_MerchantAllList(p, t):
    met = assistantappApi.MerchantAllList()
    return __defult(met, p, t)


def assistantappApi_ApprovalAddApprovalVisit(p, t):
    met = assistantappApi.ApprovalAddApprovalVisit()
    return __defult(met, p, t)


def assistantappApi_ApprovalAddApprovalSign(p, t):
    met = assistantappApi.ApprovalAddApprovalSign()
    return __defult(met, p, t)


def assistantappApi_ApprovalAddApprovalTrain(p, t):
    met = assistantappApi.ApprovalAddApprovalTrain()
    return __defult(met, p, t)


def activityApi_AdminTemplateSave(p, t):
    met = activityApi.AdminTemplateSave()
    return __defult(met, p, t)


def activityApi_AdminTemplatePurchaseGoodsList(p, t):
    met = activityApi.AdminTemplatePurchaseGoodsList()
    return __defult(met, p, t)


def activityApi_DdLogin(p, t):
    met = activityApi.DdLogin()
    return __defult(met, p, t)


def activityApi_DdMobilelogin(p, t):
    met = activityApi.DdMobilelogin()
    return __defult(met, p, t)


def activityApi_SmsReset(p, t):
    met = activityApi.SmsReset()
    return __defult(met, p, t)


def activityApi_AdminTemplateDel(p, t):
    met = activityApi.AdminTemplateDel()
    return __defult(met, p, t)


def activityApi_ActivitySave(p, t):
    met = activityApi.ActivitySave()
    return __defult(met, p, t)


def activityApi_ActivitySwitch(p, t):
    met = activityApi.ActivitySwitch()
    return __defult(met, p, t)


def activityApi_Activity1RedOneSendRedeem(p, t):
    met = activityApi.Activity1RedOneSendRedeem()
    return __defult(met, p, t)


def activityApi_CommonMemberParse(p, t):
    met = activityApi.CommonMemberParse()
    return __defult(met, p, t)


def DrugStoreApi_V4DrugsSearch(p, t):
    met = activityApi.CommonMemberParse()
    return __defult(met, p, t)


class ApproveApi(object):
    pass


def ApproveApi_UnfreezeAssistantSubmitApproval(p, t):
    met = ApproveApi.UnfreezeAssistantSubmitApproval()
    return __defult(met, p, t)


# 备注test一下
# 备注测试一下2
# 备注测试一下4
# 备注测试一下3
def insureApi_queryPoolClaimAmount(p, t):
    met = insureApi.queryPoolClaimAmount()
    return __defult(met, p, t)


def insureApi_listFeeBill(p, t):
    met = insureApi.listFeeBill()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderqueryMulti(p, t):
    met = unifyorderApi.UnifyorderqueryMulti()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderqueryResourceId(p, t):
    met = unifyorderApi.UnifyorderqueryResourceId()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderRCOrdercreate(p, t):
    met = unifyorderApi.UnifyorderRCOrdercreate()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderRcPaymentNo(p, t):
    met = unifyorderApi.UnifyorderRcPaymentNo()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderRcCashierCreate(p, t):
    met = unifyorderApi.UnifyorderRcCashierCreate()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderRcFinishPayment(p, t):
    met = unifyorderApi.UnifyorderRcFinishPayment()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderRcCashierCheck(p, t):
    met = unifyorderApi.UnifyorderRcCashierCheck()
    return __defult(met, p, t)


def unifyOrderCenterApi_UnifyorderCashierquery(p, t):
    met = unifyOrderCenterApi.UnifyorderCashierquery()
    return __defult(met, p, t)


def unifyOrderCenterApi_UnifyorderNotifyPayment(p, t):
    met = unifyOrderCenterApi.UnifyorderNotifyPayment()
    return __defult(met, p, t)


def newCleanCenterApi_openQueryVas(p, t):
    met = newCleanCenterApi.openQueryVas()
    return __defult(met, p, t)


def newCleanCenterApi_openExecSpecialDisease(p, t):
    met = newCleanCenterApi.openExecSpecialDisease()
    return __defult(met, p, t)


def newCleanCenterApi_cleanQueryQueryAll(p, t):
    met = newCleanCenterApi.cleanQueryQueryAll()
    return __defult(met, p, t)


def newCleanCenterApi_healthOrder(p, t):
    met = newCleanCenterApi.healthOrder()
    return __defult(met, p, t)


def BusinessServicesApi_MrchantStoreClerkCount(p, t):
    met = BusinessServicesApi.MrchantStoreClerkCount()
    return __defult(met, p, t)


def BusinessServicesApi_HomePageOperateData(p, t):
    met = BusinessServicesApi.HomePageOperateData()
    return __defult(met, p, t)


def BusinessServicesApi_HomePageMonthStoreTop(p, t):
    met = BusinessServicesApi.HomePageMonthStoreTop()
    return __defult(met, p, t)


def BusinessServicesApi_HomePageMonthClerkTop(p, t):
    met = BusinessServicesApi.HomePageMonthClerkTop()
    return __defult(met, p, t)


def BusinessServicesApi_HomePageMerchantDataQuality(p, t):
    met = BusinessServicesApi.HomePageMerchantDataQuality()
    return __defult(met, p, t)


def BusinessServicesApi_HomePageGetBusinessInfo(p, t):
    met = BusinessServicesApi.HomePageGetBusinessInfo()
    return __defult(met, p, t)


def BusinessServicesApi_HomePageTodayData(p, t):
    met = BusinessServicesApi.HomePageTodayData()
    return __defult(met, p, t)


def BusinessServicesApi_MerchantInfo(p, t):
    met = BusinessServicesApi.MerchantInfo()
    return __defult(met, p, t)


def BusinessServicesApi_InclusiveCheckApply(p, t):
    met = BusinessServicesApi.InclusiveCheckApply()
    return __defult(met, p, t)


def BusinessServicesApi_UserLogin(p, t):
    met = BusinessServicesApi.UserLogin()
    return __defult(met, p, t)


def im_group_chat_IM_account(p, t):
    met = im_group_chat.IM.account()
    return __defult(met, p, t)


def im_group_chat_IM_couponMsg(p, t):
    met = im_group_chat.IM.couponMsg()
    return __defult(met, p, t)


def im_group_chat_IM_pollIsOnline(p, t) -> object:
    met = im_group_chat.IM.pollIsOnline()
    return __defult(met, p, t)


def im_group_chat_IM_imInit(p, t):
    met = im_group_chat.IM.imInit()
    return __defult(met, p, t)


def im_group_chat_IM_updateUser(p, t):
    met = im_group_chat.IM.updateUser()
    return __defult(met, p, t)


def im_group_chat_IM_addFriendTo(p, t):
    met = im_group_chat.chat.IM.addFriendTo()
    return __defult(met, p, t)


def im_group_chat_RenewCart(p: object, t: object) -> object:
    met = im_group_chat.RenewCart()
    return __defult(met, p, t)

def insureApi_getByProjectId(p, t):
	met = insureApi.getByProjectId()
	return __defult(met, p, t)
def insureApi_UnifyorderConfirmInvoiceChange(p, t):
	met = insureApi.UnifyorderConfirmInvoiceChange()
	return __defult(met, p, t)
def im_group_chat_IM_pollIsOnline(p, t):
	met = im.group.chat.IM.pollIsOnline()
	return __defult(met, p, t)
def im_group_chat_RenewCart(p, t):
	met = im.group.chat.RenewCart()
	return __defult(met, p, t)
def im_group_chat_IM_pollIsOnline(p, t):
	met = im.group.chat.IM.pollIsOnline()
	return __defult(met, p, t)
def im_group_chat_RenewCart(p, t):
	met = im.group.chat.RenewCart()
	return __defult(met, p, t)
def billCenterApi_systemRoleWorkertree(p, t):
	met = billCenterApi.systemRoleWorkertree()
	return __defult(met, p, t)
def billCenterApi_directPayoutStatementPaging(p, t):
	met = billCenterApi.directPayoutStatementPaging()
	return __defult(met, p, t)
def billCenterApi_payoutBillPaging(p, t):
	met = billCenterApi.payoutBillPaging()
	return __defult(met, p, t)
def insureApi_InfoPaging(p, t):
	met = insureApi.InfoPaging()
	return __defult(met, p, t)
def insureApi_dataCheck(p, t):
	met = insureApi.dataCheck()
	return __defult(met, p, t)
def insureApi_getByInsurerIdAndPolicyNo(p, t):
	met = insureApi.getByInsurerIdAndPolicyNo()
	return __defult(met, p, t)
def drugappApi_PrivilegeList(p, t):
	met = drugappApi.PrivilegeList()
	return __defult(met, p, t)
def drugappApi_PrivilegeV2ProgressList(p, t):
	met = drugappApi.PrivilegeV2ProgressList()
	return __defult(met, p, t)
def drugappApi_CiMemberPage(p, t):
	met = drugappApi.CiMemberPage()
	return __defult(met, p, t)
def drugappApi_CodeSend(p, t):
	met = drugappApi.CodeSend()
	return __defult(met, p, t)
def drugappApi_V4UsersSmslogin1(p, t):
	met = drugappApi.V4UsersSmslogin1()
	return __defult(met, p, t)
def drugappApi_CiMemberChatList(p, t):
	met = drugappApi.CiMemberChatList()
	return __defult(met, p, t)
def drugappApi_CiMemberStartChat(p, t):
	met = drugappApi.CiMemberStartChat()
	return __defult(met, p, t)
def drugappApi_CiMemberDetail(p, t):
	met = drugappApi.CiMemberDetail()
	return __defult(met, p, t)
def drugappApi_CiMemberAdvisorDetail(p, t):
	met = drugappApi.CiMemberAdvisorDetail()
	return __defult(met, p, t)
def drugappApi_PrivilegeRuleDetail(p, t):
	met = drugappApi.PrivilegeRuleDetail()
	return __defult(met, p, t)
def drugappApi_CiMemberEvaluateList(p, t):
	met = drugappApi.CiMemberEvaluateList()
	return __defult(met, p, t)
def drugappApi_ResourceBannerList(p, t):
	met = drugappApi.ResourceBannerList()
	return __defult(met, p, t)
def drugappApi_ResourceServiceList(p, t):
	met = drugappApi.ResourceServiceList()
	return __defult(met, p, t)
def drugappApi_CiMemberDeleteChat(p, t):
	met = drugappApi.CiMemberDeleteChat()
	return __defult(met, p, t)
def drugappApi_DrugstoreuserGroupCreate(p, t):
	met = drugappApi.DrugstoreuserGroupCreate()
	return __defult(met, p, t)
def drugappApi_GroupDetail(p, t):
	met = drugappApi.GroupDetail()
	return __defult(met, p, t)
def drugappApi_OrderCanUseList(p, t):
	met = drugappApi.OrderCanUseList()
	return __defult(met, p, t)
def drugappApi_UserWxConfig(p, t):
	met = drugappApi.UserWxConfig()
	return __defult(met, p, t)
def drugappApi_UserAddressList(p, t):
	met = drugappApi.UserAddressList()
	return __defult(met, p, t)
def drugappApi_OrderUpdatePreOrder(p, t):
	met = drugappApi.OrderUpdatePreOrder()
	return __defult(met, p, t)
def drugappApi_RxRxTabList(p, t):
	met = drugappApi.RxRxTabList()
	return __defult(met, p, t)
def drugappApi_OrderInit(p, t):
	met = drugappApi.OrderInit()
	return __defult(met, p, t)
def drugappApi_DrugUserList(p, t):
	met = drugappApi.DrugUserList()
	return __defult(met, p, t)
def drugappApi_DrugUserDetail(p, t):
	met = drugappApi.DrugUserDetail()
	return __defult(met, p, t)
def drugappApi_DrugUserAdd(p, t):
	met = drugappApi.DrugUserAdd()
	return __defult(met, p, t)
def drugappApi_RxApplyRx(p, t):
	met = drugappApi.RxApplyRx()
	return __defult(met, p, t)
def drugappApi_OrderCreateOrder(p, t):
	met = drugappApi.OrderCreateOrder()
	return __defult(met, p, t)
def drugappApi_OrderPreDetail(p, t):
	met = drugappApi.OrderPreDetail()
	return __defult(met, p, t)
def drugappApi_OrderRxUrl(p, t):
	met = drugappApi.OrderRxUrl()
	return __defult(met, p, t)
def drugappApi_ApiDrugCategory(p, t):
	met = drugappApi.ApiDrugCategory()
	return __defult(met, p, t)
def drugappApi_ApiCartAddCart(p, t):
	met = drugappApi.ApiCartAddCart()
	return __defult(met, p, t)
def drugappApi_ApiSearchTerms(p, t):
	met = drugappApi.ApiSearchTerms()
	return __defult(met, p, t)
def drugappApi_ApiSearchAssociateList(p, t):
	met = drugappApi.ApiSearchAssociateList()
	return __defult(met, p, t)
def drugappApi_ApiDrugSearch(p, t):
	met = drugappApi.ApiDrugSearch()
	return __defult(met, p, t)
def drugappApi_ApiMemberInfo(p, t):
	met = drugappApi.ApiMemberInfo()
	return __defult(met, p, t)
def drugappApi_ApiUtilGetExpressRule(p, t):
	met = drugappApi.ApiUtilGetExpressRule()
	return __defult(met, p, t)
def drugappApi_ApiActivityTemporaryActivity(p, t):
	met = drugappApi.ApiActivityTemporaryActivity()
	return __defult(met, p, t)
def drugappApi_ApiActivityIssueCoupon(p, t):
	met = drugappApi.ApiActivityIssueCoupon()
	return __defult(met, p, t)
def drugappApi_ApiUtilGetNearestStore(p, t):
	met = drugappApi.ApiUtilGetNearestStore()
	return __defult(met, p, t)
def drugappApi_ApiMemberModalBoxNotify(p, t):
	met = drugappApi.ApiMemberModalBoxNotify()
	return __defult(met, p, t)
def drugappApi_ApiNoticeIndex(p, t):
	met = drugappApi.ApiNoticeIndex()
	return __defult(met, p, t)
def drugappApi_ApiBonusMerchants(p, t):
	met = drugappApi.ApiBonusMerchants()
	return __defult(met, p, t)
def drugappApi_ApiUtilWeather(p, t):
	met = drugappApi.ApiUtilWeather()
	return __defult(met, p, t)
def drugappApi_ApiCartCheckCart(p, t):
	met = drugappApi.ApiCartCheckCart()
	return __defult(met, p, t)
def drugappApi_ApiActivityGetActivityIndex(p, t):
	met = drugappApi.ApiActivityGetActivityIndex()
	return __defult(met, p, t)
def drugappApi_ApiUtilFindSubstationConfig(p, t):
	met = drugappApi.ApiUtilFindSubstationConfig()
	return __defult(met, p, t)
def activityApi_AdminChainActivityPage(p, t):
	met = activityApi.AdminChainActivityPage()
	return __defult(met, p, t)
def activityApi_CommonMerchantHome(p, t):
	met = activityApi.CommonMerchantHome()
	return __defult(met, p, t)
def activityApi_CommonModuleInfoWxConfig(p, t):
	met = activityApi.CommonModuleInfoWxConfig()
	return __defult(met, p, t)
def activityApi_Activity6MerchantGetIds(p, t):
	met = activityApi.Activity6MerchantGetIds()
	return __defult(met, p, t)
def activityApi_CommonMerchantActivity(p, t):
	met = activityApi.CommonMerchantActivity()
	return __defult(met, p, t)
def DrugstoreApi_AdminTemplateSave(p, t):
	met = DrugstoreApi.AdminTemplateSave()
	return __defult(met, p, t)
def financeBusinessApi_invoicePage(p, t):
	met = financeBusinessApi.invoicePage()
	return __defult(met, p, t)
def customerCenterApi_OrderRefundApplyPaging(p, t):
	met = customerCenterApi.OrderRefundApplyPaging()
	return __defult(met, p, t)
def customerCenterApi_RefundapplyInfo(p, t):
	met = customerCenterApi.RefundapplyInfo()
	return __defult(met, p, t)
def unifyOrderCenterApi_UnifyorderOrderCancelSub(p, t):
	met = unifyOrderCenterApi.UnifyorderOrderCancelSub()
	return __defult(met, p, t)
def financeDataApi_partnerSetting(p, t):
	met = financeDataApi.partnerSetting()
	return __defult(met, p, t)
def financeDataApi_vipDetail(p, t):
	met = financeDataApi.vipDetail()
	return __defult(met, p, t)
def financeDataApi_partnerTodoList(p, t):
	met = financeDataApi.partnerTodoList()
	return __defult(met, p, t)
def financeDataApi_insurerInfo(p, t):
	met = financeDataApi.insurerInfo()
	return __defult(met, p, t)
def financeApi_SmsLogin(p, t):
	met = financeApi.SmsLogin()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_ApiDrugSearch(p, t):
	met = O2OPlaceTheOrderApi.ApiDrugSearch()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_ApiCartAddCart(p, t):
	met = O2OPlaceTheOrderApi.ApiCartAddCart()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_ApiCartShowCart(p, t):
	met = O2OPlaceTheOrderApi.ApiCartShowCart()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_ApiOrderCreatePreviewOrder(p, t):
	met = O2OPlaceTheOrderApi.ApiOrderCreatePreviewOrder()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_RxApplyRx(p, t):
	met = O2OPlaceTheOrderApi.RxApplyRx()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_OrderCreateOrder(p, t):
	met = O2OPlaceTheOrderApi.OrderCreateOrder()
	return __defult(met, p, t)
def newCleanCenterApi_cleanErpUpdateErpSn(p, t):
	met = newCleanCenterApi.cleanErpUpdateErpSn()
	return __defult(met, p, t)
def financeDataApi_versionControl(p, t):
	met = financeDataApi.versionControl()
	return __defult(met, p, t)
def financeDataApi_unitRelationship(p, t):
	met = financeDataApi.unitRelationship()
	return __defult(met, p, t)
def financeDataApi_unitBillInfo(p, t):
	met = financeDataApi.unitBillInfo()
	return __defult(met, p, t)
def financeDataApi_workerExist(p, t):
	met = financeDataApi.workerExist()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_UnifyorderConfirmUserRuleAddSign(p, t):
	met = O2OPlaceTheOrderApi.UnifyorderConfirmUserRuleAddSign()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_MngUserCardDelete(p, t):
	met = O2OPlaceTheOrderApi.MngUserCardDelete()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_VMemberEditnamecard(p, t):
	met = O2OPlaceTheOrderApi.VMemberEditnamecard()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_MemberUpdateUserInfo(p, t):
	met = O2OPlaceTheOrderApi.MemberUpdateUserInfo()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_ApiDrugCategory(p, t):
	met = O2OPlaceTheOrderApi.ApiDrugCategory()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_ApiDrugSearchDtpDrugs(p, t):
	met = O2OPlaceTheOrderApi.ApiDrugSearchDtpDrugs()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_OrganizebaseDirectChangeStatus(p, t):
	met = O2OPlaceTheOrderApi.OrganizebaseDirectChangeStatus()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_OrderInit(p, t):
	met = O2OPlaceTheOrderApi.OrderInit()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_OrderUpdatePreOrder(p, t):
	met = O2OPlaceTheOrderApi.OrderUpdatePreOrder()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_CanUseList(p, t):
	met = O2OPlaceTheOrderApi.CanUseList()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_VoucherCreate(p, t):
	met = O2OPlaceTheOrderApi.VoucherCreate()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_ApiWxJssdk(p, t):
	met = O2OPlaceTheOrderApi.ApiWxJssdk()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_ApiSweepGetPartnerStores(p, t):
	met = O2OPlaceTheOrderApi.ApiSweepGetPartnerStores()
	return __defult(met, p, t)
def searchCenterApi_GoodsSearchSearchGoodsByTradeCodes(p, t):
	met = searchCenterApi.GoodsSearchSearchGoodsByTradeCodes()
	return __defult(met, p, t)
def searchCenterApi_WordSuggesterExist(p, t):
	met = searchCenterApi.WordSuggesterExist()
	return __defult(met, p, t)
def searchCenterApi_WelfareGoodsSearchGoodsAll(p, t):
	met = searchCenterApi.WelfareGoodsSearchGoodsAll()
	return __defult(met, p, t)
def searchCenterApi_WelfareGoodsSuggester(p, t):
	met = searchCenterApi.WelfareGoodsSuggester()
	return __defult(met, p, t)
def financeBusinessApi_userUuid(p, t):
	met = financeBusinessApi.userUuid()
	return __defult(met, p, t)
def financeBusinessApi_transactionOrdersPaging(p, t):
	met = financeBusinessApi.transactionOrdersPaging()
	return __defult(met, p, t)
def O2OPlaceTheOrderApi_AdminApiExpressSetExpressRule(p, t):
	met = O2OPlaceTheOrderApi.AdminApiExpressSetExpressRule()
	return __defult(met, p, t)
def promoteCenterApi_CardQueryMyRecord(p, t):
	met = promoteCenterApi.CardQueryMyRecord()
	return __defult(met, p, t)
def promoteCenterApi_CardSendCard(p, t):
	met = promoteCenterApi.CardSendCard()
	return __defult(met, p, t)
def promoteCenterApi_TrialQueryActivity(p, t):
	met = promoteCenterApi.TrialQueryActivity()
	return __defult(met, p, t)
def promoteCenterApi_CcardQueryCardDetail(p, t):
	met = promoteCenterApi.CcardQueryCardDetail()
	return __defult(met, p, t)
def promoteCenterApi_CardQueryCardAmount(p, t):
	met = promoteCenterApi.CardQueryCardAmount()
	return __defult(met, p, t)
def promoteCenterApi_OutSchemeDetailInfo(p, t):
	met = promoteCenterApi.OutSchemeDetailInfo()
	return __defult(met, p, t)
def promoteCenterApi_CardBatchQuery(p, t):
	met = promoteCenterApi.CardBatchQuery()
	return __defult(met, p, t)
def promoteCenterApi_OutSchemeDetailList(p, t):
	met = promoteCenterApi.OutSchemeDetailList()
	return __defult(met, p, t)
def promoteCenterApi_CardQueryProjectInfo(p, t):
	met = promoteCenterApi.CardQueryProjectInfo()
	return __defult(met, p, t)
def promoteCenterApi_CouponQuerySchemeInfo(p, t):
	met = promoteCenterApi.CouponQuerySchemeInfo()
	return __defult(met, p, t)
def promoteCenterApi_InfoCheckGoods(p, t):
	met = promoteCenterApi.InfoCheckGoods()
	return __defult(met, p, t)
def promoteCenterApi_OutSchemeQuerySchemeAndTag(p, t):
	met = promoteCenterApi.OutSchemeQuerySchemeAndTag()
	return __defult(met, p, t)
def promoteCenterApi_CardQueryGiftDetail(p, t):
	met = promoteCenterApi.CardQueryGiftDetail()
	return __defult(met, p, t)
def promoteCenterApi_LockLockCard(p, t):
	met = promoteCenterApi.LockLockCard()
	return __defult(met, p, t)
def promoteCenterApi_OutSchemeSchemeInfo(p, t):
	met = promoteCenterApi.OutSchemeSchemeInfo()
	return __defult(met, p, t)
def promoteCenterApi_OutSchemeSchemeAndRule(p, t):
	met = promoteCenterApi.OutSchemeSchemeAndRule()
	return __defult(met, p, t)
def promoteCenterApi_TrialActivityTrial(p, t):
	met = promoteCenterApi.TrialActivityTrial()
	return __defult(met, p, t)
def promoteCenterApi_CardBatchMerchantQuery(p, t):
	met = promoteCenterApi.CardBatchMerchantQuery()
	return __defult(met, p, t)
def promoteCenterApi_DeductCouponDeductPayBackNotice(p, t):
	met = promoteCenterApi.DeductCouponDeductPayBackNotice()
	return __defult(met, p, t)
def promoteCenterApi_DeductCouponVerification(p, t):
	met = promoteCenterApi.DeductCouponVerification()
	return __defult(met, p, t)
def promoteCenterApi_OutRateQueryRate(p, t):
	met = promoteCenterApi.OutRateQueryRate()
	return __defult(met, p, t)
def promoteCenterApi_DeductCouponCouponTrialForOrder(p, t):
	met = promoteCenterApi.DeductCouponCouponTrialForOrder()
	return __defult(met, p, t)