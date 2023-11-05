class Assertions:
    @staticmethod
    def assert_equal(actual, expected):
        assert actual == expected, AssertionErrors.EQUAL.format(expected, actual)


class AssertionErrors:
    EQUAL = 'Expected text is {0}, but got {1}'
