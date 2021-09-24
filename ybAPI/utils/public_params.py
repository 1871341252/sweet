from utils.get_sign import *
from utils.get_token import *

get_sign=Sign()
get_token=Token()

class Public:
    """获取公共参数类"""
    def get_userinfo(self):
        access_token=get_token.get_user_token('13999990007','123456')
        sign_token=get_sign.get_sign(access_token)
        return access_token,sign_token

    def public_params(self):
        """获取公共参数返回"""
        res_temp=self.get_userinfo()
        times=res_temp[1][0]
        sign=res_temp[1][1]
        access_token=res_temp[0]
        public_params={
            'public_oaid':(None,'7dfc2dc3-8bc2-4092-8dfb-d38a9366b267'),
            'public_app_id':(None,'1'),
            'public_app_version':(None,'1.3.0'),
            'public_app_version_code':(None,'30'),
            'public_android_id':(None,'9cef2d09b8f32ab0'),
            'public_app_os':(None,'Android'),
            'timestamp':(None,times),
            'yuan_api_sign':(None,sign),
            'access_token':(None,access_token)
            }
        return public_params
