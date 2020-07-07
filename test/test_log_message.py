from unittest import TestCase, main

from src.log_message import LogMessage
from src.log_level import LevelDebug, LevelInfo, LevelError, LevelWarn, LevelFatal


class TestLogMessage(TestCase):
    def setup(self):
        pass

    def tearDown(self):
        return super().tearDown()

    def test_init(self):
        message = LogMessage(
            'test', 'debug', 'this is a message', '2020-07-07 12:00:00')
        self.assertEqual('test', message.name)
        self.assertEqual('debug', message.level)
        self.assertEqual('this is a message', message.message)
        self.assertEqual('2020-07-07 12:00:00', message.datetime)
        self.assertEqual(0, message.indent)

    def test_setName(self):
        msg = LogMessage('test', 'info', 'testing', '2020-07-07 12:00:00')
        msg.set_name('jasoom')
        self.assertEqual('jasoom', msg.name)

    def test_create_debug_msg(self):
        msg = LogMessage.debug('test', 'jasoom')
        self.assertEqual('test', msg.name)
        self.assertEqual(LevelDebug.name, msg.level)

    def test_create_info_msg(self):
        msg = LogMessage.info('test', 'jasoom')
        self.assertEqual('test', msg.name)
        self.assertEqual(LevelInfo.name, msg.level)

    def test_create_warn_msg(self):
        msg = LogMessage.warn('test', 'jasoom')
        self.assertEqual('test', msg.name)
        self.assertEqual(LevelWarn.name, msg.level)

    def test_create_error_msg(self):
        msg = LogMessage.error('test', 'jasoom')
        self.assertEqual('test', msg.name)
        self.assertEqual(LevelError.name, msg.level)

    def test_create_fatal_msg(self):
        msg = LogMessage.fatal('test', 'jasoom')
        self.assertEqual('test', msg.name)
        self.assertEqual(LevelFatal.name, msg.level)

