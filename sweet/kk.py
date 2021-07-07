from utils.mysql_tools import Db


# def test():
#     n=467251995
#     number=n/15
#     print(number)
db=Db("39.100.88.180",3306,"voice","xpvhafO26ghDwU3a","voice_api")



# def test():
#     n=467355651
#     number=n/7
#     print(number)
#     db.query("SELECT * FROM room WHERE room_id =168")
    
# if __name__ == "__main__":
#     # for i in range(10):
#     #     test()
#     test()

def test():
    list1=[]
    res=db.query("SELECT * FROM room WHERE room_id =168")
    print(res)
    td=res[0][3]
    print(td)
    for i in res:
        list1.append(i)
    print(list1)
if __name__ == "__main__":
    test()  