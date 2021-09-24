import time
import hashlib

ApiToken="Gu0HHk3zVFOWovRG"
class Sign:
    """获取接口签名类"""
    def get_time_stamp(self):
        """获取当前时间戳"""
        time_stamp=int(time.time())
        time_stamp_s=str(time_stamp)
        return time_stamp_s
    def get_sign(self,access_token):
        """获取当前时间戳的接口签名"""
        # print(self.get_time_stamp())
        time=self.get_time_stamp()
        conent=(str(access_token)+'_'+time+'_'+ApiToken)
        m=hashlib.md5()
        m.update(conent.encode())
        sign=m.hexdigest()
        # print(m.hexdigest())
        return (time,sign)

# test=Sign()
# test.get_sign("jsdfjskdfjksd")

    # def get_time_stamp():
    #     time_stamp=time.time()
    #     time_stamp_s=int(time_stamp)
    #     print(time_stamp_s)
    #     return str(time_stamp_s)
    # get_time_stamp()

    # a="ertrtrd"
    # c="gdfgdfg"

    # def md5():
    #     conent=(a+'_'+get_time_stamp()+'_'+c)
    #     # conent=(a+'_'+c)
    #     m=hashlib.md5()
    #     m.update(conent.encode())
    #     print(m.hexdigest())
    #     return m.hexdigest()
    #     # print(conent)
    # md5()
