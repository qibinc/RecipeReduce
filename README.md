# RecipeReduce

[![GitHub stars](https://img.shields.io/github/stars/qibinc/RecipeReduce)](https://github.com/qibinc/RecipeReduce/stargazers)
[![GitHub license](https://img.shields.io/github/license/qibinc/RecipeReduce)](https://github.com/qibinc/RecipeReduce/blob/master/LICENSE)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

- [RecipeReduce](#recipereduce)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Usage](#usage)
  - [More Food!](#more-food)
    - [Add a New Recipe](#add-a-new-recipe)
    - [Add New Ingredients](#add-new-ingredients)

## Getting Started

### Installation

```bash
git clone https://github.com/qibinc/RecipeReduce
cd RecipeReduce
pip install -e .
```

### Usage

To start, create a menu in desired language (available options: en / zh):

```bash
python -m recipe_reduce.menu --fname input.json --lang en
```

Fill in the number of meals you would like to have for each recipe. Run reduce to get the list of ingredients:

```bash
python -m recipe_reduce.reduce --fname input.json --lang en
```

## More Food!

### Add a New Recipe

To add a new recipe, have a look at  `recipe_reduce/recipe.py`, create and add your own recipe to `ALL_RECIPES`.

### Add New Ingredients

You might also want to add new ingredents, open `data/items.csv` and fill in the item information. Then, add a constant string in `recipe_reduce/constants.py` consistent with the item id in the csv.
