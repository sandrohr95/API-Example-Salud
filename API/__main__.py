import argparse

from fimed import __version__, __author__

HEADER = "\n".join(
    [
        r" _____    _ _____ __  __ ____  _     ___    _  _   ",
        r"| ____|  | | ____|  \/  |  _ \| |   / _ \  | || |  ",
        r"|  _| _  | |  _| | |\/| | |_) | |  | | | | | || |_ ",
        r"| |__| |_| | |___| |  | |  __/| |__| |_| | |__   _|",
        r"|_____\___/|_____|_|  |_|_|   |_____\___/     |_|  ",
        "                                                    ",
        f" ver.{__version__}             author{__author__}  ",
        "                                                    ",
    ]
)


def get_parser():
    parser = argparse.ArgumentParser(prog="EJEMPLO4")

    subparser = parser.add_subparsers(dest="coomand", help="EJEMPLO4 sub-commands")
    subparser.required = True

    subparser.add_parser("deploy", help="Deploy server")
    return parser


def cli():
    print(HEADER)
    args, _ = get_parser().parse_known_args()

    if args.command == "deploy":
        from ejemplo_4.app import run_server

        run_server()

if __name__ == "__main__":
    cli()