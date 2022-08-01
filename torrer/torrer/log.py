import logging
import sys

from pathlib import Path

from torrer.constants import LOG_FORMAT, LOG_FILE


def initiate_logger(filename: Path | str = LOG_FILE) -> None:
    """
    Holds the basic config for a logger to be used in the program

    Args:
        filename (Path | str): where to save the log file at

    Returns:
        None
    """
    logging.basicConfig(format=LOG_FORMAT, level=logging.INFO, filename=filename)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    return
