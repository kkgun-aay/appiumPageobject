# coding=utf-8
import logging
import time
import os

log_path = './log'


class Log:
    def __init__(self):
        self.now = time.strftime("%Y-%m-%d--%H-%M-%S")

    @staticmethod
    def print_console(level, message):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(ch)
        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)

        # 记录完日志移除句柄Handler
        logger.removeHandler(ch)

    def debug(self, message):
        self.print_console('debug', message)

    def info(self, message):
        self.print_console('info', message)

    def warning(self, message):
        self.print_console('warning', message)

    def error(self, message):
        self.print_console('error', message)


if __name__ == '__main__':

    Log.print_console("info", "hhh")
