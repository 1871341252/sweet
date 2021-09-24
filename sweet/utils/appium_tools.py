from appium import webdriver
import time

def get_driver():
    """
        获取设备driver
    """
    desired_caps = {}
    desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
    desired_caps['platformVersion'] = '10'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
    desired_caps['deviceName'] = 'TAS-AN00'                # 手机/模拟器的型号：adb shell getprop ro.product.model
    desired_caps['appPackage'] = 'com.android.permissioncontroller'               # app的名字：
                                                            # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
                                                            # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
    desired_caps['appActivity'] = 'com.android.packageinstaller.permission.ui.GrantPermissionsActivity'              # 同上↑
    desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
    desired_caps['resetKeyboard'] = True                     # 设置成appium自带的键盘
    desired_caps['noReset'] = True                    # 设置保存登录或其他信息
    # 去打开app，并且返回当前app的操作对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
    
class Runappium:
    def __init__(self):
        """ 初始化类 """
        self.driver=get_driver()

    def input_text(self,locator_type,locator,text):
        """ 输入值的方法 """
        if locator_type=='xpath':
            self.driver.find_element_by_xpath(locator).send_keys(text)
        elif locator_type=='id':
            self.driver.find_element_by_id(locator).send_keys(text)
        elif locator_type=='name':
            self.driver.find_element_by_name(locator).send_keys(text)
        elif locator_type=='class_name':
            self.driver.find_element_by_class_name(locator).send_keys(text)
        #link_text用于定位超链接的全部文本值
        elif locator_type=='link_text':
            self.driver.find_element_by_link_text(locator).send_keys(text)
        # #partial_link_text用于定位超链接的部分文本值
        # elif locator_type=='partial_link_text':
        #     self.driver.find_element_by_partial_link_text(locator).send_keys(text)
        # #通过元素的标签名来定位元素，如：input标签、span标签
        # elif locator_type=='tag_name':
        #     self.driver.find_element_by_tag_name(locator).send_keys(text)
        # #通过组合的方式进行定位
        # elif locator_type=='css_selector':
        #     self.driver.find_element_by_css_selector(locator).send_keys(text)

    def clear(self,locator_type,locator):
        """ 清空输入框中原始值的方法 """
        if locator_type=='xpath':
            self.driver.find_element_by_xpath(locator).clear()
        elif locator_type=='id':
            self.driver.find_element_by_id(locator).clear()
        elif locator_type=='name':
            self.driver.find_element_by_name(locator).clear()
        elif locator_type=='class_name':
            self.driver.find_element_by_class_name(locator).clear()
        if locator_type=='link_text':
            self.driver.find_element_by_link_text(locator).clear()
        # elif locator_type=='partial_link_text':
        #     self.driver.find_element_by_partial_link_text(locator).clear()
        # elif locator_type=='tag_name':
        #     self.driver.find_element_by_tag_name(locator).clear()
        # elif locator_type=='css_selector':
        #     self.driver.find_elements_by_css_selector(locator).clear()

    def clicking(self,locator_type,locator):
        """ 点击的方法 """
        if locator_type=='xpath':
            self.driver.find_element_by_xpath(locator).click()
        elif locator_type=='id':
            self.driver.find_element_by_id(locator).click()
        elif locator_type=='name':
            self.driver.find_element_by_name(locator).click()
        elif locator_type=='class_name':
            self.driver.find_element_by_class_name(locator).click()
        elif locator_type=='link_text':
            self.driver.find_element_by_link_text(locator).click()
        # elif locator_type=='partial_link_text':
        #     self.driver.find_element_by_partial_link_text(locator).click()
        # elif locator_type=='tag_name':
        #     self.driver.find_element_by_tag_name(locator).click()
        # elif locator_type=='css_selector':
        #     self.driver.find_elements_by_css_selector(locator).click()

    def wait_sleep(self,secoeds):
        """ 强制等待的方法 """
        time.sleep(secoeds)
    
    def wait(self,secoeds):
        """ 隐形等待的方法 """
        self.driver.implicitly_wait(secoeds)
    
    def assert_text(self,locator_type,locator):
        """ 断言(获取)某个元素的值的方法 """
        if locator_type=='xpath':
            element_text=self.driver.find_element_by_xpath(locator).text
        elif locator_type=='id':
            element_text=self.driver.find_element_by_id(locator).text
        elif locator_type=='name':
            element_text=self.driver.find_element_by_name(locator).text
        elif locator_type=='class_name':
            element_text=self.driver.find_element_by_class_name(locator).text
        elif locator_type=='link_text':
            element_text=self.driver.find_element_by_link_text(locator).text
        # elif locator_type=='partial_link_text':
        #     element_text=self.driver.find_element_by_partial_link_text(locator).text
        # elif locator_type=='tag_name':
        #     element_text=self.driver.find_element_by_tag_name(locator).text
        # elif locator_type=='css_selector':
        #     element_text=self.driver.find_elements_by_css_selector(locator).text
        return element_text

    def assert_title(self):
        """ 断言窗体标题的方法 """
        # wins = self.driver.window_handles
        # self.driver.switch_to.window(wins[0])
        title=self.driver.title
        return title

    def get_text(self,locator_type,locator):
        """ 获取某个元素的属性或获取文本框内容的方法 """
        if locator_type=='xpath':
            get_text=self.driver.find_element_by_xpath(locator).get_attribute('value')
        elif locator_type=='id':
            get_text=self.driver.find_element_by_id(locator).get_attribute('value')
        elif locator_type=='name':
            get_text=self.driver.find_element_by_name(locator).get_attribute('value')
        elif locator_type=='class_name':
            get_text=self.driver.find_element_by_class_name(locator).get_attribute('value')
        elif locator_type=='link_text':
            get_text=self.driver.find_element_by_link_text(locator).get_attribute('value')
        # elif locator_type=='partial_link_text':
        #     get_text=self.driver.find_element_by_partial_link_text(locator).get_attribute('value')
        # elif locator_type=='tag_name':
        #     get_text=self.driver.find_element_by_tag_name(locator).get_attribute('value')
        # elif locator_type=='css_selector':
        #     get_text=self.driver.find_elements_by_css_selector(locator).get_attribute('value')
        return get_text

    def quit_app(self):
        """ 关闭app的方法 """
        self.driver.quit()

    def close_app(self):
        """ 关闭app的方法 """
        self.driver.close()

    def swipeUp(self,t,n):
        """向上滑动屏幕"""
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5     # x坐标
        y1 = l['height'] * 0.75   # 起始y坐标
        y2 = l['height'] * 0.25   # 终点y坐标
        for i in range(n):        # n为滑动的次数
            self.driver.swipe(x1, y1, x1, y2, t)   # t为滑动的时间
        
    def swipeDown(self,t,n):
        """向下滑动屏幕"""
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5          # x坐标
        y1 = l['height'] * 0.25        # 起始y坐标
        y2 = l['height'] * 0.75         # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2,t)
 
    def swipLeft(self,t,n):
        """向左滑动屏幕"""
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)
    
    def swipRight(self,t,n):
        """向右滑动屏幕"""
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    
       


