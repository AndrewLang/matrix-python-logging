from .log_message import LogMessage

from threading import current_thread
import os
import json

class LogLayout:
    def __init__(self):
        self.type = ''
    
    def layout(self, msg: LogMessage) -> str:
        pass

    def toJSON(self) -> str:
        pass


class LogTimeLayout(LogLayout):

    def layout(self, msg: LogMessage) -> str:
        return f'[{msg.datetime}]'

    def toJSON(self)-> str:
        data = {
            'type': LayoutNames.TimeLayout
        }
        return json.dumps(data)


class LogNameLayout(LogLayout):

    def layout(self, msg: LogMessage) -> str:
        return f'[{msg.name}]'

    def toJSON(self)-> str:
        data = {
            'type': LayoutNames.NameLayout
        }
        return json.dumps(data)

class LogLevelLayout(LogLayout):

    def layout(self, msg: LogMessage) -> str:
        return f'[{msg.level}]'

    def toJSON(self)-> str:
        data = {
            'type': LayoutNames.LevelLayout
        }
        return json.dumps(data)

class LogIndentLayout(LogLayout):

    def layout(self, msg: LogMessage) -> str:
        if msg.indent == 0:
            return ''
        else:
            return ' ' * msg.indent

    def toJSON(self)-> str:
        data = {
            'type': LayoutNames.IndentLayout
        }
        return json.dumps(data)

class LogMessageLayout(LogLayout):

    def layout(self, msg: LogMessage) -> str:
        return msg.message

    def toJSON(self)-> str:
        data = {
            'type': LayoutNames.MessageLayout
        }
        return json.dumps(data)

class LogThreadIdLayout(LogLayout):

    def layout(self, msg: LogMessage) -> str:
        return f'{current_thread().ident}'

    def toJSON(self)-> str:
        data = {
            'type': LayoutNames.ThreadIdLayout
        }
        return json.dumps(data)

class LogProcessIdLayout(LogLayout):

    def layout(self, msg: LogMessage) -> str:
        return f'{os.getpid()}'

    def toJSON(self)-> str:
        data = {
            'type': LayoutNames.ProcessIdLayout
        }
        return json.dumps(data)

class LogComposeLayout(LogLayout):

    def __init__(self, layouts: []):
        self.layouts = layouts

    def layout(self, msg: LogMessage) -> str:
        content = []
        for x in self.layouts:
            content.append(x.layout(msg))

        return ' '.join(content)

    def toJSON(self)-> str:
        data = {
            
        }
        return json.dumps(data)


class LayoutNames:
    TimeLayout = 'TimeLayout'
    NameLayout = 'NameLayout'
    LevelLayout = 'LevelLayout'
    IndentLayout = 'IndentLayout'
    MessageLayout = 'MessageLayout'
    ThreadIdLayout = 'ThreadIdLayout'
    ProcessIdLayout = 'ProcessIdLayout'


class LogLayoutRepository:

    def __init__(self):
        self.layouts = {}

    def add(self, name: str, creator) -> 'LogLayoutRepository':
        if creator is None:
            raise ValueError('Layout creator is none')

        self.layouts[name] = creator
        return self

    def get(self, name: str) -> LogLayout:
        if name in self.layouts:
            creator = self.layouts.get(name)
            return creator()

        return None

    def all(self):
        return list(self.layouts.values())

    def default(self) -> 'LogLayoutRepository':
        (
            self.add(LayoutNames.NameLayout, lambda: LogNameLayout())
                .add(LayoutNames.TimeLayout, lambda: LogTimeLayout())
                .add(LayoutNames.LevelLayout, lambda: LogLevelLayout())
                .add(LayoutNames.IndentLayout, lambda: LogIndentLayout())
                .add(LayoutNames.MessageLayout, lambda: LogMessageLayout())
                .add(LayoutNames.ThreadIdLayout, lambda: LogThreadIdLayout())
                .add(LayoutNames.ProcessIdLayout, lambda: LogProcessIdLayout())
        )
        return self
