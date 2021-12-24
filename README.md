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
  - [More Recipes!](#more-recipes)
    - [Add a New Recipe](#add-a-new-recipe)
    - [Add New Ingredients](#add-new-ingredients)

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

Open `input.json`, fill in the number of meals you would like to have for each recipe. Then, run the following command to get the shopping list of ingredients:

```bash
python -m recipe_reduce.main --fname input.json --lang en
```

## Examples

We provide examples in [English](/examples.md) and [中文](/examples_zh.md).

## More Recipes!

### Add a New Recipe

To add a new recipe, take a look at  `recipe_reduce/recipe_list.py`, create and add your own recipe to `ALL_RECIPES`.

### Add New Ingredients

You might also want to add new ingredents, take a look at `recipe_reduce/item_list.py` and add your own ingredients. Use [bitly](https://bitly.com/) to shorten the purchase urls.

PRs are welcome!
