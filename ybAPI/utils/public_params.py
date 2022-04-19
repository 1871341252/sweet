from os import device_encoding
from utils.get_sign import *
from utils.get_token import *
from utils.public_tools import *

conf_temp=Tools().read_configure("public_conf/conf.ini")
user_conf=conf_temp.items("user")

# get_sign=Sign()
# get_token=Token()

class Public:
    # """获取公共参数类"""
    # def __init__(self,phone,code):
    #     """初始化方法"""
    #     self.phone=phone
    #     self.code=code

    def get_userinfo(self):
        token_data=Token().get_user_token(user_conf[0][1],user_conf[1][1])
        sign_token=Sign().get_sign(token_data[1])
        return token_data,sign_token

    def public_params(self):
        """获取公共参数返回"""
        res_temp=self.get_userinfo()
        times=res_temp[1][0]
        sign=res_temp[1][1]
        device_token=res_temp[0][0]
        access_token=res_temp[0][1]
        public_params={
            'public_oaid':(None,'7dfc2dc3-8bc2-4092-8dfb-d38a9366b267'),
            'public_app_id':(None,'1'),
            'public_app_version':(None,'1.3.0'),
            'public_app_version_code':(None,'30'),
            'public_android_id':(None,'9cef2d09b8f32ab0'),
            'public_app_os':(None,'Android'),
            'public_device_token':(None,device_token),
            'shumei_device_id':(None,'BhN5EywFhYjb8pJXjD5UCAULN0ryV4BcxXX0okynGdUF+'),
            'timestamp':(None,times),
            'yuan_api_sign':(None,sign),
            'access_token':(None,access_token)
            }
        # print(public_params)
        return public_params
