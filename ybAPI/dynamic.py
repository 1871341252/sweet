import requests
import pytest
import allure
from utils.log import logging
from utils.get_sign import *
from utils.get_token import *
from utils.tools import *
from ddt import ddt,data,unpack

get_sign=Sign()
get_token=Token()
db=Db("121.5.7.158",3306,"yuanban","xpvhafO26ghDwU3aa","yuanban_api")

public_params={
    'public_oaid':(None,'7dfc2dc3-8bc2-4092-8dfb-d38a9366b267'),
    'public_app_id':(None,'1'),
    'public_app_version':(None,'1.3.0'),
    'public_app_version_code':(None,'30'),
    'public_android_id':(None,'9cef2d09b8f32ab0'),
    'public_app_os':(None,'Android')
    }

class TestCases:

    # # @data("selected","time","follow")
    # def test_dynamic_list(self):
    #     access_token=get_token.get_user_token('13999990003','123456')
    #     sign_token=get_sign.get_sign(access_token)
    #     times=sign_token[0]
    #     sign=sign_token[1]
    #     url="https://api.test.xiangcaohuyu.com/v1/user/Shortposts/newList"
    #     data={
    #         'timestamp':times,
    #         'yuan_api_sign':sign,
    #         'access_token':access_token,
    #         'page':'1',
    #         'pagesize':'20',
    #         'follow':'time'
    #     }
    #     res=requests.post(url,data=data,files=public_params)
    #     logging.info(res.json()["m"])
    #     print(res.json()["m"])
    #     assert res.json()["c"]==0

    # def test_dynamic_contentdelete(self):
    #     """动态评论删除接口"""
    #     access_token=get_token.get_user_token('13999990003','123456')
    #     sign_token=get_sign.get_sign(access_token)
    #     times=sign_token[0]
    #     sign=sign_token[1]
    #     url="https://api.test.xiangcaohuyu.com/v1/user/Shortposts/newDeletesHortPostsComment"
    #     comment_id_temp=db.query("SELECT comment_id FROM short_posts_comment WHERE comment_content='测试啊' ORDER BY comment_id LIMIT 1")
    #     comment_id=comment_id_temp[0][0]
    #     print(comment_id)
    #     data={
    #         'timestamp':times,
    #         'yuan_api_sign':sign,
    #         'access_token':access_token,
    #         'posts_id':'184',
    #         'comment_id':comment_id
    #     }
    #     res=requests.post(url,data=data,files=public_params)
    #     logging.info(res.json()["m"])
    #     print(res.json())
    #     assert res.json()["c"]==0

    def test_dynamic(self):
        """发布动态接口"""
        global post_id
        access_token=get_token.get_user_token('13999990003','123456')
        sign_token=get_sign.get_sign(access_token)
        times=sign_token[0]
        sign=sign_token[1]
        url="https://api.test.xiangcaohuyu.com/v1/user/Shortposts/newAddPosts"
        # comment_id_temp=db.query("SELECT comment_id FROM short_posts_comment WHERE comment_content='测试啊' ORDER BY comment_id LIMIT 1")
        # comment_id=comment_id_temp[0][0]
        # print(comment_id)
        data={
            'timestamp':times,
            'yuan_api_sign':sign,
            'access_token':access_token,
            'post_content':'测试啊',
            'post_type':'image',
            'images':'https://yuanban-1303879345.file.myqcloud.com/image/community/2021/09/03/651_android_1630663195635.png',
            'short_posts_city':'深圳市'
        }
        res=requests.post(url,data=data,files=public_params)
        post_id_temp=db.query("SELECT short_posts_id FROM short_posts WHERE short_posts_word='测试啊' ORDER BY short_posts_id DESC LIMIT 1")
        post_id=post_id_temp[0][0]
        print(post_id)
        logging.info(res.json()["m"])
        print(res.json())
        assert res.json()["c"]==0

    # # @pytest.mark.parametrize('args',[184])
    # @pytest.mark.run(order=8)
    # @allure.step(title="动态删除接口")
    # @allure.title("动态删除接口")
    # def test_dynamic_delete(self):
    #     """删除动态接口"""
    #     access_token=get_token.get_user_token('13999990003','123456')
    #     sign_token=get_sign.get_sign(access_token)
    #     times=sign_token[0]
    #     sign=sign_token[1]
    #     url="https://api.test.xiangcaohuyu.com/v1/user/Shortposts/newDeleteShortPost"
    #     data={
    #         'timestamp':times,
    #         'yuan_api_sign':sign,
    #         'access_token':access_token,
    #         'posts_id':post_id,
    #     }
    #     res=requests.post(url,data=data,files=public_params)
    #     logging.info(res.json()["m"])
    #     print(res.json())
    #     assert res.json()["c"]==0

    # @pytest.mark.run(order=7)
    # @allure.step(title="动态消息列表")
    # @allure.title("动态消息列表")
    # def test_dynamic_MessageList(self):
    #     """动态消息列表接口"""
    #     access_token=get_token.get_user_token('13999990007','123456')
    #     sign_token=get_sign.get_sign(access_token)
    #     times=sign_token[0]
    #     sign=sign_token[1]
    #     url="https://api.test.xiangcaohuyu.com/v1/user/Shortposts/newMessageList"
    #     data={
    #         'timestamp':times,
    #         'yuan_api_sign':sign,
    #         'access_token':access_token,
    #         'page':'1',
    #     }
    #     res=requests.post(url,data=data,files=public_params)
    #     print(res.json())
    #     print(res.json()["d"]["list"][0]["message_id"])
    #     logging.info(res.json()["m"])
    #     assert res.json()["c"]==0

    # @pytest.mark.parametrize("report_reason,reason_details,reason_details_imgs", ("test", "test", "test"))
    @pytest.mark.run(order=10)
    @allure.step(title="举报动态")
    @allure.title("举报动态")
    def test_dynamic_DeleteMessage(self):
        """举报动态"""
        access_token=get_token.get_user_token('13999990003','123456')
        sign_token=get_sign.get_sign(access_token)
        times=sign_token[0]
        sign=sign_token[1]
        url="https://api.test.xiangcaohuyu.com/v1/user/Shortposts/newReport"
        data={
            'timestamp':times,
            'yuan_api_sign':sign,
            'access_token':access_token,
            'posts_id':post_id,
            'report_reason':'report_reason',
            'reason_details':'reason_details',
            'reason_details_imgs':'reason_details_imgs'
        }
        res=requests.post(url,data=data,files=public_params)
        print(res.json())
        logging.info(res.json()["m"])
        assert res.json()["c"]==0


test=TestCases()
# test.test_dynamic_list()
# test.test_dynamic_contentdelete()
# test.test_dynamic()
test.test_dynamic()
# test.test_dynamic_delete()
# test.test_dynamic_MessageList()
test.test_dynamic_DeleteMessage()