import logging

from typer import Typer, Option, Argument

from torrer.constants import DEFAULT_URL, REQUESTS_TORRENTING_WEBSITE, DEFAULT_SELENIUM_DOWNLOAD_PATH, SELENIUM_TORRENTING_WEBSITE
from torrer.torrent.requests_interface import search, parse_search_result
from torrer.torrent.qb_utils import add_to_qb
from torrer.torrent.selenium_torrent import magnet_link_process

cmd: Typer = Typer()

logger = logging.getLogger(__name__)


@cmd.command(help="parse piratesbay with requests and bs4")
def request(
    website: str = Option(
        REQUESTS_TORRENTING_WEBSITE, "-w", "--website", help="very legal torrenting website link"
    ),
    query: str = Argument(..., help="query to send to very legal torrenting website"),
    qb_url: str = Option(
        DEFAULT_URL, "-l", "--localhost", help="url of qbittorent web API"
    ),
) -> None:
    logger.info("Requests used to parse")
    top_result: str = search(website, query)
    magnet_link: str = parse_search_result(top_result)
    add_to_qb(magnet_link, qb_url)
    return


@cmd.command(help="""
interact with piratesbay using selenium.
If the selenium driver is not on path, it will download it.""")
def selenium(
    website: str = Option(
        SELENIUM_TORRENTING_WEBSITE, "-w", "--website", help="very legal torrenting website link"
    ),
    query: str = Argument(..., help="query to send to very legal torrenting website"),
    qb_url: str = Option(
        DEFAULT_URL, "-l", "--localhost", help="url of qbittorent web API"
    ),
    selenium_path: str = Option(
        DEFAULT_SELENIUM_DOWNLOAD_PATH, "-d", "--download-path", help="Path to download the geckodriver to"
    )
) -> None:
    logger.info("Selenium used")
    magnet_link: str = magnet_link_process(website, query, selenium_path)
    add_to_qb(magnet_link, qb_url)
    return
