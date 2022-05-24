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

datalist=  readexcle("./data/首页模块接口测试用例.xls","Cases")
conf_temp=Tools().read_configure("public_conf/conf.ini")
mysql_conf=conf_temp.items("mysql")
db=Db(mysql_conf[0][1],int(mysql_conf[1][1]),mysql_conf[2][1],mysql_conf[3][1],mysql_conf[4][1])
url_conf=conf_temp.items("url")
#public_params=Public().public_params()

class TestCases:
    @classmethod
    def setup_class(cls):
        logger.info("*************** 开始执行用例 ***************")
        print('\n开始执行')
        cls.public_params=Public().public_params()
        return cls.public_params

    # @classmethod
    # def setup_method(cls):
    #     logger.info("*************** 开始执行用例 ***************")
    #     print('\n开始执行')
    #     cls.public_params=Public().public_params()
    #     return cls.public_params

    @classmethod
    def teardown_class(cls):
        logger.info("*************** 结束执行用例 ***************")
        print('\n测试结束')

    # @classmethod
    # def teardown_method(cls):
    #     logger.info("*************** 结束执行用例 ***************")
    #     print('\n测试结束')
    

    @pytest.mark.parametrize('args', [datalist[0][5]])
    @pytest.mark.run(order=1)
    @allure.step(title="首页信息")
    @allure.title("首页信息")
    def test_profile_index(self,args):
        """首页信息"""
        logger.info("---- {} ----".format(datalist[0][1]))
        url=url_conf[0][1]+datalist[0][2]
        # print(self.public_params)
        res=requests.post(url,files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[1][5]])
    @pytest.mark.run(order=2)
    @allure.step(title="轮播图")
    @allure.title("轮播图")
    def test_get_banner(self,args):
        """获取轮播图"""
        logger.info("---- {} ----".format(datalist[1][1]))
        url=url_conf[0][1]+datalist[1][2]
        # print(self.public_params)
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[2][5]])
    @pytest.mark.run(order=3)
    @allure.step(title="上电视")
    @allure.title("上电视")
    def test_profile_newUpTV(self,args):
        """上电视"""
        logger.info("---- {} ----".format(datalist[2][1]))
        url=url_conf[0][1]+datalist[2][2]
        res=requests.post(url,files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[3][5]])
    @pytest.mark.run(order=4)
    @allure.step(title="礼物列表")
    @allure.title("礼物列表")
    def test_user_GiftList(self,args):
        """礼物列表"""
        logger.info("---- {} ----".format(datalist[3][1]))
        url=url_conf[0][1]+datalist[3][2]
        res=requests.post(url,files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[4][5]])
    @pytest.mark.run(order=5)
    @allure.step(title="搜索列表")
    @allure.title("搜索列表")
    def test_user_searchList(self,args):
        """搜索列表"""
        logger.info("---- {} ----".format(datalist[4][1]))
        url=url_conf[0][1]+datalist[4][2]
        res=requests.post(url,files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[5][5]])
    @pytest.mark.run(order=6)
    @allure.step(title="搜索")
    @allure.title("搜索")
    def test_user_search(self,args):
        """搜索"""
        logger.info("---- {} ----".format(datalist[5][1]))
        url=url_conf[0][1]+datalist[5][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', (datalist[6][5],datalist[7][5],datalist[8][5]))
    @pytest.mark.run(order=7)
    @allure.step(title="亲密度排行榜")
    @allure.title("亲密度排行榜")
    def test_user_RankingList(self,args):
        """亲密度排行榜"""
        logger.info("---- {} ----".format(datalist[6][1]))
        url=url_conf[0][1]+datalist[6][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[9][5]])
    @pytest.mark.run(order=8)
    @allure.step(title="签到")
    @allure.title("签到")
    def test_user_signinAdd(self,args):
        """签到"""
        logger.info("---- {} ----".format(datalist[9][1]))
        url=url_conf[0][1]+datalist[9][2]
        res=requests.post(url,files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[10][5]])
    @pytest.mark.run(order=9)
    @allure.step(title="语音抢聊")
    @allure.title("语音抢聊")
    def test_rob_voice(self,args):
        """语音抢聊"""
        logger.info("---- {} ----".format(datalist[10][1]))
        global voice_enter_id
        url=url_conf[0][1]+datalist[10][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        voice_enter_id=res.json()["d"]["enter_id"]
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[11][5]])
    @pytest.mark.run(order=10)
    @allure.step(title="退出语音抢聊")
    @allure.title("退出语音抢聊")
    def test_exit_rob_voice(self,args):
        """退出语音抢聊"""
        logger.info("---- {} ----".format(datalist[11][1]))
        url=url_conf[0][1]+datalist[11][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[12][5]])
    @pytest.mark.run(order=11)
    @allure.step(title="视频抢聊")
    @allure.title("视频抢聊")
    def test_rob_video(self,args):
        """视频抢聊"""
        logger.info("---- {} ----".format(datalist[12][1]))
        time.sleep(10)
        global video_enter_id
        url=url_conf[0][1]+datalist[12][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        video_enter_id=res.json()["d"]["enter_id"]
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[13][5]])
    @pytest.mark.run(order=12)
    @allure.step(title="退出视频抢聊")
    @allure.title("退出视频抢聊")
    def test_exit_rob_video(self,args):
        """退出视频抢聊"""
        logger.info("---- {} ----".format(datalist[13][1]))
        url=url_conf[0][1]+datalist[13][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[14][5]])
    @pytest.mark.run(order=13)
    @allure.step(title="首页在线列表")
    @allure.title("首页在线列表")
    def test_RecommendList(self,args):
        """首页在线列表"""
        logger.info("---- {} ----".format(datalist[14][1]))
        url=url_conf[0][1]+datalist[14][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[15][5]])
    @pytest.mark.run(order=14)
    @allure.step(title="首页离线列表")
    @allure.title("首页离线列表")
    def test_offlineRecommendList(self,args):
        """首页离线列表"""
        logger.info("---- {} ----".format(datalist[15][1]))
        url=url_conf[0][1]+datalist[15][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[16][5]])
    @pytest.mark.run(order=15)
    @allure.step(title="首页附近列表")
    @allure.title("首页附近列表")
    def test_NearbyList(self,args):
        """首页附近列表"""
        logger.info("---- {} ----".format(datalist[16][1]))
        url=url_conf[0][1]+datalist[16][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', [datalist[17][5]])
    @pytest.mark.run(order=16)
    @allure.step(title="约会列表")
    @allure.title("约会列表")
    def test_indexNew(self,args):
        """约会列表"""
        logger.info("---- {} ----".format(datalist[17][1]))
        url=url_conf[0][1]+datalist[17][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', (datalist[18][5],datalist[19][5],datalist[20][5]))
    @pytest.mark.run(order=17)
    @allure.step(title="富豪榜")
    @allure.title("富豪榜")
    def test_FortuneList(self,args):
        """富豪榜"""
        logger.info("---- {} ----".format(datalist[18][1]))
        url=url_conf[0][1]+datalist[18][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args', (datalist[21][5],datalist[22][5],datalist[23][5]))
    @pytest.mark.run(order=18)
    @allure.step(title="女神榜")
    @allure.title("女神榜")
    def test_GlamourList(self,args):
        """女神榜"""
        logger.info("---- {} ----".format(datalist[21][1]))
        url=url_conf[0][1]+datalist[21][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0