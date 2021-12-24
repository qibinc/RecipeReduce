import json
from argparse import ArgumentParser

from recipe_reduce.lang import Lang
from recipe_reduce.options import add_options
from recipe_reduce.recipe_list import ALL_RECIPES

if __name__ == "__main__":
    parser = ArgumentParser()
    add_options(parser)
    args = parser.parse_args()

    Lang.set(args.lang)

    with open(args.fname, "w") as f:
        f.write(
            json.dumps(
                {
                    "count": {recipe.name: 0 for recipe in ALL_RECIPES},
                    "info": {
                        recipe.name: recipe.info
                        for recipe in ALL_RECIPES
                        if recipe.info
                    },
                },
                indent=2,
                ensure_ascii=False,
            )
        )
