from tests.test_base import TestBase
from photobook_creator import _open_image

from PIL.JpegImagePlugin import JpegImageFile


class TestOpenImage(TestBase):
    """Test class to test the helper function open_image."""

    def test_nominal(self):
        """
        Nominal test case to see that the function works as expected.
        Expected Output:
        """

        res = _open_image("photos/horizontal_1.jpg")
        assert isinstance(res, JpegImageFile)

    def test_incorrect_path(self):
        """Test case where incorrect path is given"""
        res = _open_image("photos/asdfasdf.jpg")
        assert res == None
