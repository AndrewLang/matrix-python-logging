from .log_message import LogMessage

from threading import current_thread
import os


class LogLayout:
    def layout(self, msg: LogMessage) -> str:
        pass


class LogTimeLayout(LogLayout):

    def layout(self, msg: LogMessage) -> str:
        return f'[{msg.datetime}]'


class LogNameLayout(LogLayout):

    def layout(self, msg: LogMessage) -> str:
        return f'[{msg.name}]'


class LogLevelLayout(LogLayout):

    def layout(self, msg: LogMessage) -> str:
        return f'[{msg.level}]'


class LogIndentLayout(LogLayout):

    def layout(self, msg: LogMessage) -> str:
        if msg.indent == 0:
            return ''
        else:
            return ' ' * msg.indent


class LogMessageLayout(LogLayout):

    def layout(self, msg: LogMessage) -> str:
        return msg.message


class LogThreadIdLayout(LogLayout):

    def layout(self, msg: LogMessage) -> str:
        return f'{current_thread().ident}'

class LogProcessIdLayout(LogLayout):

    def layout(self, msg: LogMessage) -> str:
        return f'{os.getpid()}'

class LogComposeLayout(LogLayout):

    def __init__(self, layouts: []):
        self.layouts = layouts

    def layout(self, msg: LogMessage) -> str:
        content = []
        for x in self.layouts:
            content.append(x.layout(msg))

        return ' '.join(content)
