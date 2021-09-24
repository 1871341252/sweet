import pytest
import requests
import json
from requests_toolbelt import MultipartEncoder

public_params={
    'public_oaid':(None,'7dfc2dc3-8bc2-4092-8dfb-d38a9366b267'),
    'public_app_id':(None,'1'),
    'public_app_version':(None,'1.3.0'),
    'public_app_version_code':(None,'30'),
    'public_android_id':(None,'9cef2d09b8f32ab0'),
    'public_app_os':(None,'Android')
    }
class TestCases:
    def setup_class(self):
        print('\n开始执行')

    def teardown_class(self):
        print('\n测试结束')
    
    def test_get_devices_token(self):
        global temp
        url="https://api.test.xiangcaohuyu.com/v1/app/basic/getDeviceToken"
        # data=MultipartEncoder(
        #     fields={
        #     # 'phone':'13999990003',
        #     # 'code':'123456',
        #     # 'category':'phone',
        #     'public_oaid':'7dfc2dc3-8bc2-4092-8dfb-d38a9366b267',
        #     'public_app_id':'1',
        #     'public_app_version':'1.3.0',
        #     'public_app_version_code':'30',
        #     'public_android_id':'9cef2d09b8f32ab0',
        #     # 'public_device_token':'4fd24aba-b9e7-4755-aadd-f1d91f1d5e48',
        #     'public_app_os':'Android'
        #     }
        # )
        # header={"Content-Type":data.content_type}
        temp=requests.post(url,files=public_params)
        res=temp.json()["d"]["device_token"]
        print(res)

    def test_login(self):
        url="https://api.test.xiangcaohuyu.com/v1/account/login/index"
        # data=MultipartEncoder(
        #     fields={
        #     'phone':'13999990003',
        #     'code':'123456',
        #     'category':'phone',
        #     'public_oaid':'7dfc2dc3-8bc2-4092-8dfb-d38a9366b267',
        #     'public_app_id':'1',
        #     'public_app_version':'1.3.0',
        #     'public_app_version_code':'30',
        #     'public_android_id':'9cef2d09b8f32ab0',
        #     'public_device_token':temp.json()["d"]["device_token"],
        #     'public_app_os':'Android'
        #     }
        # )
        data={
            'phone':'13999990003',
            'code':'123456',
            'category':'phone',
            'public_device_token':temp.json()["d"]["device_token"]
        }
        # header={"Content-Type":data.content_type}
        res=requests.post(url,data=data,files=public_params)
        print(res.json())
        # print(res)
        # print(json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=4))
