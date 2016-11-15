# prettystring prettystring.py
#
# The MIT License (MIT)
# Copyright (c) 2016 Robert Oliveira
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from enum import Enum
from util import overridemethod

class MARKUP(Enum):
    esc = '\033['
    eb = 'm'
    es = ''
    nul = '0'
    clr = '\033[0m' # clears anything (used to reset color back to default)

class STYLE(Enum):
    styledefault = ''
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
    def __init__(self, stl, c, bgc):
        self.stl = stl
        self.c = c
        self.bgc = bgc

    def setstyle(self, s):
        self.stl = s

    def setcolor(self, c):
        self.c = c

    def setbgcolor(self, bgc):
        self.bgc = bgc

    def _code(self):
        return '{};{};{}'.format(self.stl.value, self.c.value, self.bgc.value)

    @overridemethod
    def __str__(self):
        return self.__repr__()

    @overridemethod
    def __repr__(self):
        return '{}{}{}'.format(MARKUP.esc.value, self._code(), MARKUP.eb.value)

class prettystring(str):
    @overridemethod
    def __new__(cls,
                s='',
                stl=STYLE.styledefault,
                c=COLOR.default, bgc=BACKGROUND.bgdefault):
        '''Override __new__ and install style, color, and background color
        Enums.

        This allows a nice way of passing the formatting codes around:

            from prettystring import prettystring as pstr
            
            pretty = pstr('sweet!').paint(pstr.blue) # pstr.blue = COLOR.blue
        '''
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
        return super(prettystring, cls).__new__(cls, s)

    @overridemethod
    def __init__(self,
                 s='',
                 stl=STYLE.styledefault,
                 c=COLOR.default, bgc=BACKGROUND.bgdefault):
        '''Initialize new prettystring.

        Formatting may be set during initialization:

            from prettystring import prettystring as pstr
            
            pretty = pstr('sweet!', pstr.blink, pstr.blue)

        @param stl: STYLE
        @param c: COLOR
        @param bgc: BACKGROUND
        '''
        self.value = s
        self.brush = brush(stl, c, bgc)
        super(prettystring, self).__init__(s)

    def paint(self, m):
        '''Apply medium to the prettystring.

        Prettystring supports the list of ANSI color codes.

        See README for the full list of supported mediums and the names of
        their enums.

        @param m: STYLE or COLOR or BACKGROUND
        '''
        if isinstance(m, STYLE):
            self.brush.setstyle(m)
        if isinstance(m, COLOR):
            self.brush.setcolor(m)
        if isinstance(m, BACKGROUND):
            self.brush.setbgcolor(m)
        return self

    @overridemethod
    def __str__(self):
        return self.__repr__()

    @overridemethod
    def __repr__(self):
        return '{}{}{}'.format(self.brush, self.value, MARKUP.clr.value)

    def _composition(self):
        return '{}'.format(self.brush)

    @overridemethod
    def format(self, *args, **kwargs):
        '''Override method str.format to add support for inserting strings into
        prettystrings.

        This method currently only returns a regular string.

        TODO FIXME: Improve implementation by returning instance of
                    prettystring. The problem here is that calling super's
                    format on this child instance returns a string that doesn't
                    preserve the color codes we want (since the codes are
                    defined as instance member values, and are represented when
                    self.__repr__ is called). A more involved implementation
                    may require a C-level rewrite of the str.format method.
        '''
        t_args = []
        t_kwargs = {}
        for arg in args:
            t_args.append('{}{}'.format(arg, self._composition()))
        for k in kwargs:
            t_kwargs[k] = '{}{}'.format(kwargs[k], self._composition())
        #return super(prettystring, self).format(*t_args, **t_kwargs) # FIXME
        return self.__repr__().format(*t_args, **t_kwargs)
