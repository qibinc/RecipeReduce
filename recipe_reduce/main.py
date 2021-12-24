import json
from argparse import ArgumentParser
from collections import Counter
from typing import List, Tuple

from tabulate import tabulate

from recipe_reduce import item
from recipe_reduce.item import Item
from recipe_reduce.lang import Lang
from recipe_reduce.options import add_options
from recipe_reduce.recipe import Recipe
from recipe_reduce.recipe_list import NAME_TO_RECIPE


def recipe_reduce(recipe_with_count: List[Tuple[Recipe, int]]) -> List[Item]:
    # map
    counters = []
    for recipe, amount in recipe_with_count:
        assert isinstance(amount, int)
        counters += [Counter(recipe.items)] * amount
    # reduce
    item_counter = sum(counters, Counter())
    item_list = list(item_counter.keys())
    # add amount to item
    for item in item_list:
        item.amount = item_counter[item]
    return item_list


if __name__ == "__main__":
    parser = ArgumentParser()
    add_options(parser)
    args = parser.parse_args()

    Lang.set(args.lang)

    with open(args.fname) as f:
        name_to_count = json.loads(f.read())["count"]

    recipe_with_count = [
        (NAME_TO_RECIPE[name], amount) for name, amount in name_to_count.items()
    ]
    item_list = recipe_reduce(recipe_with_count)
    item_list.sort(key=lambda item: item.id)
    print(
        tabulate(
            list(map(lambda item: item.to_row(), item_list)),
            headers=Item.HEADERS,
            floatfmt=".2f",
            tablefmt="github",
        )
    )
