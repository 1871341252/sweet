import requests

public_params={
    'public_oaid':(None,'7dfc2dc3-8bc2-4092-8dfb-d38a9366b267'),
    'public_app_id':(None,'1'),
    'public_app_version':(None,'1.3.0'),
    'public_app_version_code':(None,'30'),
    'public_android_id':(None,'9cef2d09b8f32ab0'),
    'public_app_os':(None,'Android')
    }

class Token:
    """获取access_token类"""
    def get_devices_token(self):
        """获取设备token"""
        url="https://api.test.xiangcaohuyu.com/v1/app/basic/getDeviceToken"
        devices_token=requests.post(url,files=public_params)
        return devices_token

    def get_user_token(self,phone,code):
        """登录"""
        devices_token=self.get_devices_token()
        url="https://api.test.xiangcaohuyu.com/v1/account/login/index"
        data={
            'phone':phone,
            'code':code,
            'category':'phone',
            'public_device_token':devices_token.json()["d"]["device_token"]
        }
        access_token_temp=requests.post(url,data=data,files=public_params)
        access_token=str(access_token_temp.json()["d"]["access_token"])
        return access_token
        # print(access_token)