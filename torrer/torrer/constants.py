from typing import Final
from pathlib import Path

DEFAULT_URL: Final[str] = "localhost:8080"
DEFAULT_USERNAME: Final[str] = "admin"

REQUESTS_TORRENTING_WEBSITE: Final[
    str
] = "https://thepiratebay0.org"  # this mirror doesn't require javascript
SELENIUM_TORRENTING_WEBSITE: Final[str] = "https://thepiratebay.org/index.html"

LOG_FORMAT: Final[str] = "%(asctime)s-%(name)s-%(levelname)s: %(message)s"
LOG_FILE: Final[str] = "torrer_log.log"

CHUNK_SIZE: Final[int] = 8192  # chunks to download the zip files with
TIMEOUT_AMT: Final[int] = 10  # 10 seconds

WINDOWS_64_SELENIUM_URL: Final[
    str
] = "https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz"
LINUX_64_SELENIUM_URL: Final[
    str
] = "https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-win64.zip"
MACOS_64_SELENIUM_URL: Final[
    str
] = "https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-macos.tar.gz"

DEFAULT_SELENIUM_DOWNLOAD_PATH: Final[Path] = Path.home()

COMMON_FIREFOX_FORK_NAMES: Final[list[str]] = [
    "firefox",
    "librewolf",
    "waterfox",
    "palemoon",
]
