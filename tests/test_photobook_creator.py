from tests.test_base import TestBase
from photobook_creator import photobook_creator

import os
from unittest.mock import patch


class TestPhotobookCreator(TestBase):
    """Test class to test the main function photobook_creator."""

    def test_nominal(self):
        """
        Nominal test case to see that the function works as expected.
        Expected Output:
        """

        res = photobook_creator(self.test_payload)
        assert res == True
        assert "final_photobook.pdf" in os.listdir("./photos")

    def test_missing_payload(self):
        """Test case where payload is missing"""
        res = photobook_creator({})
        assert res == False

    @patch("photobook_creator._open_image")
    def test_failed_image(self, mock_function):
        """Test to see that the function under test handles if the image does not load."""
        mock_function.return_value = None
        res = photobook_creator(self.test_payload)
        assert res == False

    @patch("photobook_creator._get_model")
    def test_failed_model(self, mock_function):
        """Test to see that the function under test handles if the model does not load."""
        mock_function.return_value = None
        res = photobook_creator(self.test_payload)
        assert res == False
