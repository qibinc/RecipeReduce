import json
from argparse import ArgumentParser

from recipe_reduce.constants import Lang
from recipe_reduce.options import add_options
from recipe_reduce.recipe import ALL_RECIPES

if __name__ == "__main__":
    parser = ArgumentParser()
    add_options(parser)
    args = parser.parse_args()

    Lang.set(args.lang)

    with open(args.fname, "w") as f:
        f.write(
            json.dumps(
                {recipe.name: 0 for recipe in ALL_RECIPES}, indent=2, ensure_ascii=False
            )
        )
