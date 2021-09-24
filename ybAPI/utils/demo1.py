import requests
import json

class requestsUtils:
    """request的post方法"""
    def post_main(self,url,header,data):
        global res
        if header =="form-data":
            res = requests.post(url=url, data=data)

        if header =="Content-type:application/x-www-form-urlencoded":
            res = requests.post(url=url, data=data)

        if header=="Content-type:application/json":
            res = requests.post(url=url, json=data)
        # return json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=4)
        #json.dumps()返回结果为格式化字符串，无法取值
        return res

    def get_main(self,url,header,data):
        """request的get方法"""
        global res
        if header != None:
            res = requests.get(url=url, data=data, headers=header)
        else:
            res = requests.get(url=url, data=data)
        # return json.dumps(res.json(), ensure_ascii=False, sort_keys=True, indent=4)
        return res