import requests
import pytest
import allure
import urllib3
from utils.log import logging
from utils.get_sign import *
from utils.yaml_tools import *

# 屏蔽requests的警告
urllib3.disable_warnings()

get_sign=Sign()
login_data=YamlHandler("./data_yaml/login.yaml").read_yaml()

public_params={
    'public_oaid':(None,'7dfc2dc3-8bc2-4092-8dfb-d38a9366b267'),
    'public_app_id':(None,'1'),
    'public_app_version':(None,'1.3.0'),
    'public_app_version_code':(None,'30'),
    'public_android_id':(None,'9cef2d09b8f32ab0'),
    'public_app_os':(None,'Android'),
    'shumei_device_id':(None,'BhN5EywFhYjb8pJXjD5UCAULN0ryV4BcxXX0okynGdUF+')
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
        logging.info(devices_token.json()["m"])
        assert devices_token.json()["c"]==0
        
    @pytest.mark.run(order=2)
    @allure.step(title="登录")
    @allure.title("登录")
    def test_login(self):
        """登录"""
        global access_token_temp
        global access_token
        url="https://api.test.xiangcaohuyu.com/v1/account/login/index"
        data={
            'phone':login_data["login"]["phone"],
            'code':login_data["login"]["code"],
            'category':login_data["login"]["category"],
            'public_device_token':devices_token.json()["d"]["device_token"]
        }
        access_token_temp=requests.post(url,data=data,files=public_params)
        access_token=str(access_token_temp.json()["d"]["access_token"])
        logging.info(access_token_temp.json()["m"])
        assert access_token_temp.json()["c"]==0