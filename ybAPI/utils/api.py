import requests
import json
from utils.tools import readexcle,createreport

host = "http://118.24.255.132:2333"
datalist=  readexcle("./data/接口测试用例.xlsx","Cases")

class requestsUtils:
    def post1(self,row):
        global res
        url = host + datalist[row][2]
        headers = eval(datalist[row][4])
        data = eval(datalist[row][5])
        res = requests.post(url,headers=headers,json=data)
        return res
    def get1(self,row):
        global res
        url = host + datalist[row][2]
        headers = eval(datalist[row][4])
        data = datalist[row][5]
        # if data != None:
        res = requests.get(url+"?"+data,headers=headers)
        return res
    
    # """request的post方法"""
    # def post_main(self,url,headers,data,judge_headers):
    #     global res
    #     if judge_headers == {'form-data'}:
    #         res = requests.post(url=url, data=data)
    #     if judge_headers == {'Content-type': 'application/x-www-form-urlencoded'}:
    #         res = requests.post(url=url,headers=headers,data=data)
    #     if judge_headers == {'Content-Type': 'application/json'}:
    #         res = requests.post(url=url,headers=headers, json=data)
    #     # return json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=4)
    #     #json.dumps()返回结果为格式化字符串，无法取值
    #     return res

    # def get_main(self,url,header,data):
    #     """request的get方法"""
    #     global res
    #     if header != None:
    #         res = requests.get(url=url, data=data, headers=header)
    #     else:
    #         res = requests.get(url=url, data=data)
    #     # return json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=4)
    #     return res