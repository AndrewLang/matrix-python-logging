from .console_logger import ConsoleLogger
from .config import LoggerConfig
from .log_message import LogMessage
from .config import Formatter, LevelStyle
from .log_level import LevelError, LevelDebug, LevelInfo, LevelWarn, LevelFatal
import sys
import os


class ColorConsoleLogger(ConsoleLogger):

    def __init__(self, name: str, config: LoggerConfig):
        super().__init__(name, config)
        self.colorEnabled = False
        self.formatter = Formatter()
        self.stylePickers = {
            LevelDebug.name: config.debugStyle,
            LevelInfo.name: config.infoStyle,
            LevelWarn.name: config.warnStyle,
            LevelError.name: config.errorStyle,
            LevelFatal.name: config.fatalStyle,
        }

    def log(self, message: LogMessage):
        content = self.config.layout.layout(message)       
        style = self._getStyle(message).parse()
        output = self.formatter.formatConsoleOutput(content, style)
        self.write(output)
        # self.write(content)
        return self

    def write(self, message: str):
        if not self.colorEnabled:
            self._enableColorful()

        print(message)

    def _enableColorful(self) -> None:
        if self.colorEnabled:
            return

        os.system('')
        self.colorEnabled = True

    def _getStyle(self, message: LogMessage) -> LevelStyle:
        return self.stylePickers.get(message.level)
