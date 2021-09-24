from appium import webdriver
from utils.appium_tools import Runappium
from appium.webdriver.common.touch_action import TouchAction
import time

run=Runappium()
# def get_driver():
#     """
#         获取设备driver
#     """
#     desired_caps = {}
#     desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
#     desired_caps['platformVersion'] = '10'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
#     desired_caps['deviceName'] = 'TAS-AN00'                # 手机/模拟器的型号：adb shell getprop ro.product.model
#     desired_caps['appPackage'] = 'com.android.permissioncontroller'               # app的名字：
#                                                             # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
#                                                             # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
#     desired_caps['appActivity'] = 'com.android.packageinstaller.permission.ui.GrantPermissionsActivity'              # 同上↑
#     desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
#     desired_caps['resetKeyboard'] = True                     # 设置成appium自带的键盘
#     desired_caps['noReset'] = True                    # 设置保存登录或其他信息
#     # 去打开app，并且返回当前app的操作对象
#     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#     return driver

def test():
    """
        查找单个元素
    """
    # driver=get_driver()
    # size = driver.get_window_size()
    # print(size)
    # # 屏幕宽度width
    # print(size['width'])
    # # 屏幕高度width
    # print(size['height'])
    run.swipeDown(500,1)
    run.quit_app()


    
if __name__ == "__main__":
    # for i in range(10):
    #     test()
    test()