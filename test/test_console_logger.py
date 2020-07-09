from unittest import TestCase, main
from src.console_logger import ConsoleLogger
from src.config import LoggerConfig
from src.log_level import LevelDebug
from src.layouts import LogLayoutRepository, LogComposeLayout, LayoutNames
import datetime


class TestConsoleLogMessage(TestCase):

    def create_logger(self) -> ConsoleLogger:
        config = LoggerConfig()
        repo = LogLayoutRepository().default()       
        config.layout = LogComposeLayout([
            repo.get(LayoutNames.TimeLayout), repo.get(LayoutNames.LevelLayout),
            repo.get(LayoutNames.NameLayout), repo.get(LayoutNames.MessageLayout)
        ])
        return ConsoleLogger('Jasoom', config)

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