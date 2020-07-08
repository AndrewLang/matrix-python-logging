from .log_level import LevelAll
from .layouts import LogComposeLayout

class LoggerConfig:
    def __init__(self):
        self.min_level = LevelAll.value
        self.layout = LogComposeLayout([])


class Configuration:
    def __init__(self):
        pass
