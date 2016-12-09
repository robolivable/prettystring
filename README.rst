============
prettystring
============
.. image:: https://travis-ci.org/robolivable/prettystring.svg?branch=master
    :target: https://travis-ci.org/robolivable/prettystring

Use prettystring to build colorful strings for more engaging output.

Prettystrings are conveniently encoded with the proper ANSI color codes based
on the colors you specify for them.

============
Installation
============
Install using ``pip``:

::

  pip install prettystring

=====
Usage
=====

As straight forward as you may think:

::

  >>> from prettystring import prettystring as pstr
  >>> colorful = pstr('sweet!')
  >>> colorful.__str__()
  '\x1b[;39;49msweet!\x1b[0m'

Prettystrings are initialized with default ANSI code values. ``sweet!`` should be
in default colors. Paint it with ``paint()``:

::

  >>> colorful.paint(pstr.blue)
  >>> colorful.__str__()
  '\x1b[;34;49msweet!\x1b[0m'
  >>> print colorful
  sweet!

The value of ``colorful`` will show up blue when ``print`` is called on it.

You can also initialize prettystrings with a style:

::

  >>> stylish = pstr('the answer is 42', pstr.blink, pstr.green, pstr.bgblue)
  >>> stylish.__str__()
  '\x1b[5;32;44mthe answer is 42\x1b[0m'
  >>> print stylish
  the answer is 42

You can even format:

::

  >>> pstr('Hello {}!').paint(pstr.red).format(pstr('world').paint(pstr.blue))
  '\x1b[;31;49mHello \x1b[;34;49mworld\x1b[0m\x1b[;31;49m!\x1b[0m'

*Note that format returns a regular string. This is a known limitation, and is
being worked on.*

==================
Prettystring Enums
==================
Use these enum values with the ``paint()`` method to apply color and formatting
to prettystrings.

Note that you can only apply one style, one color, and one background color at
a time (no mixing colors [yet]).

===================
Styles (Formatting)
===================
::

    prettystring.styledefault
    prettystring.bold
    prettystring.dim
    prettystring.underline
    prettystring.blink
    prettystring.invert
    prettystring.hidden

======
Colors
======
::

    prettystring.default
    prettystring.black
    prettystring.red
    prettystring.green
    prettystring.yellow
    prettystring.blue
    prettystring.magenta
    prettystring.cyan
    prettystring.light
    prettystring.dark

============
Light colors
============
::

    prettystring.lred
    prettystring.lgreen
    prettystring.lyellow
    prettystring.lblue
    prettystring.lmagenta
    prettystring.lcyan
    prettystring.white

=================
Background colors
=================
::

    prettystring.bgdefault
    prettystring.bgblack
    prettystring.bgred
    prettystring.bggreen
    prettystring.bgyellow
    prettystring.bgblue
    prettystring.bgmagenta
    prettystring.bgcyan
    prettystring.bglight
    prettystring.bgdark

=======================
Light background colors
=======================
::

    prettystring.bglred
    prettystring.bglgreen
    prettystring.bglyellow
    prettystring.bglblue
    prettystring.bglmagenta
    prettystring.bglcyan
    prettystring.bgwhite

=============
Compatibility
=============
Prettystring is sure to work in most Unix based environments. Official
compatibility tests/upgrades are soon to come.

============
Contribution
============
Feel free to make prettystring better by submitting a pull request. I will
review your submission as soon as possible.

=======
License
=======
This software is distributed under the MIT License. See LICENSE.md for details.
