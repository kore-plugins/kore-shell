from kore_shell.lib.dict import merge_dict


class TestMergeDict(object):

    def test_empty(self):
        result = merge_dict()

        assert result == {}

    def test_single(self):
        dict1 = {
            'foo': 'bar',
            'bar': 'baz',
        }

        result = merge_dict(dict1)

        assert result == dict1

    def test_multiple(self):
        dict1 = {
            'foo': 'bar',
            'bar': 'baz',
        }
        dict2 = {
            'foo2': 'bar2',
        }

        result = merge_dict(dict1, dict2)

        assert result == {
            'foo': 'bar',
            'bar': 'baz',
            'foo2': 'bar2',
        }

    def test_multiple_same_keys(self):
        dict1 = {
            'foo': 'bar',
            'bar': 'baz',
        }
        dict2 = {
            'foo': 'bar2',
        }

        result = merge_dict(dict1, dict2)

        assert result == {
            'foo': 'bar2',
            'bar': 'baz',
        }
