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
            repo.get(LayoutNames.TimeLayout),
            repo.get(LayoutNames.LevelLayout),
            repo.get(LayoutNames.NameLayout),
            repo.get(LayoutNames.MessageLayout)
        ])
        return ColorConsoleLogger('Jasoom', config)

    def test_style_pickers(self):
        logger = self.create_logger()

        self.assertEqual(5, len(logger.stylePickers))
        self.assertIsNotNone(logger.stylePickers.get(LevelDebug.name))

    def now(self) -> str:
        value = datetime.datetime.now()
        return value.strftime('%Y-%m-%d %H:%M:%S.%f')

    def test_log_messages(self):
        logger = self.create_logger()
        print('')

        (
            logger
            .debug('now debug: ', self.now())
            .info('now info: ', self.now())
            .warn('now warn: ', self.now())
            .error('now error: ', self.now())
            .fatal('now fatal: ', self.now())
        )
