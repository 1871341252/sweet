from selenium.webdriver.support.ui import WebDriverWait

def find_element(driver,locator,timeout=10):
    """
    参数
    driver 浏览器操作对象
    locator 元素定位方法 ("id" : "xxx")
    timeout 超长时间 timeout=10 默认超长时间为10
    """
    return WebDriverWait(driver,timeout).until(lambda s: s.find_element(*locator))


'''
Id="id"
Xpath='xpath'
Link_txt="link text"
Name="name"
class_name="class name"
'''