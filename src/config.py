from .log_level import LevelAll
from .layouts import LogComposeLayout


class Colors:
    StyleEsc = '\033['
    StyleEnd = 'm'
    ForegroundPrefix = 'Fore'
    BackgroundPrefix = 'Bg'
    ResetAllStyle = StyleEsc + "0m"

    Color256Start = '38;5;'
    Color256End = ''
    Color256BgStart = '48;5;'
    Color256BgEnd = ''

    KnownColors = {
        'ForeDefaultText':  '39',
        'ForeBlack':        '30',
        'ForeRed':          '31',
        'ForeGreen':        '32',
        'ForeYellow':       '33',
        'ForeBlue':         '34',
        'ForeMagenta':      '35',
        'ForeCyan':         '36',
        'ForeLightGray':    '37',
        'ForeDarkGray':     '90',
        'ForeLightRed':     '91',
        'ForeLightGreen':   '92',
        'ForeLightYellow':  '93',
        'ForeLightBlue':    '94',
        'ForeLightMagenta': '95',
        'ForeLightCyan':    '96',
        'ForeLightWhite':   '97',
        'BgDefault':        '49',
        'BgBlack':          '40',
        'BgRed':            '41',
        'BgGreen':          '42',
        'BgYellow':         '43',
        'BgBlue':           '44',
        'BgMagenta':        '45',
        'BgCyan':           '46',
        'BgLightGray':      '47',
        'BgDarkGray':       '100',
        'BgLightRed':       '101',
        'BgLightGreen':     '102',
        'BgLightYellow':    '103',
        'BgLightBlue':      '104',
        'BgLightMagenta':   '105',
        'BgLightCyan':      '106',
        'BgLightWhite':     '107',
        'BrightBlack':      '30;1',
        'BrightRed':        '31;1',
        'BrightGreen':      '32;1',
        'BrightYellow':     '33;1',
        'BrightBlue':       '34;1',
        'BrightMagenta':    '35;1',
        'BrightCyan':       '36;1',
        'BrightWhite':      '37;1',
    }

    KnownStyles = {
        'Bold':      '1',
        'Dim':       '2',
        'Underline': '4',
        'Blink':     '5',
        'Reverse':   '6',
        'Hidden':    '8',
    }


class Formatter:

    def format256Color(self, value) -> str:
        return f'{Colors.Color256Start}{value}'

    def formatConsoleStyle(self, styles: []) -> str:
        values = [Colors.StyleEsc]
        values.extend(';'.join(styles))
        values.append(Colors.StyleEnd)
        return ''.join(values)

    def formatConsoleOutput(self, value: str, styles: []) -> str:
        values = []
        values.extend(self.formatConsoleStyle(styles))
        values.append(value)
        values.append(Colors.ResetAllStyle)
        return ''.join(values)


class LevelStyle:
    def __init__(self, fore='', back='', styles=''):
        self.foreground = fore
        self.background = back
        self.styles = styles
        self.formatter = Formatter()

    def _parseForeground(self) -> str:
        color = ''

        if not self.foreground:
            return color

        if self.foreground.isnumeric():
            color = self.formatter.format256Color(self.foreground)
        else:
            colorName = Colors.ForegroundPrefix + self.foreground
            if colorName in Colors.KnownColors:
                color = Colors.KnownColors.get(colorName)
        return color

    def _parseBackground(self) -> str:
        color = ''

        if not self.background:
            return color

        if self.background.isnumeric():
            color = self.formatter.format256Color(self.background)
        else:
            colorName = Colors.BackgroundPrefix + self.background
            if colorName in Colors.KnownColors:
                color = Colors.KnownColors.get(colorName)
        return color

    def _parseStyle(self) -> []:
        styles = []

        if not self.styles:
            return styles

        for x in self.styles.split(','):
            x = x.strip()
            if not x:
                continue

            if x in Colors.KnownStyles:
                styles.append(Colors.KnownStyles.get(x))
            else:
                styles.append(x)

        return styles

    def parse(self) -> []:
        styles = []

        part = self._parseForeground()
        if part:
            styles.append(part)

        part = self._parseBackground()
        if part:
            styles.append(part)

        parts = self._parseStyle()
        if len(parts) > 0:
            styles.extend(parts)

        return styles

    def debug() -> 'LevelStyle':
        return LevelStyle('245', '24', '')

    def info() -> 'LevelStyle':
        return LevelStyle('56', '234', '1')

    def warn() -> 'LevelStyle':
        return LevelStyle('226', '124', '4')

    def error() -> 'LevelStyle':
        return LevelStyle('166', '234', '1,4')

    def fatal() -> 'LevelStyle':
        return LevelStyle('196', '11', '7')


class LoggerConfig:
    def __init__(self):
        self.min_level = LevelAll.value
        self.layout = LogComposeLayout([])
        self.debugStyle = LevelStyle.debug()
        self.infoStyle = LevelStyle.info()
        self.warnStyle = LevelStyle.warn()
        self.errorStyle = LevelStyle.error()
        self.fatalStyle = LevelStyle.fatal()


class Configuration:
    def __init__(self):
        pass
