from dataclasses import dataclass
from typing import Dict

from recipe_reduce import constants


@dataclass
class Recipe:
    name_dict: Dict[str, str]
    items: Dict[str, float]

    @property
    def name(self) -> str:
        return self.name_dict[constants.Lang.get()]


ALL_RECIPES = [
    Recipe(
        name_dict={
            "en": "Sweet & Sticky Salmon with Roasted Veggies & Rice",
            "zh": "甜粘三文鱼 配 烤蔬菜和米饭",
        },
        items={
            constants.RICE: 2.5,
            constants.GREEN_BEANS: 0.25,
            constants.BELL_PEPPER: 0.5,
            constants.GARLIC: 0.5,
            constants.SESAME: 0.125,
            constants.TAMARI: 0.25,
            constants.SALMON: 5,
            constants.SWEET_CHILI_SAUCE: 1.5,
            constants.LIME: 0.5,
        },
    ),
    Recipe(
        name_dict={
            "en": "Lemon-Caper Pork Cutlets & Parmesan Polenta with Rosemary & Garlic Roasted Green Beans",
            "zh": "柠檬刺山柑猪排和帕尔马玉米粥 配 迷迭香和大蒜烤青豆",
        },
        items={
            constants.CHIVES: 0.125,
            constants.ROSEMARY: 0.125,
            constants.GARLIC: 0.5,
            constants.LEMON: 0.5,
            constants.PARMESAN: 0.375,
            constants.POLENTA: 1.5,
            constants.PORK: 6,
            constants.TURKEY_BROTH_CON: 0.5,
            constants.GREEN_BEANS: 0.25,
            constants.CAPER: 0.5,
        },
    ),
]

NAME_TO_RECIPE = {
    name: recipe for recipe in ALL_RECIPES for _, name in recipe.name_dict.items()
}
