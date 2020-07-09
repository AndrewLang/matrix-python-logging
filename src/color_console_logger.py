from .console_logger import ConsoleLogger
from .config import LoggerConfig
from .log_message import LogMessage

import sys
import colorama


class ColorConsoleLogger(ConsoleLogger):

    def __init__(self, name: str, config: LoggerConfig):
        super().__init__(name, config)
        self.colorEnabled = False

    def log(self, message: LogMessage):
        content = self.config.layout.layout(message)
        self.write(f'\033[93m{content}\033[0m')       
        return self

    def write(self, message: str):
        if not self.colorEnabled:
            self._enableColorful()

        print(message)

    def _enableColorful(self) -> None:
        if self.colorEnabled:
            return
        colorama.init()
        self.colorEnabled = True
