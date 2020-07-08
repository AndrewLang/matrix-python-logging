from unittest import TestCase, main

from src.layouts import LogLayout, LogTimeLayout, LogMessage, LogNameLayout, LogLevelLayout, LogIndentLayout, LogMessageLayout, LogComposeLayout, LogThreadIdLayout, LogProcessIdLayout
from src.log_level import LevelDebug, LevelInfo, LevelError, LevelWarn, LevelFatal


class TestLogMessage(TestCase):
    def create_message(self):
        msg = LogMessage.debug('Barsoom', 'Barsoom is earth')
        return msg

    def test_create_time_layout(self):
        msg = self.create_message()
        layout = LogTimeLayout()
        part = layout.layout(msg)
        print(part)

    def test_create_name_layout(self):
        msg = self.create_message()
        layout = LogNameLayout()
        part = layout.layout(msg)
        print(part)

    def test_create_level_layout(self):
        msg = self.create_message()
        layout = LogLevelLayout()
        part = layout.layout(msg)
        print(part)

    def test_create_indent_layout(self):
        msg = self.create_message()
        msg.indent = 4
        layout = LogIndentLayout()
        part = layout.layout(msg)
        print(f'Indent: [{part}]')

    def test_create_message_layout(self):
        msg = self.create_message()
        layout = LogMessageLayout()
        part = layout.layout(msg)
        print(part)

    def test_create_thread_id_layout(self):
        msg = self.create_message()
        layout = LogThreadIdLayout()
        part = layout.layout(msg)
        print(part)

    def test_create_process_id_layout(self):
        msg = self.create_message()
        layout = LogProcessIdLayout()
        part = layout.layout(msg)
        print(part)

    def test_create_compose_layout(self):
        msg = self.create_message()
        layouts = [LogTimeLayout(), LogLevelLayout(),
                   LogNameLayout(), LogProcessIdLayout(),
                   LogThreadIdLayout(), LogMessageLayout()]
        layout = LogComposeLayout(layouts)
        part = layout.layout(msg)
        print(part)
