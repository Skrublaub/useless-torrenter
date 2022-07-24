import requests

from bs4 import BeautifulSoup
from io import StringIO


def search(pb_url: str, query: str) -> str:
    """
    Searches pirates bay for the top result and looks for the top result

    Args:
        pb_url (str): pirates bay url
            The pirates bay url to use as there are many and the main one I use is down
        query (str): The search query for the pirates bay

    Returns:
        str: The link to the top result of the search
    """
    search_url: str = f"{pb_url}/search/{query}"

    r: requests.Response = requests.get(search_url)

    html: BeautifulSoup = BeautifulSoup(r.text, features='lxml')
    top_result_element = html.find_all('a', class_='detLink')[0]
    top_result_link: str = top_result_element['href']

    return top_result_link


def parse_search_result(torrent_page: str) -> str:
    """
    Gets the magnet link from an individual torrent page

    Args:
        torrent_page (str): The individual torrent page to download
            the magnet link from

    Returns:
        str: The magnet link
    """
    r: requests.Response = requests.get(torrent_page, timeout=10)

    html: BeautifulSoup = BeautifulSoup(r.text, features='lxml')

    #print(html.prettify())
    download_class = html.find('div', {"class": "download"})
    a_divs = download_class.find_all('a')[0]
    magnet_link = a_divs['href']

    return magnet_link
