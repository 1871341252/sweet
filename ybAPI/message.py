import requests
import pytest
import allure
from utils.log import logging
from utils.get_sign import *
from utils.get_token import *
from utils.tools import *
from ddt import ddt,data,unpack

get_sign=Sign()
get_token=Token()
db=Db("121.5.7.158",3306,"yuanban","xpvhafO26ghDwU3aa","yuanban_api")

public_params={
    'public_oaid':(None,'7dfc2dc3-8bc2-4092-8dfb-d38a9366b267'),
    'public_app_id':(None,'1'),
    'public_app_version':(None,'1.3.0'),
    'public_app_version_code':(None,'30'),
    'public_android_id':(None,'9cef2d09b8f32ab0'),
    'public_app_os':(None,'Android')
    }

class TestCases:
    def test_dynamic_details(self):
        """系统消息接口"""
        access_token=get_token.get_user_token('13999990003','123456')
        sign_token=get_sign.get_sign(access_token)
        times=sign_token[0]
        sign=sign_token[1]
        url="https://api.test.xiangcaohuyu.com/v1/user/message/systemList"
        data={
            'timestamp':times,
            'yuan_api_sign':sign,
            'access_token':access_token,
        }
        res=requests.post(url,data=data,files=public_params)
        logging.info(res.json()["m"])
        print(res.json())
        assert res.json()["c"]==0

    def test_message_user(self):
        """用户消息接口"""
        access_token=get_token.get_user_token('13999990003','123456')
        sign_token=get_sign.get_sign(access_token)
        times=sign_token[0]
        sign=sign_token[1]
        url="https://api.test.xiangcaohuyu.com/v1/user/message/list"
        data={
            'timestamp':times,
            'yuan_api_sign':sign,
            'access_token':access_token,
            'page':'1',
            'pagesize':'20'
        }
        res=requests.post(url,data=data,files=public_params)
        logging.info(res.json()["m"])
        print(res.json())
        assert res.json()["c"]==0

test=TestCases()
test.test_dynamic_details()
test.test_message_user()