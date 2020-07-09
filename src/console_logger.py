from .logger import Logger
from .config import LoggerConfig


class ConsoleLogger(Logger):

    def __init__(self, name: str, config: LoggerConfig):
        super(ConsoleLogger, self).__init__(name, config)

    def write(self, message: str):
        print(message)
