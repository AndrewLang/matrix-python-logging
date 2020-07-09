from src.log_level import LevelDebug, LevelInfo, LevelError, LevelWarn, LevelFatal
from unittest import TestCase, main

from src.layouts import (LogLayout, LogTimeLayout, LogMessage, LogNameLayout, LogLevelLayout, LogIndentLayout,
                         LogMessageLayout, LogComposeLayout, LogThreadIdLayout, LogProcessIdLayout,
                         LogLayoutRepository, LayoutNames)


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

    def test_layout_repo(self):
        repo = (LogLayoutRepository()
                .add(LayoutNames.TimeLayout, lambda: LogTimeLayout())
                .add(LayoutNames.NameLayout, lambda: LogNameLayout())
                .add(LayoutNames.LevelLayout, lambda: LogLevelLayout())
                .add(LayoutNames.IndentLayout, lambda: LogIndentLayout())
                .add(LayoutNames.MessageLayout, lambda: LogMessageLayout())
                .add(LayoutNames.ThreadIdLayout, lambda: LogThreadIdLayout())
                .add(LayoutNames.ProcessIdLayout, lambda: LogProcessIdLayout())
                )

        def verify(name: str):
            layout = repo.get(name)
            self.assertIsNotNone(layout)

        verify(LayoutNames.NameLayout)
        verify(LayoutNames.TimeLayout)
        verify(LayoutNames.LevelLayout)
        verify(LayoutNames.IndentLayout)
        verify(LayoutNames.MessageLayout)
        verify(LayoutNames.ThreadIdLayout)
        verify(LayoutNames.ProcessIdLayout)

    def test_layout_repo_default(self):
        def verify(name: str):
            layout = repo.get(name)
            self.assertIsNotNone(layout)
            
        repo = LogLayoutRepository().default()

        verify(LayoutNames.NameLayout)
        verify(LayoutNames.TimeLayout)
        verify(LayoutNames.LevelLayout)
        verify(LayoutNames.IndentLayout)
        verify(LayoutNames.MessageLayout)
        verify(LayoutNames.ThreadIdLayout)
        verify(LayoutNames.ProcessIdLayout)

    def test_layout_repo_all(self):
        repo = LogLayoutRepository().default()
        all = repo.all()
        self.assertEqual(7,  len(all))        
