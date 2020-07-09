from .logger import Logger

class ColorConsoleLogger(Logger):

    def __init__(self, name: str, config: LoggerConfig):
        super().__init__(name, config)

    def write(self, message: str):
        print(message)