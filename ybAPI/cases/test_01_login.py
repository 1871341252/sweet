import requests
import pytest
import allure
from utils.log import logging
from utils.get_sign import *

get_sign=Sign()

public_params={
    'public_oaid':(None,'7dfc2dc3-8bc2-4092-8dfb-d38a9366b267'),
    'public_app_id':(None,'1'),
    'public_app_version':(None,'1.3.0'),
    'public_app_version_code':(None,'30'),
    'public_android_id':(None,'9cef2d09b8f32ab0'),
    'public_app_os':(None,'Android')
    }

class TestCases:
    @classmethod
    def setup_class(cls):
        logging.info("开始执行")
        print('\n开始执行')

    @classmethod
    def teardown_class(cls):
        logging.info("测试结束")
        print('\n测试结束')
    
    @pytest.mark.run(order=1)
    @allure.step(title="获取设备token")
    @allure.title("获取设备token")
    def test_get_devices_token(self):
        """获取设备token"""
        global devices_token
        url="https://api.test.xiangcaohuyu.com/v1/app/basic/getDeviceToken"
        devices_token=requests.post(url,files=public_params)
        # res=devices_token.json()["d"]["device_token"]
        logging.info(devices_token.json()["m"])
        assert devices_token.json()["c"]==0
        # print(devices_token.json()["m"])
        # print(res)
        
    @pytest.mark.run(order=2)
    @allure.step(title="登录")
    @allure.title("登录")
    def test_login(self):
        """登录"""
        global access_token_temp
        global access_token
        url="https://api.test.xiangcaohuyu.com/v1/account/login/index"
        data={
            'phone':'13999990002',
            'code':'123456',
            'category':'phone',
            'public_device_token':devices_token.json()["d"]["device_token"]
        }
        access_token_temp=requests.post(url,data=data,files=public_params)
        access_token=str(access_token_temp.json()["d"]["access_token"])
        # print(access_token)
        logging.info(access_token_temp.json()["m"])
        assert access_token_temp.json()["c"]==0
        # print(access_token_temp.json())
        # print(access_token_temp.json()["d"]["access_token"])
        # print(access_token_temp.json()["m"])
        # print(res)
        # print(json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=4))

    @pytest.mark.run(order=3)
    @allure.step(title="首页信息")
    @allure.title("首页信息")
    def test_profile_index(self):
        """首页信息"""
        res=get_sign.get_sign(access_token)
        times=res[0]
        sign=res[1]
        url="https://api.test.xiangcaohuyu.com/v1/user/profile/index"
        data={
            'timestamp':times,
            'yuan_api_sign':sign,
            'access_token':access_token
        }
        res=requests.post(url,data=data,files=public_params)
        logging.info(res.json()["m"])
        assert res.json()["c"]==0

    @pytest.mark.run(order=4)
    @allure.step(title="轮播图")
    @allure.title("轮播图")
    def test_get_banner(self):
        """获取轮播图"""
        res=get_sign.get_sign(access_token)
        times=res[0]
        sign=res[1]
        url="https://api.test.xiangcaohuyu.com/v1/app/basic/carousel"
        data={
            'timestamp':times,
            'yuan_api_sign':sign,
            'access_token':access_token,
            'type':'message'
        }
        res=requests.post(url,data=data,files=public_params)
        logging.info(res.json()["m"])
        assert res.json()["c"]==0
