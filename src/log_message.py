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

    def debug(name, message):
        msg = LogMessage(name, LevelDebug.name, message,
                         LogMessage._format_now())
        return msg

    def info(name, message):
        msg = LogMessage(name, LevelInfo.name, message,
                         LogMessage._format_now())
        return msg

    def warn(name, message):
        msg = LogMessage(name, LevelWarn.name, message,
                         LogMessage._format_now())
        return msg

    def error(name, message):
        msg = LogMessage(name, LevelError.name, message,
                         LogMessage._format_now())
        return msg

    def fatal(name, message):
        msg = LogMessage(name, LevelFatal.name, message,
                         LogMessage._format_now())
        return msg

    def _format_now():
        now = datetime.datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S.%f')
