from .config import LoggerConfig
from .log_level import LogLevel
from .log_message import LogMessage
from .log_level import LevelDebug, LevelInfo, LevelError, LevelWarn, LevelFatal

class Logger:
    def __init__(self, config: LoggerConfig):
        self.config = config
        self.name = ''

    def is_enable(self, level: LogLevel) -> bool:
        return level.value >= self.config.min_level

    def format(self, format: str, *args) -> str:
        return format.join(args)

    def log(self, message: LogMessage) -> 'Logger':
        content = self.config.layout.layout(message)
        self.write(content)
        return self
    
    def write(self, message: str):
        pass

    def debug(self, message: str, *args) -> 'Logger':
        msg = LogMessage.debug(self.name, message, args)        
        return self.log(msg)

    def info(self, message: str, *args) -> 'Logger':
        msg = LogMessage.info(self.name, message, args)        
        return self.log(msg)

    def warn(self, message: str, *args) -> 'Logger':
        msg = LogMessage.warn(self.name, message, args)        
        return self.log(msg)

    def error(self, message: str, *args) -> 'Logger':
        msg = LogMessage.error(self.name, message, args)        
        return self.log(msg)

    def fatal(self, message: str, *args) -> 'Logger':
        msg = LogMessage.fatal(self.name, message, args)        
        return self.log(msg)