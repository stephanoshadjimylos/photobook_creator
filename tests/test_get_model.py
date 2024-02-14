from tests.test_base import TestBase
from photobook_creator import _get_model
from models.photobook_models import *

import pytest


class TestGetModel(TestBase):
    """Test class to test the helper function get_model."""

    @pytest.mark.parametrize(
        "mode, expected",
        [
            (0, SingleSquare),
            (1, TwoVertical),
            (2, TwoHorizontal),
            (3, FourSquares),
            (4, OneVerticalOneSquare),
            (5, SingleHorizontal),
        ],
    )
    def test_nominal(self, mode, expected):
        """
        Nominal test case to see that the function works as expected.
        Expected Output:
        """

        res = _get_model(mode, "center", 700, 700)
        assert isinstance(res, expected)

    def test_invalid_mode(self):
        """Test to see that if an invalid mode is given, the function."""
        res = _get_model(-1, "center", 700, 700)
        assert res == None
