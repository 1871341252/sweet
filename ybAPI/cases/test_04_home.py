import requests
import pytest
import allure
import urllib3
from utils.log import logging
from utils.get_sign import *
from utils.get_token import *
from utils.tools import *
from utils.public_params import *
from utils.public_tools import *

# 屏蔽requests的警告
urllib3.disable_warnings()

datalist=  readexcle("./data/首页模块接口测试用例.xls","Cases")
conf_temp=Tools().read_configure("public_conf/conf.ini")
mysql_conf=conf_temp.items("mysql")
db=Db(mysql_conf[0][1],int(mysql_conf[1][1]),mysql_conf[2][1],mysql_conf[3][1],mysql_conf[4][1])
url_conf=conf_temp.items("url")
#public_params=Public().public_params()

class TestCases:
    @classmethod
    def setup_class(cls):
        logging.info("开始执行")
        print('\n开始执行')
        cls.public_params=Public().public_params()
        return cls.public_params

    @classmethod
    def teardown_class(cls):
        logging.info("测试结束")
        print('\n测试结束')

    @pytest.mark.parametrize('args', [datalist[0][5]])
    @pytest.mark.run(order=1)
    @allure.step(title="首页信息")
    @allure.title("首页信息")
    def test_profile_index(self,args):
        """首页信息"""
        url=url_conf[0][1]+datalist[0][2]
        # print(self.public_params)
        res=requests.post(url,files=self.public_params,verify=False)
        logging.info(res.json()["m"])
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[1][5]])
    @pytest.mark.run(order=2)
    @allure.step(title="轮播图")
    @allure.title("轮播图")
    def test_get_banner(self,args):
        """获取轮播图"""
        url=url_conf[0][1]+datalist[1][2]
        print(self.public_params)
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logging.info(res.json()["m"])
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[2][5]])
    @pytest.mark.run(order=3)
    @allure.step(title="上电视")
    @allure.title("上电视")
    def test_profile_newUpTV(self,args):
        """上电视"""
        url=url_conf[0][1]+datalist[2][2]
        res=requests.post(url,files=self.public_params,verify=False)
        logging.info(res.json()["m"])
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[3][5]])
    @pytest.mark.run(order=4)
    @allure.step(title="礼物列表")
    @allure.title("礼物列表")
    def test_user_GiftList(self,args):
        """礼物列表"""
        url=url_conf[0][1]+datalist[3][2]
        res=requests.post(url,files=self.public_params,verify=False)
        logging.info(res.json()["m"])
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[4][5]])
    @pytest.mark.run(order=5)
    @allure.step(title="搜索列表")
    @allure.title("搜索列表")
    def test_user_searchList(self,args):
        """搜索列表"""
        url=url_conf[0][1]+datalist[4][2]
        res=requests.post(url,files=self.public_params,verify=False)
        logging.info(res.json()["m"])
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[5][5]])
    @pytest.mark.run(order=6)
    @allure.step(title="搜索")
    @allure.title("搜索")
    def test_user_search(self,args):
        """搜索"""
        url=url_conf[0][1]+datalist[5][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logging.info(res.json()["m"])
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', (datalist[6][5],datalist[7][5],datalist[8][5]))
    @pytest.mark.run(order=7)
    @allure.step(title="亲密度排行榜")
    @allure.title("亲密度排行榜")
    def test_user_RankingList(self,args):
        """亲密度排行榜"""
        url=url_conf[0][1]+datalist[6][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logging.info(res.json()["m"])
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[9][5]])
    @pytest.mark.run(order=8)
    @allure.step(title="签到")
    @allure.title("签到")
    def test_user_signinAdd(self,args):
        """签到"""
        url=url_conf[0][1]+datalist[9][2]
        # print(self.public_params)
        res=requests.post(url,files=self.public_params,verify=False)
        logging.info(res.json()["m"])
        assert res.json()["c"]==0