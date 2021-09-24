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
    @allure.step(title="系统消息接口")
    @allure.title("系统消息接口")
    def test_message_systemList(self):
        """系统消息接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/systemList"
        res=requests.post(url,files=self.public_params)
        logging.info(res.json()["m"])
        print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.run(order=2)
    @allure.step(title="用户消息接口")
    @allure.title("用户消息接口")
    def test_message_list(self):
        """用户消息接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/list"
        data={
            'page':'1',
            'pagesize':'20'
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.run(order=3)
    @allure.step(title="系统消息列表接口")
    @allure.title("系统消息列表接口")
    def test_message_system(self):
        """系统消息列表接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/system"
        res=requests.post(url,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.parametrize('value', ("1"))
    @pytest.mark.run(order=4)
    @allure.step(title="公告消息列表接口")
    @allure.title("公告消息列表接口")
    def test_message_systemNotification(self,value):
        """公告消息列表接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/systemNotification"
        data={
            'app_id':value
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.run(order=5)
    @allure.step(title="我关注的列表接口")
    @allure.title("我关注的列表接口")
    def test_message_FriendsFollowList(self):
        """我关注的列表接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/FriendsFollowList"
        data={
            'page':'1',
            'pagesize':'20'
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.run(order=6)
    @allure.step(title="互关的列表接口")
    @allure.title("互关的列表接口")
    def test_message_FriendsList(self):
        """互关的列表接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/FriendsList"
        data={
            'page':'1',
            'pagesize':'20'
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.run(order=7)
    @allure.step(title="关注我的列表接口")
    @allure.title("关注我的列表接口")
    def test_message_FriendsFansList(self):
        """关注我的列表接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/FriendsFansList"
        data={
            'page':'1',
            'pagesize':'20'
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.run(order=8)
    @allure.step(title="亲密关系列表接口")
    @allure.title("亲密关系列表接口")
    def test_message_intimacy(self):
        """亲密关系列表接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/intimacy"
        data={
            'page':'1',
            'pagesize':'20'
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0
    
    @pytest.mark.run(order=9)
    @allure.step(title="未读消息总数接口")
    @allure.title("未读消息总数接口")
    def test_message_index(self):
        """未读消息总数接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/index"
        res=requests.post(url,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.run(order=10)
    @allure.step(title="置顶消息接口")
    @allure.title("置顶消息接口")
    def test_message_top(self):
        """置顶消息接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/Topping"
        data={
            'to_user_id':'380'
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.run(order=11)
    @allure.step(title="聊天设置信息接口")
    @allure.title("聊天设置信息接口")
    def test_message_chatSettings(self):
        """聊天设置信息接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/chatSettings"
        data={
            'to_user_id':'380'
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.run(order=12)
    @allure.step(title="搭讪接口")
    @allure.title("搭讪接口")
    def test_message_sayHiPacket(self):
        """搭讪接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/sayHiPacket"
        data={
            'to_user_id':'380'
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.run(order=13)
    @allure.step(title="亲密度接口")
    @allure.title("亲密度接口")
    def test_message_intimacyPopup(self):
        """亲密度接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/intimacyPopup"
        data={
            'to_user_id':'380'
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.run(order=14)
    @allure.step(title="通话信息接口")
    @allure.title("通话信息接口")
    def test_message_privateChatInfo(self):
        """通话信息接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/privateChatInfo"
        data={
            'to_user_id':'380'
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.run(order=15)
    @allure.step(title="是否能私信接口")
    @allure.title("是否能私信接口")
    def test_message_privateLetterFlg(self):
        """是否能私信接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/privateLetterFlg"
        res=requests.post(url,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.parametrize('value', ("HelloWord","在干嘛","吃饭没"))
    @pytest.mark.run(order=16)
    @allure.step(title="打招呼接口")
    @allure.title("打招呼接口")
    def test_message_sayHi(self,value):
        """打招呼接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/sayHi"
        data={
            'to_user_id':'380',
            'say_hi_content':value
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.parametrize('value', ("11111","222222222","嘿嘿嘿嘿"))
    @pytest.mark.run(order=17)
    @allure.step(title="发消息接口")
    @allure.title("发消息接口")
    def test_message_send(self,value):
        """发消息接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/send"
        data={
            'to_user_id':'380',
            'msgType':'word',
            'content':value
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.run(order=18)
    @allure.step(title="邀请真人认证接口")
    @allure.title("邀请真人认证接口")
    def test_message_inviteRealCertification(self):
        """邀请真人认证接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/inviteRealCertification"
        data={
            'to_user_id':'380'
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.run(order=19)
    @allure.step(title="常用语列表接口")
    @allure.title("常用语列表接口")
    def test_message_sayHiList(self):
        """常用语列表接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/sayHiList"
        data={
            'to_user_id':'380'
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.parametrize('value', ("嘿嘿嘿嘿","哈哈哈哈"))
    @pytest.mark.run(order=20)
    @allure.step(title="增加常用语接口")
    @allure.title("增加常用语接口")
    def test_message_addUserSayHi(self,value):
        """增加常用语接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/addUserSayHi"
        data={
            'say_hi_content':value
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    @pytest.mark.parametrize('value', ("嘿嘿嘿嘿","哈哈哈哈"))
    @pytest.mark.run(order=21)
    @allure.step(title="删除常用语接口")
    @allure.title("删除常用语接口")
    def test_message_delUserSayHi(self,value):
        """删除常用语接口"""
        url="https://api.test.xiangcaohuyu.com/v1/user/message/delUserSayHi"
        data={
            'say_hi_content':value
        }
        res=requests.post(url,data=data,files=self.public_params)
        logging.info(res.json()["m"])
        # print(res.json())
        assert res.json()["c"]==0

    


    
    

    

    

    
    

    
