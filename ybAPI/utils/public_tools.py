import xlrd
import random
import configparser

class Tools:
    """公共的工具类"""
    # def __init__(self,min,max):
    #     """初始化变量""" #可作为全局变量使用
    #     self.min=min
    #     self.max=max

    def random_number(self,min,max):
        """获取随机数"""
        number=random.randint(min,max)
        number1=random.randrange(10)
        return number,number1

    def readexcle(exclename,sheetname):
        """读取exlce表中的内容。返回值是一个二维数组"""
        excle = xlrd.open_workbook(exclename)
        table = excle.sheet_by_name(sheetname)
        rows = table.nrows
        tabledata = []
        for i in range(1,rows):
            tabledata.append(table.row_values(i))
        return tabledata

    def read_configure(self,path):
        """读取配置文件"""
        config = configparser.ConfigParser()
        config.read(path)
        # print(config)
        return config