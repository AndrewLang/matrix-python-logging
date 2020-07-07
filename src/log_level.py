
class LogLevel:
    def __init__(self, name, value):
        self.name = name
        self.value = value


LevelAll = LogLevel('ALL', 0)
LevelDebug = LogLevel('DEBUG', 100)
LevelInfo = LogLevel('INFO', 200)
LevelWarn = LogLevel('WARN', 300)
LevelError = LogLevel('ERROR', 400)
LevelFatal = LogLevel('FATAL', 500)
LevelNone = LogLevel('None', 99999)
