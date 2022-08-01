import logging
import time

from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service

from torrer.torrent.geckodriver_utils import check_geckodriver, check_firefox

logger = logging.getLogger(__name__)


def start_webdriver(geckodriver_path: Path) -> webdriver.Firefox:
    """
    Starts a firefox webdriver

    Returns:
        webdriver.Firefox: The firefox webdriver being used
    """
    firefox_service: Service = Service(executable_path=str(geckodriver_path))
    driver: webdriver.Firefox = webdriver.Firefox(service=firefox_service)

    return driver


def close_webdriver(driver: webdriver.Firefox) -> None:
    """
    Closes a firefox webdriver

    Args:
        driver (webdriver.Firefox): Firefox webdriver to be shutdown

    Returns:
        None
    """
    driver.quit()
    return


def magnet_link_process(funny_website: str, query: str, selenium_path: Path | str) -> str:
    """
    The process for getting the magnet link. Still learning how to not spaghetti code.
    If any xpaths are changed, this will totally fail.

    Args:
        funny_website (str): The pirates bay website to use
        query (str): What query to send the pirates bay
        selenium_path (Path): Path to the selenium driver

    Returns:
        str: The magnet link to the torrent
    """
    selenium_path = Path(selenium_path)

    selenium_path = check_geckodriver(selenium_path)
    # firefox_path = check_firefox()

    driver: webdriver.Firefox = start_webdriver(selenium_path)

    driver.get(funny_website)
    search_box = driver.find_element(By.XPATH, r"/html/body/main/section/form/div[1]/input")
    # search_box.click()
    logger.info(f"Sending {query} to search_box")
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)

    driver.implicitly_wait(5)  # wait for javascript to load on the page
    top_result = driver.find_element(By.XPATH, r"(//li[@id='st']/span[2]/a)[2]")
    top_result.click()

    driver.implicitly_wait(5)
    magnet_link_button = driver.find_element(By.XPATH, r"//a[contains(text(),'Get This Torrent')]")
    magnet_link: str = magnet_link_button.get_property("href")

    logger.debug(f"Magnet link: {magnet_link}")

    close_webdriver(driver)

    return magnet_link
