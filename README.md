## prettystring

Use prettystring to build colorful strings for more engaging output.

## Installation

TODO

## Usage

As straight forward as you may think:

    >>> from prettystring import prettystring as pstr
    >>> colorful = pstr('sweet!')
    >>> colorful.__str__()
    '\x1b[;39;49msweet!\x1b[0m'

Prettystrings are initialized with default ANSI style code values. Paint them
with `paint()`:

    >>> colorful.paint(pstr.blue)
    >>> colorful.__str__()
    '\x1b[;34;49msweet!\x1b[0m'
    >>> print colorful
    sweet!

Or initialize them with a style:

    >>> stylish = pstr('the answer is 42', pstr.blink, pstr.green, pstr.bgblue)
    >>> stylish.__str__()
    '\x1b[5;32;44mthe answer is 42\x1b[0m'
    >>> print stylish
    the answer is 42

You can also format:

    >>> pstr('Hello {}').paint(pstr.red).format(pstr('world').paint(pstr.blue))
    '\x1b[;31;49mHello \x1b[;34;49mworld\x1b[0m\x1b[;31;49m\x1b[0m'

*Note that format returns a regular string. This is a known limitation, and is
being worked on.*

## ANSI Code Enums

#### Styles (Formatting)
    pstr.styledefault
    pstr.bold
    pstr.dim
    pstr.underline
    pstr.blink
    pstr.invert
    pstr.hidden

#### Colors
    pstr.default
    pstr.black
    pstr.red
    pstr.green
    pstr.yellow
    pstr.blue
    pstr.magenta
    pstr.cyan
    pstr.light
    pstr.dark

#### Light colors
    pstr.lred
    pstr.lgreen
    pstr.lyellow
    pstr.lblue
    pstr.lmagenta
    pstr.lcyan
    pstr.white

#### Background colors
    pstr.bgdefault
    pstr.bgblack
    pstr.bgred
    pstr.bggreen
    pstr.bgyellow
    pstr.bgblue
    pstr.bgmagenta
    pstr.bgcyan
    pstr.bglight
    pstr.bgdark

#### Light background colors
    pstr.bglred
    pstr.bglgreen
    pstr.bglyellow
    pstr.bglblue
    pstr.bglmagenta
    pstr.bglcyan
    pstr.bgwhite

## Contribution

Feel free to make prettystring better by submitting a pull request. I will
review your submission as soon as I can.

## License

This software is distributed under The MIT License. See LICENSE.md for details.
