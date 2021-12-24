# RecipeReduce

[![GitHub stars](https://img.shields.io/github/stars/qibinc/RecipeReduce)](https://github.com/qibinc/RecipeReduce/stargazers)
[![GitHub license](https://img.shields.io/github/license/qibinc/RecipeReduce)](https://github.com/qibinc/RecipeReduce/blob/master/LICENSE)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

This repo will help you figure out the amount of ingredients to buy for a certain number of meals with selected recipes.

- [RecipeReduce](#recipereduce)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Usage](#usage)
  - [Examples](#examples)
    - [Input](#input)
    - [Output](#output)
  - [More Recipes!](#more-recipes)
    - [Add a New Recipe](#add-a-new-recipe)
    - [Add New Ingredients](#add-new-ingredients)
  - [TODOs](#todos)

## Getting Started

### Installation

```bash
pip install -e .
```

### Usage

To start, create a menu in desired language (available options: en / zh):

```bash
python -m recipe_reduce.menu --fname input.json --lang en
```

Open `input.json`, fill in the number of meals you would like to have for each recipe. Then, run the following command to get the list of ingredients:

```bash
python -m recipe_reduce.main --fname input.json --lang en
```

## Examples

### Input

```json
{
  "甜粘三文鱼 配 烤蔬菜和米饭": 1,
  "柠檬刺山柑猪排和帕尔马玉米粥 配 迷迭香和大蒜烤青豆": 1
}
```

### Output

```python
[("rice", 2.5), ("green_beans", 0.5), ("bell_pepper", 0.5), ("garlic", 1.0), ("sesame", 0.125), ("tamari", 0.25), ("salmon", 5), ("sweet_chili_sauce", 1.5), ("lime", 0.5), ("chives", 0.125), ("rosemary", 0.125), ("lemon", 0.5), ("parmesan", 0.375), ("polenta", 1.5), ("pork", 6), ("turkey_broth_con", 0.5), ("caper", 0.5)]
```

## More Recipes!

### Add a New Recipe

To add a new recipe, have a look at  `recipe_reduce/recipe.py`, create and add your own recipe to `ALL_RECIPES`.

### Add New Ingredients

You might also want to add new ingredents, open `data/items.csv` and fill in the item information. Then, add a constant string in `recipe_reduce/constants.py` consistent with the item id in the csv.

## TODOs

- [ ] Print detailed item information from csv
- [ ] Automatically add to WholeFoods cart with item url and amount
