import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(False, 2)
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("arara", "not int")
    assert encrypt_message("arara", 2) == "ara_ra"
    assert encrypt_message("arara", 9) == "arara"
