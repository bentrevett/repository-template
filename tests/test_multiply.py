import numpy as np
import pytest
from example.multiply import double


@pytest.mark.parametrize(
    "x, expected",
    [
        ([1, 2, 3], [2, 4, 6]),
        (np.array([1, 2, 3]), np.array([2, 4, 6])),
        (-1, -2),
    ],
)
def test_add_1(x, expected):
    result = double(x)
    if isinstance(expected, (list, np.ndarray)):
        assert np.array_equal(result, expected)
    else:
        assert np.equal(result, expected)
