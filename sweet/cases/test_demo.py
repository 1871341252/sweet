import pytest
import pytest_ordering
import pytest_rerunfailures

class TestCases:
    age=18

    #装饰器改变用例执行的顺序(order=2)
    @pytest.mark.run(order=2)
    #装饰器给用例进行分组cat
    @pytest.mark.cat
    def test_01_demo2(self):
        print("第六个用例")

    #装饰器改变用例执行的顺序(order=1)
    @pytest.mark.run(order=1)
    #装饰器给用例进行分组dog
    @pytest.mark.dog
    #装饰器实现有条件跳过测试用例
    @pytest.mark.skipif(age>=18,reason="已成年")
    def test_02_demo2(self):
        print("第七个用例")

    @pytest.mark.run(order=3)
    @pytest.mark.dog
    def test_03_demo1(self):
        print("第八个用例")
        # assert 1==2

    @pytest.mark.run(order=5)
    @pytest.mark.cat
    def test_04_demo1(self):
        print("第九个用例")

    @pytest.mark.run(order=4)
    @pytest.mark.cat
    #装饰器实现无条件跳过测试用例
    @pytest.mark.skip(reason="无条件跳过")
    def test_05_demo1(self):
        print("第十个用例")

# if __name__ == "__main__":
#     pytest.main(['-vs','./cases'])

#运行参数详解
#-s: 表示输出调试信息，包括print打印的信息
#-v: 显示更详细的信息
#-vs: 两参数可以一起使用
#-n: 支持多线程或者分布式运行测试用例（'-n=2'）
#--reruns: 失败用例重跑（'--reruns=2'）
#-x: 表示只要有一个用例报错就停止测试，后面的用例不运行
#--maxfail: 出现两个失败用例就停止（'--maxfail=2'）
#-k:根据测试用例名称的部分字符串运行测试用例（'-k=demo'）
#-m 实现分组，实际应用'-m=cat or dog'

