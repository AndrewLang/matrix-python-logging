from .log_level import LevelDebug, LevelInfo, LevelError, LevelWarn, LevelFatal
import datetime


class LogMessage:

    def __init__(self, name, level, message, datetime, indent=0):
        self.name = name
        self.level = level
        self.message = message
        self.datetime = datetime
        self.indent = 0

    def set_name(self, name):
        self.name = name
        return self

    def debug(name, message: str, *values) -> 'LogMessage':
        content = '{} {}'.format(message, LogMessage.format(' ', values))
        msg = LogMessage(name, LevelDebug.name, content,
                         LogMessage._formatNow())
        return msg

    def info(name, message: str, *values):
        content = '{} {}'.format(message, LogMessage.format(' ', values))
        msg = LogMessage(name, LevelInfo.name, content,
                         LogMessage._formatNow())
        return msg

    def warn(name, message: str, *values):
        content = '{} {}'.format(message, LogMessage.format(' ', values))
        msg = LogMessage(name, LevelWarn.name, content,
                         LogMessage._formatNow())
        return msg

    def error(name, message: str, *values):
        content = '{} {}'.format(message, LogMessage.format(' ', values))
        msg = LogMessage(name, LevelError.name, content,
                         LogMessage._formatNow())
        return msg

    def fatal(name, message: str, *values):
        content = '{} {}'.format(message, LogMessage.format(' ', values))
        msg = LogMessage(name, LevelFatal.name, content,
                         LogMessage._formatNow())
        return msg

    def format(template: str, *args) -> str:
        return template.join(str(v) for v in args)

    def _formatNow() -> str:
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S.%f')
