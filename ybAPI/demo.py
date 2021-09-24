from utils.get_sign import *
from utils.get_token import *
import time
import hashlib

# ApiToken="vGbtpRPSHPABISKr"
ApiToken="Gu0HHk3zVFOWovRG"
class Sign:
    # def get_time_stamp(self):
    #     """获得当前时间戳"""
    #     time_stamp=int(time.time())
    #     time_stamp_s=str(time_stamp)
    #     return time_stamp_s
    def get_sign(self,access_token,times):
        """获取当前时间戳的接口签名"""
        # print(self.get_time_stamp())
        # time=self.get_time_stamp()
        conent=(access_token+'_'+times+'_'+ApiToken)
        m=hashlib.md5()
        m.update(conent.encode())
        sign=m.hexdigest()
        print(m.hexdigest())
        return sign
    
get_sign=Sign()
res=get_sign.get_sign("v6iLARnwotO8K6Q4a0M092LMD34RUJFYmv1wF93BlvpQ0_xZEHHf.fqE4YhWi_FyYBciOhuEtWPHprUsIAoJ","1631584107")


get_token=Token()
get_token.get_user_token('13999990003','123456')
# get_sign=Sign()
# res=get_sign.get_sign("sjfsdfjsdf")
# print(res)
# print(res[0])
# print(res[1])
