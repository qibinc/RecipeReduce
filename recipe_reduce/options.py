from argparse import ArgumentParser

from recipe_reduce.lang import Lang


def add_options(parser: ArgumentParser):
    # fmt: off
    parser.add_argument("--lang", type=str, default="en", choices=Lang.ALL)
    parser.add_argument("--fname", type=str, default="input.json")
    # fmt: on
