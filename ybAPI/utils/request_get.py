import requests

class Requests:
    def requests_get(self,url,headers,values):
        r = requests.post(url,headers=headers,data=values)
        result = r.json().get("state")#获取状态码
        return result

