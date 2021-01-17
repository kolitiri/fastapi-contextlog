import logging

import contextlogger


# Create a CLogger instance, for structured logging
clogger = contextlogger.getCLogger(__name__, level='INFO', structured=True)

# Create a formatter for structured logging
logging_format = "{'time': '%(asctime)s', 'level': '%(levelname)s', 'name': '%(name)s', %(message)s}"
formatter = logging.Formatter(logging_format)

# Create handlers for console logger
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
clogger.addHandler(console_handler)
