# -*- coding: utf-8 -*- 
# @Time : 2022/7/8 10:24 AM 
# @Author : feiyuanfeng 
# @File : statisticsRun.py 
# @Copyright : uniondrug
import os.path
from datetime import datetime
from time import localtime, strftime
from urllib.parse import quote

from Common.DingdingHandler import DingDingHandler


class statisticsRun:
    def __init__(self):
        pass

    def getEditTime(self,path):
        time = os.path.getmtime(path)
        edit_time_locale = localtime(time)
        format_time = strftime("%Y-%m-%d", edit_time_locale)
        return format_time

    def exportAllureRes(self,path):
        with open(path) as k:
            failed = 0
            passed = 0  # 第一行标题判断未失败，所以失败从-1开始
            lines = k.readlines()
            for i in range(lines.__len__()):
                if i==0:
                    continue
                else:
                    tmp = lines[i].replace('"', '').split(',')
                    failed = failed + int(tmp[3]) + int(tmp[4])
                    passed = passed + int(tmp[5]) + int(tmp[6]) + int(tmp[7])
            res_dict = {}
            res_dict['passed'] = passed
            res_dict['failed'] = failed
            return res_dict

    def exportMsRes(self,path):
        with open(path) as k:

            lines = k.readlines()
            res_dict = {}
            res_dict['passed'] = lines[2].replace('pass=','').replace('\n','')
            res_dict['failed'] = lines[1].replace('field=','').replace('\n','')
            res_dict['report_url'] =lines[3].replace('report=','').replace('\n','')
            return res_dict


if __name__ == '__main__':
    path='/var/lib/jenkins/workspace'
    ms_list=['连锁对接自动化测试','商品中心自动化测试']
    time1 = datetime.now().strftime('%Y-%m-%d')
    res_list=[]
    for root, dirs, files in os.walk(path):
        for d in dirs:
            if ms_list.__contains__(d):
                propfile_path=os.path.join(path, d, 'propfile.txt')
                if os.path.exists(propfile_path):
                    time2 = statisticsRun().getEditTime(propfile_path)
                    print('当前时间', time1)
                    print('自动化执行时间:', time2)
                    print('自动化报告路径:', propfile_path)
                    if time1 == time2:
                        res_dict=statisticsRun().exportMsRes(propfile_path)
                        runres_dict = {}
                        runres_dict['name'] = d
                        report_url='http://{}'.format(res_dict.get('report_url'))
                        runres_dict['report_url'] = 'dingtalk://dingtalkclient/page/link?url={}&pc_slide=false'.format(quote(report_url))
                        res_dict.pop('report_url')
                        runres_dict['result'] = res_dict
                        res_list.append(runres_dict)
                        print(runres_dict)


            else:
                if d.endswith('自动化测试'):
                    behaviors_path = os.path.join(path, d, 'allure-report/data/behaviors.csv')
                    if os.path.exists(behaviors_path):
                        time2 = statisticsRun().getEditTime(behaviors_path)
                        print('当前时间', time1)
                        print('自动化执行时间:', time2)
                        print('自动化报告路径:', behaviors_path)
                        if time1 == time2:
                            res_dict = statisticsRun().exportAllureRes(behaviors_path)
                            runres_dict = {}
                            runres_dict['name'] = d
                            runres_dict['result'] = res_dict
                            runres_dict[
                                'report_url'] = 'dingtalk://dingtalkclient/page/link?url=http://jenkins.qtp.uniondrug.net/job/{}/allure/&pc_slide=false'.format(
                                quote(d))
                            res_list.append(runres_dict)
                            print(runres_dict)

    totalsys=res_list.__len__()
    totalmum=0
    totalpassed=0
    totalfailed=0
    btns_list = []
    for file in res_list:
        totalpassed+=int(file.get('result').get('passed'))
        totalfailed+= int(file.get('result').get('failed'))
        btns_dict={}
        btns_dict['title']='{}:{}'.format(file.get('name'),file.get('result'))
        btns_dict['actionURL']=file.get('report_url')
        btns_list.append(btns_dict)
    totalmum = totalpassed+totalfailed

    #【药联】项目负责人群机器人
    my_secret1 = 'SEC410759732b3452394de0a1f76e5788dee340fcd9b60992ad2df7cd054f6f40eb'
    my_url1 = 'https://oapi.dingtalk.com/robot/send?access_token=283fbcfc1e1f791724ee77b4513e414a6fdd581897042ce845163f7ce397d7ed'

    #质量管理部机器人
    my_secret2 = 'SECfe71b3ed46d722bc656c50ba6e6d6d6881aaf021df477c89a1cb7e9e68b0387e'
    my_url2 = 'https://oapi.dingtalk.com/robot/send?access_token=79e3f86433ff83c3e79cf2ced96faba07c26181680de1d967f4dda9845361a15'

    my_data={}
    actionCard_dict = {}
    actionCard_dict['title']="{}自动化汇总报告".format(time1)
    actionCard_dict['text'] = "{}自动化执行项目{}个 \n\n 执行总用例数:{} \n\n 执行成功用例数:{} \n\n 执行失败用例数:{} \n\n 公用账户：uniondrug001/uniondrug001".format(time1,totalsys,totalmum,totalpassed,totalfailed)
    actionCard_dict['btnOrientation'] = '0'
    actionCard_dict['btns'] = btns_list
    my_data['msgtype']='actionCard'
    my_data['actionCard'] = actionCard_dict

    print(my_data)

    dingding1 = DingDingHandler(secret=my_secret1, url=my_url1)
    dingding1.send_meassage(my_data)

    dingding2 = DingDingHandler(secret=my_secret2, url=my_url2)
    dingding2.send_meassage(my_data)


