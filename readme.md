# Introduction

This is a personal tool for downloading the top torrent from a query from
the most popular public tracker.

## Disclamer 

This is for educational purposes only.

Please use a vpn while running this program because it will start torrents
given the setup is proper.

## Setup

This uses [qbittorrent](https://www.qbittorrent.org/) to torrent.

Enable `Web UI` under `Tools -> Preferences`.

Tick the `Bypass authentication for clients on localhost` box.

## Selenium Info

Geckodriver is installed based on the system detected. geckodriver.exe for windows and
just geckodriver for MacOS and Linux.

You must have firefox installed to use selenium. I tried this with librewolf by pointing
towards the executable, and it didn't work :/

## Other info

This project scrapes for a magnet link. The more popular mirrors use javascript which
makes scraping harder.

When using `torrer requests "query"`, this sends a get request to a piratesbay mirror
that doesn't need javascript to work. The official mirror needs it.

When using `torrer selenium "query"`, this uses a geckodriver install to open the
official piratesbay website. Javascript is run when using selenium

## Why

I wanted to learn selenium and how to parse with python requests.

I also wanted to learn how to use github actions. This checks to make
sure any code pushed has been run through black.

## TODO

~~Learn selenium and requests~~
~~Learn github actions basics~~
Learn how to use pyinstaller and make a release or package on github