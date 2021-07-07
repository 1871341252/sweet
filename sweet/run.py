import pytest
import os

if __name__ == "__main__":
    pytest.main()
    # os.system('allure generate ./temp -o ./report')

#报告需要用命令打开，本地浏览器无法打开
#allure open C:\pyapp\tapp\report
#addopts= -vs --reruns 2 --alluredir ./temp 可执行失败用例重跑