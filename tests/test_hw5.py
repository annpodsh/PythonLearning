import hw5
import string


def test_custom_range():
    assert hw5.custom_range(string.ascii_lowercase, 'g') == 'abcdef'
    assert hw5.custom_range(string.ascii_lowercase, 'g', 'p') == 'ghijklmno'
    assert hw5.custom_range(string.ascii_lowercase, 'p', 'g', -2) == 'pnljh'
