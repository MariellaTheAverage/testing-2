import pytest
from io import StringIO
from unittest.mock import patch
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import exceptions
import cipher.caesar as cphr

class TestCaesarCipher:
    def test_one_word(self):
        assert cphr.encrypt("hello", 3) == 'khoor'

    def test_uppercase(self):
        with patch('sys.stdin', StringIO("1\nHelloWorld\n5\n")), patch('sys.stdout', new=StringIO()) as oo:
            cphr.run()
            assert oo.getvalue().strip()[-10:] == 'mjqqtbtwqi'

    def test_uppercase_and_punctuation(self):
        with patch('sys.stdin', StringIO("1\nHello, Amazing World!!\n6\n")), patch('sys.stdout', new=StringIO()) as oo:
            cphr.run()
            assert oo.getvalue().strip() [-22:]== 'nkrru, gsgfotm cuxrj!!'

    def test_neg_shift(self):
        with patch('sys.stdin', StringIO("1\nHelloWorld\n-1\n")):
            with pytest.raises(exceptions.InvalidShiftError) as err:
                cphr.run()
            assert 'out of range' in str(err.value)

    def test_large_shift(self):
        with patch('sys.stdin', StringIO("1\nHelloWorld\n100\n")):
            with pytest.raises(exceptions.InvalidShiftError) as err:
                cphr.run()
            assert 'out of range' in str(err.value)

    def test_get_consistent_shift(self):
        assert cphr.get_key('helloworld', 'mjqqtbtwqi') == 5

    def test_mismatched_text_length(self):
        with pytest.raises(exceptions.MismatchedTextsError) as err:
            cphr.get_key('sometext', 'textofadifferentlength')
        assert ('8' in str(err.value)) and ('22' in str(err.value))

    def test_inconsistent_shift(self):
        with pytest.raises(exceptions.InconsistentShiftError) as err:
            cphr.get_key('sometext', 'moretext')

    def test_not_int_opcode(self):
        with patch("sys.stdin", StringIO("a\n")):
            with pytest.raises(exceptions.InvalidOperationError) as err:
                cphr.run()
            assert 'not an int' in str(err.value)

    def test_nonexistent_opcode(self):
        with patch("sys.stdin", StringIO("4\n")):
            with pytest.raises(exceptions.InvalidOperationError) as err:
                cphr.run()
            assert 'unsupported code' in str(err.value)