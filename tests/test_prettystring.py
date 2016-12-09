import unittest

class Test_Prettystring(unittest.TestCase):
    def test_import(self):
        from prettystring import prettystring as pstr

    def test_prettystring_isinstance(self):
        from prettystring import prettystring as pstr
        assert isinstance(pstr('test string'), str)

    def test_prettystring__str__returns_string(self):
        from prettystring import prettystring as pstr
        assert type(pstr('test string').__str__()) is str

    def test_prettystring__str__default_value(self):
        from prettystring import prettystring as pstr
        assert pstr('test string').__str__() == \
            '\x1b[;39;49mtest string\x1b[0m'

    def test_prettystring__str__blue_value(self):
        from prettystring import prettystring as pstr
        assert pstr('test string').paint(pstr.blue).__str__() == \
            '\x1b[;34;49mtest string\x1b[0m'

    def test_prettystring__str__red_value(self):
        from prettystring import prettystring as pstr
        assert pstr('test string').paint(pstr.red).__str__() == \
            '\x1b[;31;49mtest string\x1b[0m'

    def test_prettystring__str__green_value(self):
        from prettystring import prettystring as pstr
        assert pstr('test string').paint(pstr.green).__str__() == \
            '\x1b[;32;49mtest string\x1b[0m'

if __name__ == '__main__':
    unittest.main()
