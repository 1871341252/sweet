from logging import info
from utils.appium_tools import Runappium
from utils.app_log import logging
from utils.mysql_tools import Db
import pytest
import allure

db=Db("39.100.88.180",3306,"voice","xpvhafO26ghDwU3a","voice_api")

run=Runappium()
class TestCases:
    @pytest.mark.run(order=1)
    @allure.step(title="派对房间发送快捷消息的方法")
    @allure.title("进入派对操作")
    def test_01_demo(self):
        """派对房间内发消息，送礼物，上麦，下麦，发表情等"""
        public=run.wait(30)
        step2=run.clicking("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.ImageView')
        logging.info("进入派对")
        step3=run.clicking("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[5]/android.widget.TextView')
        logging.info("切换点唱")
        # step4=run.clicking("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[2]')
        step4=run.clicking("id","com.yuyin.live.voice:id/llRoot")
        logging,info("进入房间")
        step6=run.clicking("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageView')
        logging,info("上一号麦")
        step7=run.clicking("id","com.yuyin.live.voice:id/ivEmotion")
        logging.info("拉起表情栏")
        step8=run.clicking("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView')
        logging.info("发送表情")
        step9=run.clicking("id","com.yuyin.live.voice:id/mIvGift")
        logging,info("拉起礼物栏")
        step10=run.clicking("id","com.yuyin.live.voice:id/mIvImg")
        logging,info("选择送礼物的对象")
        step11=run.clicking("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[4]/android.widget.ImageView')
        logging,info("选择礼物")
        step12=run.clicking("id","com.yuyin.live.voice:id/mTvSend")
        logging,info("赠送礼物")
        step13=run.clicking("id","com.yuyin.live.voice:id/mRlGoMic")
        logging.info("下麦")
        step14=run.clicking("id",'com.yuyin.live.voice:id/mIvPublicChat')
        logging.info("拉起消息框")
        step15=run.clicking("id","com.yuyin.live.voice:id/mEtContent")
        step16=run.input_text("id","com.yuyin.live.voice:id/mEtContent","以爱之名")
        logging.info("输入消息文本")
        step17=run.clicking("id","com.yuyin.live.voice:id/mTvSend")
        logging.info("发送消息")
        step18=run.assert_text("xpath",'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.TextView[3]')
        # print(step18)
        temp=db.query("SELECT * FROM room WHERE room_id =168")
        res=temp[0][2]
        # sleep=run.wait_sleep(5)
        end=run.quit_app()
        logging.info("退出App")
        assert step18 == res,"元素的text值与数据库一致即用例通过"
        