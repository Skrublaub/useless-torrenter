import qbittorrentapi as qb
from typer import Typer, Option, Argument

from torrer.constants import DEFAULT_URL, DEFAULT_USERNAME, TORRENTING_WEBSITE
from torrer.pirates_bay_requests.interface import search, parse_search_result

cmd: Typer = Typer()


@cmd.command(help="command to actually torrent something")
def torrent(
    host: str = Option(
        DEFAULT_URL, "-l", "--localhost", help="hostname of qbittorent web API"
    ),
    username: str = Option(
        DEFAULT_USERNAME, "-u", "--username", help="username to login"
    ),
    password: str = Option(..., "-p", "--password", help="password to login with"),
) -> None:
    qb_client = qb.Client(host=host, username=username, password=password)

    try:
        qb_client.auth_log_in()
    except qb.LoginFailed as e:
        print(e)

    for indiv_torrent in qb_client.torrents_info():
        print(indiv_torrent.name)


@cmd.command(help="print html for piratesbay")
def info(
    website: str = Option(
        TORRENTING_WEBSITE, "-w", "--website", help="piratesbay link"
    ),
    query: str = Argument(..., help="query to send to pirates bay"),
) -> None:
    top_result: str = search(website, query)
    magnet_link = parse_search_result(top_result)
