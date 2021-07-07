import pymysql
import xlrd

class Db:
    '''
    这是操作mysql数据库的类
    '''
    def __init__(self,host,port,username,password,dbname):
        self.host = host
        self.port=port
        self.user = username
        self.password = password
        self.db = dbname

    def query(self,sql):
        '''
        这是数据库查询的方法
        '''
        db = pymysql.connect(host=self.host,port=self.port,user=self.user,
            password=self.password,db=self.db) # 1、连接数据库
        cursor = db.cursor() # 2、获取数据库游标（就是光标）
        try:
            cursor.execute(sql) # 3、在游标中执行SQL语句,select
            res = cursor.fetchall() # 4、获取返回值
            db.close() # 5、关闭数据库连接
            return res
        except Exception as e:
            return "SQL语句错误，请检查后再输入！,{}".format(e)

    def commit(self,sql):
        '''
        这是数据库新增、修改、删除的方法
        '''
        db = pymysql.connect(host=self.host,user=self.user,
            password=self.password,db=self.db) # 1、连接数据库
        cursor = db.cursor() # 2、获取数据库游标（就是光标）
        try:
            cursor.execute(sql) # 3、在游标中执行SQL语句,可以执行insert update delete
            db.commit() # 4、应用
            db.close() # 5、关闭数据库连接
            return True
        except:
            return False

# run1=Db("192.168.50.11",3312,"root","szgr123","gre_study")
# run1.query("SELECT id FROM gre_video_comment WHERE accountId = 95442 ORDER BY createAt DESC LIMIT 1;")

def readexcle(exclename,sheetname):
    '''
    读取exlce表中的内容。返回值是一个二维数组
    '''
    excle = xlrd.open_workbook(exclename)
    table = excle.sheet_by_name(sheetname)
    rows = table.nrows
    tabledata = []
    for i in range(1,rows):
        tabledata.append(table.row_values(i))
    return tabledata


def createreport(value,x):
    with open("测试报告.txt",x) as f:
        f.write(value)

