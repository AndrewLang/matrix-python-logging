from unittest import TestCase, main
from src.color_console_logger import ColorConsoleLogger
from src.config import LoggerConfig
from src.log_level import LevelDebug
from src.layouts import LogLayoutRepository, LogComposeLayout, LayoutNames
import datetime


class TestColorConsoleLogMessage(TestCase):

    def create_logger(self) -> ColorConsoleLogger:
        config = LoggerConfig()
        repo = LogLayoutRepository().default()       
        config.layout = LogComposeLayout([
            repo.get(LayoutNames.TimeLayout), repo.get(LayoutNames.LevelLayout),
            repo.get(LayoutNames.NameLayout), repo.get(LayoutNames.MessageLayout)
        ])
        return ColorConsoleLogger('Jasoom', config)

    def test_debug(self):
        logger = self.create_logger()
        logger.debug('now: ', datetime.datetime.now())
