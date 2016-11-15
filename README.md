### prettystring

Use prettystring to build colorful strings for more engaging output.

## Installation

TODO

## Usage

As straight forward as you may think:

    >>> from prettystring import prettystring as pstr
    >>> colorful = pstr('sweet!')
    >>> colorful.__str__()
    '\x1b[;39;49msweet!\x1b[0m'

Prettystrings are initialized with default style values. Paint them with
`paint()`:

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

## Contribution

Feel free to make prettystring better by submitting a pull request. I will
review your submission as soon as I can.

## License

This software is distributed under The MIT License. See LICENSE.md for details.
