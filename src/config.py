from .log_level import LevelAll
from .layouts import LogComposeLayout
import json


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

    def toJSON(self) -> str:
        data = {
            'foreground': self.foreground,
            'background': self.background,
            'styles': self.styles
        }
        return json.dumps(data)

    def debug() -> 'LevelStyle':
        return LevelStyle('DarkGray', '', '')

    def info() -> 'LevelStyle':
        return LevelStyle('LightGreen', '', '1')

    def warn() -> 'LevelStyle':
        return LevelStyle('LightYellow', '', '4')

    def error() -> 'LevelStyle':
        return LevelStyle('LightMagenta', '', '1,4')

    def fatal() -> 'LevelStyle':
        return LevelStyle('LightRed', '', '')


class LoggerConfig:
    def __init__(self, name=''):
        self.name = name
        self.minLevel = LevelAll.value
        self.enable = True
        self.layout = LogComposeLayout([])
        self.debugStyle = LevelStyle.debug()
        self.infoStyle = LevelStyle.info()
        self.warnStyle = LevelStyle.warn()
        self.errorStyle = LevelStyle.error()
        self.fatalStyle = LevelStyle.fatal()

    def toJSON(self):
        data = {
            'name': self.name,
            'minLevel': self.minLevel,
            'enable': self.enable,
            'layout': self.layout,
            'debugStyle': self.debugStyle,
            'infoStyle': self.infoStyle,
            'warnStyle': self.warnStyle,
            'errorStyle': self.errorStyle,
            'fataStyle': self.fatalStyle,
        }
        return json.dumps(data, default=lambda x: x.toJSON())

    def __repr__(self):
        return self.toJSON()


class Configuration:
    def __init__(self):
        self.loggerConfigs = {}

    def count(self) -> int:
        return len(self.loggerConfigs)

    def add(self, name: str, config: LoggerConfig) -> 'Configuration':
        if name is None:
            raise ValueError('Config name is empty')
        if config is None:
            raise ValueError('Config is none')

        if not config.name:
            config.name = name

        self.loggerConfigs[name] = config
        return self

    def remove(self, name: str) -> 'Configuration':
        if name is None:
            raise ValueError('Config name is empty')

        self.loggerConfigs.pop(name)
        return self

    def toJSON(self) -> str:
        configs = []
        for x in self.loggerConfigs.values():
            configs.append(x.toJSON())

        data = {
            'configs': configs
        }
        return json.dumps(data, default=lambda x: x.toJSON(), indent=4)

    def load(self, file: str):
        pass

    def save(self, file: str):
        content = self.toJSON()
        pass
