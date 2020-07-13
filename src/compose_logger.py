from .logger import Logger
from .config import LoggerConfig, Configuration
from .logger_context import LoggerContext

class ComposeLogger(Logger):

    def __init__(self, name: str, config: LoggerConfig):
        super(ConsoleLogger, self).__init__(name, config)
        self._loggers = { }

    def write(self, message: str):
        for logger in self._loggers.values():
            logger.write(message)
    
    def config(self, context: LoggerContext) -> 'ComposeLogger':

        return self

