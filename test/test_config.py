from unittest import TestCase, main
from src.config import LoggerConfig, LevelStyle, Formatter, Colors


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
        self.assertEqual(f'{Colors.Color256Start}245', actual)

    def test_parse_background(self):
        style = LevelStyle.debug()
        actual = style._parseBackground()
        self.assertEqual(f'{Colors.Color256Start}24', actual)

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
        self.assertEqual(4, len(actual))
        self.assertEqual('38;5;245', actual[0])
        self.assertEqual('38;5;24', actual[1])
        self.assertEqual('1', actual[2])
        self.assertEqual('4', actual[3])

