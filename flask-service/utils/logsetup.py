import logging
from logging.handlers import RotatingFileHandler
import os
import sys


FORMAT = ("%(asctime)s.%(msecs)03d;%(thread)x;%(filename)s;"
          "%(funcName)s;%(levelname)s;%(message)s")
DATEFMT = '%Y%m%d%I%M%S'

logger = logging.getLogger(__name__)
LOG_DIR = os.path.join(os.path.dirname(__file__), os.pardir, "logs")


def get_handler(basename):
    logfile = "{}.log".format(basename)
    logfile_full_path = os.path.join(LOG_DIR, logfile)
    log_handler = RotatingFileHandler(
        logfile_full_path, maxBytes=1024 * 1024 * 100, backupCount=3)

    log_handler.setFormatter(logging.Formatter(FORMAT, datefmt=DATEFMT))
    return log_handler


def handle_uncaught_exception(exc_type, exc_value, exc_traceback):
    """log uncaught exceptions before exiting the program
    """
    if not issubclass(exc_type, KeyboardInterrupt):
        logger.fatal("0;Exit with uncaught exception",
                     exc_info=(exc_type, exc_value, exc_traceback))
    sys.__excepthook__(exc_type, exc_value, exc_traceback)


def init_root_logger():
    # shorten the more common level names i.e. DEBUG -> D
    logging.addLevelName(logging.DEBUG, 'D')
    logging.addLevelName(logging.INFO, 'I')
    logging.addLevelName(logging.ERROR, 'E')
    logging.addLevelName(logging.FATAL, 'F')

    sys.excepthook = handle_uncaught_exception


def init_log_handler(basename, replace_existing=False):
    main_logger = logging.getLogger()
    if replace_existing:
        main_logger.handlers = []
    if not main_logger.handlers:
        # the root logger has no handler, so create one
        handler = get_handler(basename)
        main_logger.addHandler(handler)
        main_logger.setLevel(logging.DEBUG)
        main_logger.info(";started %s logger", basename)
