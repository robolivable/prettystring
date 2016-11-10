from enum import Enum

class MARKUP(Enum):
    esc = '\033['
    eb = 'm'
    nul = '0' # clears anything

class STYLE(Enum):
    bold = 1
    dim = 2
    underline = 4
    blink = 5
    invert = 7
    hidden = 8
    # revert style
    _bold = 21
    _dim = 22
    _underline = 24
    _blink = 25
    _invert = 27
    _hidden = 28

class COLOR(Enum):
    default = 39
    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    magenta = 35
    cyan = 36
    light = 37
    dark = 90
    # light colors
    lred = 91
    lgreen = 92
    lyellow = 93
    lblue = 94
    lmagenta = 95
    lcyan = 96
    white = 97

class BACKGROUND(Enum):
    bgdefault = 49
    bgblack = 40
    bgred = 41
    bggreen = 42
    bgyellow = 43
    bgblue = 44
    bgmagenta = 45
    bgcyan = 46
    bglight = 47
    bgdark = 100
    bglred = 101
    bglgreen = 102
    bglyellow = 103
    bglblue = 104
    bglmagenta = 105
    bglcyan = 106
    bgwhite = 107

class brush(object):
    def __init__(self, m=MARKUP.nul):
        self.code = m.value

    def setmedium(self, m):
        self.code = m.value

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '{}{}{}'.format(MARKUP.esc.value, self.code, MARKUP.eb.value)

class prettystring(str):
    def __new__(cls, contents=''):
        for attr in dir(STYLE):
            if callable(attr) or attr.startswith('__'):
                continue
            setattr(cls, attr, getattr(STYLE, attr))
        for attr in dir(COLOR):
            if callable(attr) or attr.startswith('__'):
                continue
            setattr(cls, attr, getattr(COLOR, attr))
        for attr in dir(BACKGROUND):
            if callable(attr) or attr.startswith('__'):
                continue
            setattr(cls, attr, getattr(BACKGROUND, attr))
        return super(prettystring, cls).__new__(cls, contents)

    def __init__(self, s=''):
        self.value = s
        self.color = brush()
        self.bgcolor = brush()
        self.style = brush()
        super(prettystring, self).__init__(s)

    def paint(self, m):
        if isinstance(m, COLOR):
            self.color.setmedium(m)
        if isinstance(m, BACKGROUND):
            self.bgcolor.setmedium(m)
        if isinstance(m, STYLE):
            self.style.setmedium(m)
        return self

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '{}{}{}{}{}'.format(self.style, self.bgcolor, self.color,
            self.value, brush())

    def _composition(self):
        return '{}{}{}'.format(self.style, self.background, self.color)

    def format(self, *args, **kwargs):
        for i, arg in enumerate(args):
            args[i] = '{}{}'.format(arg, self._composition())
        for k in kwargs:
            kwargs[k] = '{}{}'.format(kwargs[k], self._composition())
        return super(prettystring, self).format(*args, **kwargs)
