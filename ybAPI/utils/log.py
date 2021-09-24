import logging

# 第一步，创建日志记录器
# 1，创建一个日志记录器logger
logger = logging.getLogger()
# 2，设置日志记录器的日志级别，这里的日志级别是日志记录器能记录到的最低级别，区别于后面Handler里setLevel的日志级别
logger.setLevel(logging.INFO)
# logger.setLevel(logging.DEBUG)

# 第二步，创建日志处理器Handler。这里创建一个Handler，用于将日志写入文件
# 3，创建一个Handler，用于写入日志文件，日志文件的路径自行定义
logFile = 'logs/log.txt'
fh = logging.FileHandler(logFile, mode='a', encoding='utf-8')
# 4，设置保存至文件的日志等级
fh.setLevel(logging.INFO)

# 第三步，定义Handler的输出格式
# 5，日志输出格式定义如下
format= logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
# 6，设置 写入日志文件的Handler 的日志格式
fh.setFormatter(format)

# 第四步，将Handler添加至日志记录器logger里
logger.addHandler(fh)

# 同样的，创建一个Handler用于控制台输出日志
# ch = logging.StreamHandler()
# ch.setLevel(logging.INFO)
# ch.setFormatter(format)
# logger.addHandler(ch)

# 输出日志
# logger.info("This is info message")
# logger.warning("This is warning message")
# logger.error("This is error message")
# logger.critical("This is critical message")
