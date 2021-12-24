import json
from argparse import ArgumentParser
from collections import Counter
from typing import List, Tuple

from recipe_reduce import constants
from recipe_reduce.item import Item
from recipe_reduce.options import add_options
from recipe_reduce.recipe import NAME_TO_RECIPE, Recipe


def recipe_reduce(
    recipe_with_amount: List[Tuple[Recipe, int]]
) -> List[Tuple[str, float]]:
    # map
    counters = []
    for recipe, amount in recipe_with_amount:
        assert isinstance(amount, int)
        counters += [Counter(recipe.items)] * amount
    # reduce
    item_id_counter = sum(counters, Counter()).items()
    # TODO: get complete item information from csv
    return list(item_id_counter)


if __name__ == "__main__":
    parser = ArgumentParser()
    add_options(parser)
    args = parser.parse_args()

    constants.Lang.set(args.lang)

    with open(args.fname) as f:
        name_to_amount = json.loads(f.read())
        recipe_with_amount = [
            (NAME_TO_RECIPE[name], amount) for name, amount in name_to_amount.items()
        ]
        print(recipe_reduce(recipe_with_amount))
