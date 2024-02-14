import os
import logging


def pytest_configure(config):
    # Here we can add any code we want to execute
    # before the tests start

    # check that photos directory exists, if not exit
    if not os.path.exists("./photos"):
        logging.error("No photos directory available. Cannot run tests.")
        os._exit(1)
