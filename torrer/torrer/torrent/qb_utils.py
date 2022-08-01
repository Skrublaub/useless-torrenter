import logging
import qbittorrentapi as qb

logger = logging.getLogger(__name__)


def add_to_qb(magnet_link: str, qb_api_link: str) -> None:
    """
    Adds a magnet link to qbittorrent.

    Since this is a local instance, set option for no authentication
    in qbittorent from localhost.

    Args:
        magnet_link (str): The magnet link to torrent
        qb_api_link (str): Link to the qb api

    Returns:
        None
    """
    logger.info(f"Making a qbittorrent client to {qb_api_link}")
    qb_client = qb.Client(host=qb_api_link)

    logger.debug(f"Adding {magnet_link} to {qb_api_link}")
    qb_client.torrents_add(urls=magnet_link)

    return
