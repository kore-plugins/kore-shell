import pytest

from kore_shell.lib.parsers import KVParser


class TestKVParserParse(object):

    @pytest.fixture
    def parser(self):
        return KVParser()

    def test_wrong_format(self, parser):
        kv = 'testing123'

        with pytest.raises(ValueError):
            parser.parse(kv)

    def test_simple(self, parser):
        kv = 'test1=value'

        result = parser.parse(kv)

        assert result == {'test1': 'value'}

    def test_nested(self, parser):
        kv = 'test1.test2=value'

        result = parser.parse(kv)

        assert result == {'test1': {'test2': 'value'}}
