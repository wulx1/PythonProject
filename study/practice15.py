'''
logging常见对象
Logger：日志，暴露函数给应用程序，基于日志记录器和过滤器级别决定哪些日志有效。
LogRecord ：日志记录器，将日志传到相应的处理器处理。
Handler ：处理器, 将(日志记录器产生的)日志记录发送至合适的目的地。
Filter ：过滤器, 提供了更好的粒度控制,它可以决定输出哪些日志记录。
Formatter：格式化器, 指明了最终输出中日志记录的格式。
'''
import logging
import os

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")

path = os.getcwd()
print(path)
path = os.path.realpath(__file__)
print(path)


'''
包含知识点
第一个参数是保存日志信息的文件路径，像我写的后缀多了个 {time} ，就是获取当前时间节点，这样就会自动创建新的日志；这个time应该是库里自带的变量，如果你想自己定义time也可以的哦，具体可以看看下面封装类的实现形式！
当你需要输出中文日志的时候，请加上 encoding="utf-8" ，避免出现乱码 
enqueue=True 代表异步写入，官方的大概意思是：在多进程同时往日志文件写日志的时候使用队列达到异步功效
rotation 可以理解成日志的创建时机，可以有多种写法
rotation="500 MB" ：当日志文件达到500MB时就会重新生成一个文件
rotation="12:00" ：每天12点就会创建新的文件、
rotation="1 week" ：每隔一周创建一个log
retention 配置日志的最长保留时间，官方例子： "1 week, 3 days"、"2 months" 
compression 配置文件的压缩格式，可以配置常见的格式 zip、tar、gz、tar.gz 等

'''
from  loguru import logger
logger.add("/Users/wulongxing/Desktop/test/test_{time}.log",rotation="100MB",enqueue=True,compression="zip",retention="10 days")
logger.info("info")
logger.debug("debug")
logger.warning("waining")
logger.error("error")