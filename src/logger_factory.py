from .config import Configuration, LoggerConfig
from .logger import Logger
from .compose_logger import ComposeLogger
from .logger_context import LoggerContext

class LoggerFactory:
    _instance = None

    def default() -> 'LoggerFactory':
        if not _instance:
            _instance = LoggerFactory()
        return _instance

    def __init__(self):
        self._config = None
        self._loggers = {}
        self.context = LoggerContext()
        
    def _config(self,  config) -> 'LoggerFactory':
        self._config = config
        return self

    def getLogger(self, name: str) -> Logger:
        if name in self._loggers:
            return self._loggers.get(name)

        logger = ComposeLogger(name, None).config(self.context)

