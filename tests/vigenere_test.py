import pytest
from io import StringIO
from unittest.mock import patch
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import exceptions
import cipher.vigenere as cphr

class TestVigenereCipher:
    def test_regular_encrypt(self):
        assert cphr.encrypt('whenlifegivesyoulemonsdontmakelemonade', 'lemons') == 'hlqbyaqiswiwdcaiywxszgqgyxyoxwwiycasoi'

    def test_regular_decrypt(self):
        assert cphr.decrypt('hlqbyaqiswiwdcaiywxszgqgyxyoxwwiycasoi', 'lemons') == 'whenlifegivesyoulemonsdontmakelemonade'

    def test_huge_key(self):
        assert cphr.encrypt('lifegiveslemons', 'whenlifegivesyoulemonsdontmakelemonade') == 'hpjrrqaiytzqglg'

    def test_empty_key(self):
        with patch('sys.stdin', StringIO('makelifetakethelemonsback\n\n')):
            with pytest.raises(exceptions.EmptyKeyError) as err:
                cphr.run()

    def test_nonalphabetic_key(self):
        with patch('sys.stdin', StringIO('makelifetakethelemonsback\nportal3\n')):
            with pytest.raises(exceptions.SymbolError) as err:
                cphr.run()
            assert 'non-alphabet symbol' in str(err.value)

    def test_nonalphabetic_plaintext(self):
        with pytest.raises(exceptions.SymbolError) as err:
            cphr.encrypt("make life rue the day it thought it could give cave johnson lemons!", "lemons")
        assert 'non-alphabet symbol' in str(err.value)

    def test_nonalphabetic_ciphertext(self):
        with pytest.raises(exceptions.SymbolError) as err:
            cphr.decrypt("make life rue the day it thought it could give cave johnson lemons!", "lemons")
        assert 'non-alphabet symbol' in str(err.value)

    def test_not_int_opcode(self):
        with patch("sys.stdin", StringIO("idontwantyourdamnlemons\nportal\na\n")):
            with pytest.raises(exceptions.InvalidOperationError) as err:
                cphr.run()
            assert 'not an int' in str(err.value)

    def test_nonexistent_opcode(self):
        with patch("sys.stdin", StringIO("imgonnagetmyengineerstoinventacombustiblelemon\nportal\n4\n")):
            with pytest.raises(exceptions.InvalidOperationError) as err:
                cphr.run()
            assert 'unsupported code' in str(err.value)