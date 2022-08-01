from torrer.cli.base import cmd

from torrer.log import initiate_logger


# This is the entry point for torrer
def main() -> None:
    initiate_logger()
    cmd()


if __name__ == "__main__":
    main()