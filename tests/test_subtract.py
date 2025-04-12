import numpy as np
import pytest
from example.subtract import subtract_1


@pytest.mark.parametrize(
    "x, expected",
    [
        ([1, 2, 3], [0, 1, 2]),
        (np.array([1, 2, 3]), np.array([0, 1, 2])),
        (0, -1),
    ],
)
def test_add_1(x, expected):
    result = subtract_1(x)
    if isinstance(expected, (list, np.ndarray)):
        assert np.array_equal(result, expected)
    else:
        assert np.equal(result, expected)
