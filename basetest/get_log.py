import logging
import logging.handlers
import time

class GetLog:
    logger=None
    if logger is None:
        #获取log日志器
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        #获取处理器
        ch=logging.StreamHandler()
        th=logging.handlers.TimedRotatingFileHandler(filename="../log/{}.log".format(time.strftime("%Y_%m_d %H_%M_%S")),when="midnight",interval=1,backupCount=30,encoding="utf-8")
        #获取格式器
        fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%funcName)s:%(lineno)d] - %(message)s"
        fm=logging.Formatter(fmt=fmt)
        #给处理器设置格式器
        ch.setFormatter(fm)
        th.setFormatter(fm)
        #给日志器设置处理器
        logger.addHandler(ch)
        logger.addHandler(th)