import logging
import shutil
import platform

from pathlib import Path
from typing import Optional

from torrer.download import download_file, extract_file
from torrer.constants import COMMON_FIREFOX_FORK_NAMES
from torrer.exceptions import FirefoxNotFoundError

logger = logging.getLogger(__name__)


def download_geckodriver(download_path: Path) -> Path:
    """
    Downloads the geckodriver for your system to the specified directory

    Args:
        download_path (Path) = Path to download the geckodriver to

    Returns:
        Path: Path to geckodriver
    """
    operating_system: str = platform.system()

    selenium_url: str = ""

    match operating_system:
        case "Linux":
            selenium_url = "https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz"
        case "Windows":
            selenium_url = "https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-win64.zip"
        case "Darwin":
            selenium_url = "https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-macos.tar.gz"

    return download_file(selenium_url, download_path)


def check_geckodriver(download_path: Path = Path.home()) -> Path:
    """
    Checks to see if geckodriver is on path downloads it to directory
    if it is not found on path

    Returns:
        Path: Path to the geckodriver
    """
    operating_system: str = platform.system()
    executable_path: Optional[Path]

    logger.info(f"Operating system: {operating_system}")

    match operating_system:
        case "Windows":
            executable_path = shutil.which("geckodriver.exe")
        case _:  # Linux and MacOS have same geckodriver name
            executable_path = shutil.which("geckodriver")

    if executable_path is None:
        if not check_already_downloaded(download_path, operating_system):
            executable_path = download_geckodriver(download_path)
            executable_path = extract_file(executable_path, download_path)
        else:
            executable_path = download_path / "geckodriver"
    else:
        executable_path = Path(executable_path)

    return executable_path


def check_firefox() -> Path:
    """
    Checks to see if firefox is on path because geckodriver needs it to be

    Returns:
        Path: Path to the firefox executable or another common derivative

    Raises:
        FirefoxNotFoundError: No firefox or common firefox fork executables found on path
    """
    fork_path: Path

    for fork_name in COMMON_FIREFOX_FORK_NAMES:
        temp_path: Optional[str] = shutil.which(fork_name)
        if temp_path is not None:
            fork_path = Path(temp_path)
            break
    else:
        raise FirefoxNotFoundError("No firefox or common firefox fork executables found on path")

    return fork_path


def check_already_downloaded(download_path: Path, operating_system: str) -> bool:
    """
    Checks to see if the geckodriver is already downloaded to download path

    Args:
        download_path (Path): Path to geckodriver
        operating_system (str): user's operating system

    Returns:
        bool:
            True: if downloaded
            False: if not downloaded
    """
    geckodriver_path: Path

    match operating_system:
        case "Windows":
            geckodriver_path = download_path / "geckodriver.exe"
        case _:  # Linux and MacOS have same geckodriver name
            geckodriver_path = download_path / "geckodriver"

    exists: bool = geckodriver_path.exists()
    return exists
