from unittest import TestCase, main
from src.config import LoggerConfig, LevelStyle, Formatter, Colors, Configuration


class TestColorConsoleLogMessage(TestCase):
    def test_format256color(self):
        formatter = Formatter()
        actual = formatter.format256Color(155)
        self.assertEqual(f'{Colors.Color256Start}155', actual)

    def test_format_console_style(self):
        formatter = Formatter()
        actual = formatter.formatConsoleStyle(['1', '4', '31'])
        self.assertEqual('\033[1;4;31m', actual)

    def test_format_console_output(self):
        formatter = Formatter()
        actual = formatter.formatConsoleOutput('jasoom', ['1', '4', '31'])
        self.assertEqual('\033[1;4;31mjasoom\033[0m', actual)

    def test_parse_foreground(self):
        style = LevelStyle.debug()
        actual = style._parseForeground()
        self.assertEqual(f'90', actual)

    def test_parse_background(self):
        style = LevelStyle.fatal()
        actual = style._parseBackground()
        self.assertEqual(f'', actual)

    def test_parse_style(self):
        style = LevelStyle.debug()
        style.styles = '1 , 4 '
        print(style)
        actual = style._parseStyle()
        print(actual)
        self.assertEqual(2, len(actual))
        self.assertEqual('1', actual[0])
        self.assertEqual('4', actual[1])

    def test_parse_styles(self):
        style = LevelStyle.debug()
        style.styles = '1 , 4 '
        actual = style.parse()
        print(actual)
        self.assertEqual(3, len(actual))
        self.assertEqual('90', actual[0])
        self.assertEqual('1', actual[1])
        self.assertEqual('4', actual[2])

    def test_style_json(self):
        style = LevelStyle.debug()
        actual = style.toJSON()
        print(actual)

    def createConfiguration(self):
        config = Configuration()
        consoleConfig = LoggerConfig()
        config.add('console', consoleConfig)
        return config

    def test_configuration_add(self):
        config = self.createConfiguration()
        length = config.count()

        logConfig = LoggerConfig()
        config.add('jasoom', logConfig)
        self.assertEqual(length + 1, config.count())

        config.remove('jasoom')
        self.assertEqual(length, config.count())

    def test_configuration_json(self):
        config = self.createConfiguration()
        content = config.toJSON()
        print(content)
