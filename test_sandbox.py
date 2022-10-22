from unittest.mock import patch
from sandbox import my_func


@patch('sandbox.requests.get')
def test_my_func(mock_write):
    mock_write.return_value.text = "rustam"
    # Use side_effect if there are multiple similar function with different arguments
    # https://stackoverflow.com/questions/68075655/python-mock-patch-two-functions-that-are-similar
    x = my_func()
    assert x == "RUSTAM"
