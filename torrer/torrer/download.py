import logging

import requests
import zipfile
import tarfile

from pathlib import Path

from torrer.constants import CHUNK_SIZE

logger = logging.getLogger(__name__)


def download_file(
    url: Path | str, output_path: Path | str = Path.cwd(), chunk_size: int = CHUNK_SIZE
) -> Path:
    """
    Downloads a file in chunks. If output_path is a directory, then
    the last part of the url is taken as the name.

    So if the output path is ./downloads and the url is
    https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz,
    then the final saved file will be at ./downloads/geckodriver-v0.31.0-linux64.tar.gz

    Args:
        url (str): The url to download
        output_path (Path): Where to download the file
            A full path with a name
            https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.name
        chunk_size (int): Chunk size to download the images
            Do this because downloading the files whole is very taxing on the system

    Returns:
        Path: Path to the downloaded file
    """
    if output_path.is_dir():
        logger.info(f"Directory detected: {output_path}")
        output_path = output_path / Path(url).name  # pathlib works with urls pog

    r: requests.Response = requests.get(url, timeout=10)
    r.raise_for_status()
    with open(output_path, "wb") as file:
        logging.info(f"Downloading {url} to {output_path}")
        for chunk in r.iter_content(chunk_size=chunk_size):
            if chunk:
                file.write(chunk)

    return output_path


def extract_file(archive_file: Path, end_dir: Path = Path.cwd()) -> Path:
    """
    Extracts a given zip or tar.gz file to a directory.

    Args:
        archive_file (Path): Path to the zip file
        end_dir (Path): Where to extract the file to

    Returns:
        Path: If end_dir isn't a directory

    Raises:
        NotADirectoryError: If end_dir isn't a directory
    """
    end_file: Path

    if not end_dir.is_dir():
        raise NotADirectoryError(f"{end_dir} is not a directory")

    end_dir.mkdir(parents=True, exist_ok=True)
    # end_file = end_dir / archive_file.name

    logger.info(f"Extracting {archive_file} to {end_dir}")

    if str(archive_file).endswith(".zip"):
        end_file = end_dir / "geckodriver.exe"
        with zipfile.ZipFile(
            archive_file, "r"
        ) as extraction_file:  # haven't tested this on Windows
            extraction_file.extractall(end_dir)
    elif str(archive_file).endswith(".tar.gz"):
        end_file = end_dir / "geckodriver"
        with tarfile.open(archive_file, "r:gz") as extraction_file:
            extraction_file.extractall(end_dir)

    logger.info(f"geckodriver extracted to {end_file}")
    return end_file
