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

datalist=  readexcle("./data/动态模块接口测试用例.xls","Cases")
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

    @pytest.mark.parametrize('args', (datalist[0][5],datalist[1][5],datalist[2][5]))
    @pytest.mark.run(order=1)
    @allure.step(title="动态列表接口")
    @allure.title("动态列表接口")
    # 运行三遍，分别传入value的值
    def test_dynamic_list(self,args):
        """动态列表接口"""
        logger.info("---- {} ----".format(datalist[0][1]))
        url=url_conf[0][1]+datalist[0][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args',[datalist[3][5]])
    @pytest.mark.run(order=2)
    @allure.step(title="发布动态接口")
    @allure.title("发布动态接口")
    def test_dynamic_add(self,args):
        """发布动态接口"""
        logger.info("---- {} ----".format(datalist[3][1]))
        global post_id
        url=url_conf[0][1]+datalist[3][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        print(datalist[3][5])
        post_id_temp=db.query("SELECT short_posts_id FROM short_posts WHERE short_posts_word=%s ORDER BY short_posts_id DESC LIMIT 1",(eval(datalist[3][5])["post_content"]))
        post_id=post_id_temp[0][0]
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args',[datalist[4][5]])
    @pytest.mark.run(order=3)
    @allure.step(title="动态详情接口")
    @allure.title("动态详情接口")
    def test_dynamic_details(self,args):
        """动态详情接口"""
        logger.info("---- {} ----".format(datalist[4][1]))
        url=url_conf[0][1]+datalist[4][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args',[datalist[5][5]])
    @pytest.mark.run(order=4)
    @allure.step(title="动态点赞接口")
    @allure.title("动态点赞接口")
    def test_dynamic_good(self,args):
        """动态点赞接口"""
        logger.info("---- {} ----".format(datalist[5][1]))
        url=url_conf[0][1]+datalist[5][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args',[datalist[6][5]])
    @pytest.mark.run(order=5)
    @allure.step(title="动态评论列表接口")
    @allure.title("动态评论列表接口")
    def test_dynamic_Commentlist(self,args):
        """动态评论列表接口"""
        logger.info("---- {} ----".format(datalist[6][1]))
        url=url_conf[0][1]+datalist[6][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args',[datalist[7][5]])
    @pytest.mark.run(order=6)
    @allure.step(title="动态评论接口")
    @allure.title("动态评论接口")
    def test_dynamic_Comment(self,args):
        """动态评论接口"""
        logger.info("---- {} ----".format(datalist[7][1]))
        global comment_id
        url=url_conf[0][1]+datalist[7][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        comment_id_temp=db.query("SELECT comment_id FROM short_posts_comment WHERE comment_content=%s ORDER BY comment_id DESC LIMIT 1",(eval(datalist[3][5])["post_content"]))
        comment_id=comment_id_temp[0][0]
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args',[datalist[8][5]])
    @pytest.mark.run(order=7)
    @allure.step(title="动态消息列表")
    @allure.title("动态消息列表")
    def test_dynamic_MessageList(self,args):
        """动态消息列表接口"""
        logger.info("---- {} ----".format(datalist[8][1]))
        global message_id
        url=url_conf[0][1]+datalist[8][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        message_id=res.json()["d"]["list"][0]["message_id"]
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args',[datalist[9][5]])
    @pytest.mark.run(order=8)
    @allure.step(title="动态消息删除")
    @allure.title("动态消息删除")
    def test_dynamic_DeleteMessage(self,args):
        """动态消息删除接口"""
        logger.info("---- {} ----".format(datalist[9][1]))
        url=url_conf[0][1]+datalist[9][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0
    
    @pytest.mark.parametrize('args',[datalist[10][5]])
    @pytest.mark.run(order=9)
    @allure.step(title="举报动态")
    @allure.title("举报动态")
    def test_dynamic_DeleteMessage(self,args):
        """举报动态"""
        logger.info("---- {} ----".format(datalist[10][1]))
        url=url_conf[0][1]+datalist[10][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args',[datalist[11][5]])
    @pytest.mark.run(order=10)
    @allure.step(title="动态评论删除接口")
    @allure.title("动态评论删除接口")
    def test_dynamic_contentdelete(self,args):
        """动态评论删除接口"""
        logger.info("---- {} ----".format(datalist[11][1]))
        url=url_conf[0][1]+datalist[11][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0

    @pytest.mark.parametrize('args',[datalist[12][5]])
    @pytest.mark.run(order=11)
    @allure.step(title="动态删除接口")
    @allure.title("动态删除接口")
    def test_dynamic_delete(self,args):
        """删除动态接口"""
        logger.info("---- {} ----".format(datalist[12][1]))
        url=url_conf[0][1]+datalist[12][2]
        res=requests.post(url,data=eval(args),files=self.public_params,verify=False)
        logger.info(res.json()["m"])
        if res.json()["c"] != 0:
            logger.info(args)
            logger.info("接口结果为:{}".format(res.json()))
        assert res.json()["c"]==0