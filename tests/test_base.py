class TestBase:
    """
    Base class responsible for initiating class variables
    that are inherited by the test files to use as inputs for the
    functions being tested.
    """

    photos_dir = "./photos"
    test_payload = {
        "page_data": [
            {
                "image": {
                    "uri": "photos/horizontal_1.jpg",
                },
                "position": "center",
                "page": 0,
                "mode": 0,
                "colorTheme": "#FFFFFF",
            }
        ]
    }
