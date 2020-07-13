from .layouts import LogLayoutRepository

class LoggerContext:

    def __init__(self):
        self.layoutRepo = LogLayoutRepository().default()
        