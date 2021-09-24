from utils.get_token import *
from utils.get_sign import *
from utils.public_params import *

get_sign=Sign()
get_token=Token()
get_params=Public()

# public_params={
#     'public_oaid':(None,'7dfc2dc3-8bc2-4092-8dfb-d38a9366b267'),
#     'public_app_id':(None,'1'),
#     'public_app_version':(None,'1.3.0'),
#     'public_app_version_code':(None,'30'),
#     'public_android_id':(None,'9cef2d09b8f32ab0'),
#     'public_app_os':(None,'Android')
#     }

# def get_userinfo():
#     access_token=get_token.get_user_token('13999990007','123456')
#     sign_token=get_sign.get_sign(access_token)
#     # times=sign_token[0]
#     # sign=sign_token[1]
#     # return times,sign
#     return sign_token,access_token
class TestCases:
    def setup_class(self):
        print('\n开始执行')
        self.public_params=get_params.public_params()
        return self.public_params

    def teardown_class(self):
        print('\n测试结束')

    def test_message_index(self):
        """未读消息总数接口"""
        # public_params=get_params.public_params()
        # print(public_params)
        url="https://api.test.xiangcaohuyu.com/v1/user/message/index"
        # data={
        #     'timestamp':times,
        #     'yuan_api_sign':sign,
        #     'access_token':access_token,
        # }
        res=requests.post(url,files=self.public_params)
        # logging.info(res.json()["m"])
        print(res.json())
        # assert res.json()["c"]==0