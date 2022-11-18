from selenium import webdriver
import time,os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import KeyWordDriver.CommonKeyWord as ckw


class TestZdao:
    def test_writeWorkCase(self):
        data = ckw.CommonKeyWord().Yaml_Read("TestFile/HaoRanOnly/zdao.yaml")
        # data = ckw.CommonKeyWord().Yaml_Read("/Users/liuhaoran/PycharmProjects/automan/TestFile/HaoRanOnly/zdao.yaml")
        pkw = ckw.CommonKeyWord().Yaml_GetByKey(data,"pkw")
        person = ckw.CommonKeyWord().Yaml_GetByKey(data,"person")
        jobTitle = ckw.CommonKeyWord().Yaml_GetByKey(data,"jobTitle")
        consumed = ckw.CommonKeyWord().Yaml_GetByKey(data,"consumed")
        left = ckw.CommonKeyWord().Yaml_GetByKey(data,"left")
        self.writeJobBase(pkw, person, jobTitle, consumed, left)

    def writeJobBase(self, pkw, person, jobTitle, consumed, left):
        binary_location = '/usr/bin/google-chrome'
        chrome_driver_binary = '/usr/bin/chromedriver'
        options = webdriver.ChromeOptions()
        options.binary_location = binary_location #谷歌地址
        options.add_argument('--no-sandbox')#解决DevToolsActivePort文件不存在的报错
        options.add_argument('window-size=1920x3000') #指定浏览器分辨率
        options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
        options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
        options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
        options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        chromedriver = chrome_driver_binary
        os.environ["webdriver.chrome.driver"] = chromedriver
        brower = webdriver.Chrome(chrome_options=options,executable_path=chromedriver)
        # brower = webdriver.Chrome()
        brower.get('http://pm.turboradio.cn/')
        brower.find_element_by_id("account").send_keys("liuhaoran")
        brower.find_element_by_name("password").send_keys("123456")
        brower.find_element_by_id("submit").click()
        time.sleep(1)
        brower.find_element_by_xpath("//*[@id=\"navbar\"]/ul/li[3]").click()
        brower.find_element_by_id("currentItem").click()
        time.sleep(2)
        a = brower.find_element_by_css_selector(
            "#dropMenu > div.list-group > div > div.table-col.col-left > div.list-group").text.split("\n")
        b = brower.find_element_by_css_selector(
            "#dropMenu > div.list-group > div > div.table-col.col-right > div").text.split("\n")
        times = 1
        flag = 1
        for p in a:
            if pkw in p:
                print(p, times)
                "#dropMenu > div.list-group > div > div.table-col.col-left > div.list-group > a.search-list-item.active"
                brower.find_element_by_css_selector(
                    "#dropMenu > div.list-group > div > div.table-col.col-left > div.list-group > a:nth-child(" + str(
                        times) + ")").click()
                flag = 0
                break
            times += 1
        if flag == 1:
            times = 1
            for p in b:
                if pkw in p:
                    print(p, times)
                    brower.find_element_by_css_selector(
                        "#dropMenu > div.list-group > div > div.table-col.col-right > div.list-group > a:nth-child(" + str(
                            times) + ")").click()
                    break
        # 选任务类型
        brower.find_element_by_xpath("//*[@id=\"mainMenu\"]/div[3]/a[3]").click()
        brower.find_element_by_xpath("//*[@id=\"type_chosen\"]").click()
        brower.find_element_by_xpath("//*[@id=\"type_chosen\"]/div/ul/li[5]").click()
        # 选指派人
        brower.find_element_by_xpath("//*[@id=\"assignedTo_chosen\"]").click()
        "//*[@id=\"assignedTo_chosen\"]/div/ul/li[5]"
        names = brower.find_element_by_xpath("//*[@id=\"assignedTo_chosen\"]/div/ul").text.split("\n")
        times2 = 1
        for name in names:
            if person == name:
                print(name)
                brower.find_element_by_xpath("//*[@id=\"assignedTo_chosen\"]/div/ul/li[" + str(times2) + "]").click()
                break
            times2 += 1
        # 写任务标题
        brower.find_element_by_id("name").send_keys(jobTitle)
        # 提交
        submit = brower.find_element_by_id("submit")
        brower.execute_script("arguments[0].click();", submit)
        time.sleep(2)
        brower.find_element_by_xpath("//*[@id=\"taskList\"]/tbody/tr[1]/td[12]/a[1]").click()
        brower.switch_to_frame("iframe-triggerModal")
        brower.find_element_by_id("consumed").send_keys(consumed)
        brower.find_element_by_id("left").clear()
        brower.find_element_by_id("left").send_keys(left)
        brower.find_element_by_id("submit").click()
        time.sleep(6)
