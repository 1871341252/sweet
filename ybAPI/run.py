import pytest
import os

if __name__ == "__main__":
    pytest.main()
    os.system('allure generate ./temp -o ./report')

#报告需要用命令打开，本地浏览器无法打开
#allure open D:\ybAPI\report
