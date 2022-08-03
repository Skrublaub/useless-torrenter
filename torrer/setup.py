from setuptools import setup

packages_list: list[str] = [
    "selenium",  # also installs requests
    "typer",
    "qbittorrent-api",
    "requests-html",
    "beautifulsoup4",
]

setup(
    name="torrer",
    description="Hooks into qbittorrent to get torrents that I want",
    author="skrublaub",
    url="https://github.com/Skrublaub/useless-torrenter",
    version="0.0.1",
    entry_points={"console_scripts": ["torrer=torrer.__main__:main"]},
)
