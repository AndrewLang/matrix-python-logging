from unittest import TestCase, main
from src.logger import Logger
from src.config import LoggerConfig
from src.log_level import LevelDebug
import datetime


class TestLogMessage(TestCase):
    def create_logger(self):
        config = LoggerConfig()
        return Logger(config)

    def test_logger_init(self):
        logger = self.create_logger()
        enabled = logger.is_enable(LevelDebug)
        self.assertTrue(enabled)

    def test_logger_format(self):
        logger = self.create_logger()
        actual = logger.format(' ', 'this', 'is', 'jasoom')
        print(actual)

    def test_debug(self):
        logger = self.create_logger()
        logger.debug('now: ', datetime.datetime.now())

    def test_info(self):
        logger = self.create_logger()
        logger.info('now: ', datetime.datetime.now())

    def test_warn(self):
        logger = self.create_logger()
        logger.warn('now: ', datetime.datetime.now())

    def test_error(self):
        logger = self.create_logger()
        logger.error('now: ', datetime.datetime.now())

    def test_fatal(self):
        logger = self.create_logger()
        logger.fatal('now: ', datetime.datetime.now())
