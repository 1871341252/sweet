import requests
import pytest
import allure
import urllib3
from utils.log import *
from utils.get_sign import *
from utils.get_token import *
from utils.tools import *
from utils.public_params import *
from utils.public_tools import *

# 屏蔽requests的警告
urllib3.disable_warnings()

datalist=  readexcle("./data/消息模块接口测试用例.xls","Cases")
conf_temp=Tools().read_configure("public_conf/conf.ini")
mysql_conf=conf_temp.items("mysql")
db=Db(mysql_conf[0][1],int(mysql_conf[1][1]),mysql_conf[2][1],mysql_conf[3][1],mysql_conf[4][1])
url_conf=conf_temp.items("url")

class TestCases:
    @classmethod
    def setup_class(cls):
        logger.info("*************** 开始执行用例 ***************")
        print('\n开始执行')
        cls.public_params=Public().public_params()
        return cls.public_params

    @classmethod
    def teardown_class(cls):
        logger.info("*************** 结束执行用例 ***************")
        print('\n测试结束')

    @pytest.mark.parametrize('args', [datalist[0][5]])
    @pytest.mark.run(order=1)
    @allure.step(title="系统消息接口")
    @allure.title("系统消息接口")
    def test_message_systemList(self,args):
        """系统消息接口"""
        logger.info("---- {} ----".format(datalist[0][1]))
        url=url_conf[0][1]+datalist[0][2]
        res=requests.post(url,files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[1][5]])
    @pytest.mark.run(order=2)
    @allure.step(title="用户消息接口")
    @allure.title("用户消息接口")
    def test_message_list(self,args):
        """用户消息接口"""
        logger.info("---- {} ----".format(datalist[1][1]))
        url=url_conf[0][1]+datalist[1][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[2][5]])
    @pytest.mark.run(order=3)
    @allure.step(title="系统消息列表接口")
    @allure.title("系统消息列表接口")
    def test_message_system(self,args):
        """系统消息列表接口"""
        logger.info("---- {} ----".format(datalist[2][1]))
        url=url_conf[0][1]+datalist[2][2]
        res=requests.post(url,files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[3][5]])
    @pytest.mark.run(order=4)
    @allure.step(title="公告消息列表接口")
    @allure.title("公告消息列表接口")
    def test_message_systemNotification(self,args):
        """公告消息列表接口"""
        logger.info("---- {} ----".format(datalist[3][1]))
        url=url_conf[0][1]+datalist[3][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[4][5]])
    @pytest.mark.run(order=5)
    @allure.step(title="我关注的列表接口")
    @allure.title("我关注的列表接口")
    def test_message_FriendsFollowList(self,args):
        """我关注的列表接口"""
        logger.info("---- {} ----".format(datalist[4][1]))
        url=url_conf[0][1]+datalist[4][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[5][5]])
    @pytest.mark.run(order=6)
    @allure.step(title="互关的列表接口")
    @allure.title("互关的列表接口")
    def test_message_FriendsList(self,args):
        """互关的列表接口"""
        logger.info("---- {} ----".format(datalist[5][1]))
        url=url_conf[0][1]+datalist[5][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[6][5]])
    @pytest.mark.run(order=7)
    @allure.step(title="关注我的列表接口")
    @allure.title("关注我的列表接口")
    def test_message_FriendsFansList(self,args):
        """关注我的列表接口"""
        logger.info("---- {} ----".format(datalist[6][1]))
        url=url_conf[0][1]+datalist[6][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[7][5]])
    @pytest.mark.run(order=8)
    @allure.step(title="亲密关系列表接口")
    @allure.title("亲密关系列表接口")
    def test_message_intimacy(self,args):
        """亲密关系列表接口"""
        logger.info("---- {} ----".format(datalist[7][1]))
        url=url_conf[0][1]+datalist[7][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0
    
    @pytest.mark.parametrize('args', [datalist[8][5]])
    @pytest.mark.run(order=9)
    @allure.step(title="未读消息总数接口")
    @allure.title("未读消息总数接口")
    def test_message_index(self,args):
        """未读消息总数接口"""
        logger.info("---- {} ----".format(datalist[8][1]))
        url=url_conf[0][1]+datalist[8][2]
        res=requests.post(url,files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[9][5]])
    @pytest.mark.run(order=10)
    @allure.step(title="置顶消息接口")
    @allure.title("置顶消息接口")
    def test_message_top(self,args):
        """置顶消息接口"""
        logger.info("---- {} ----".format(datalist[9][1]))
        url=url_conf[0][1]+datalist[9][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[10][5]])
    @pytest.mark.run(order=11)
    @allure.step(title="聊天设置信息接口")
    @allure.title("聊天设置信息接口")
    def test_message_chatSettings(self,args):
        """聊天设置信息接口"""
        logger.info("---- {} ----".format(datalist[10][1]))
        url=url_conf[0][1]+datalist[10][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[11][5]])
    @pytest.mark.run(order=12)
    @allure.step(title="搭讪接口")
    @allure.title("搭讪接口")
    def test_message_sayHiPacket(self,args):
        """搭讪接口"""
        logger.info("---- {} ----".format(datalist[11][1]))
        url=url_conf[0][1]+datalist[11][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[12][5]])
    @pytest.mark.run(order=13)
    @allure.step(title="亲密度接口")
    @allure.title("亲密度接口")
    def test_message_intimacyPopup(self,args):
        """亲密度接口"""
        logger.info("---- {} ----".format(datalist[12][1]))
        url=url_conf[0][1]+datalist[12][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[13][5]])
    @pytest.mark.run(order=14)
    @allure.step(title="通话信息接口")
    @allure.title("通话信息接口")
    def test_message_privateChatInfo(self,args):
        """通话信息接口"""
        logger.info("---- {} ----".format(datalist[13][1]))
        url=url_conf[0][1]+datalist[13][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[14][5]])
    @pytest.mark.run(order=15)
    @allure.step(title="是否能私信接口")
    @allure.title("是否能私信接口")
    def test_message_privateLetterFlg(self,args):
        """是否能私信接口"""
        logger.info("---- {} ----".format(datalist[14][1]))
        url=url_conf[0][1]+datalist[14][2]
        res=requests.post(url,files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', (datalist[15][5],datalist[16][5],datalist[17][5]))
    @pytest.mark.run(order=16)
    @allure.step(title="打招呼接口")
    @allure.title("打招呼接口")
    def test_message_sayHi(self,args):
        """打招呼接口"""
        logger.info("---- {} ----".format(datalist[15][1]))
        time.sleep(5)
        url=url_conf[0][1]+datalist[15][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', (datalist[18][5],datalist[19][5],datalist[20][5]))
    @pytest.mark.run(order=17)
    @allure.step(title="发消息接口")
    @allure.title("发消息接口")
    def test_message_send(self,args):
        """发消息接口"""
        logger.info("---- {} ----".format(datalist[18][1]))
        time.sleep(5)
        url=url_conf[0][1]+datalist[18][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[21][5]])
    @pytest.mark.run(order=18)
    @allure.step(title="邀请真人认证接口")
    @allure.title("邀请真人认证接口")
    def test_message_inviteRealCertification(self,args):
        """邀请真人认证接口"""
        logger.info("---- {} ----".format(datalist[21][1]))
        url=url_conf[0][1]+datalist[21][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[22][5]])
    @pytest.mark.run(order=19)
    @allure.step(title="常用语列表接口")
    @allure.title("常用语列表接口")
    def test_message_sayHiList(self,args):
        """常用语列表接口"""
        logger.info("---- {} ----".format(datalist[22][1]))
        url=url_conf[0][1]+datalist[22][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', (datalist[23][5],datalist[24][5]))
    @pytest.mark.run(order=20)
    @allure.step(title="增加常用语接口")
    @allure.title("增加常用语接口")
    def test_message_addUserSayHi(self,args):
        """增加常用语接口"""
        logger.info("---- {} ----".format(datalist[23][1]))
        url=url_conf[0][1]+datalist[23][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', (datalist[25][5],datalist[26][5]))
    @pytest.mark.run(order=21)
    @allure.step(title="删除常用语接口")
    @allure.title("删除常用语接口")
    def test_message_delUserSayHi(self,args):
        """删除常用语接口"""
        logger.info("---- {} ----".format(datalist[25][1]))
        url=url_conf[0][1]+datalist[25][2]
        res=requests.post(url,data=eval(args),files=self.public_params)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0