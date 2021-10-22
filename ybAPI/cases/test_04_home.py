import requests
import pytest
import allure
from utils.log import logging
from utils.get_sign import *
from utils.get_token import *
from utils.public_params import *
from utils.tools import *

get_sign=Sign()
get_token=Token()
get_params=Public()
db=Db("121.5.7.158",3306,"yuanban","xpvhafO26ghDwU3aa","yuanban_api")

class TestCases:
    @classmethod
    def setup_class(cls):
        logging.info("开始执行")
        print('\n开始执行')
        cls.public_params=get_params.public_params()
        return cls.public_params

    @classmethod
    def teardown_class(cls):
        logging.info("测试结束")
        print('\n测试结束')

    @pytest.mark.run(order=1)
    @allure.step(title="推荐列表")
    @allure.title("推荐列表")
    def test_home_recommend(self):
        """首页推荐列表"""
        url="https://api.test.xiangcaohuyu.com/v1/user/user/newRecommendList"
        data={
            'page':'1',
            'pagesize':'20',
            'real_certification_flg':'M',
            'user_gender':'female',
            'user_birth':'1'
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.run(order=2)
    @allure.step(title="附近列表")
    @allure.title("附近列表")
    def test_home_nearby(self):
        """首页附近列表"""
        url="https://api.test.xiangcaohuyu.com/v1/user/user/newNearbyList"
        data={
            'page':'1',
            'pagesize':'20',
            'longitude':'113.952644',
            'latitude':'22.540617',
            'real_certification_flg':'M',
            'user_gender':'female',
            'user_birth':'1'
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        print(res.json())
        assert res.json()["c"]==0
