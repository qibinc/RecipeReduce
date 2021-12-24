from recipe_reduce import item_list
from recipe_reduce.recipe import Recipe

ALL_RECIPES = [
    Recipe(
        name_dict={
            "en": "Sweet & Sticky Salmon with Roasted Veggies & Rice",
            "zh": "甜粘三文鱼 配 烤蔬菜和米饭",
        },
        items={
            item_list.RICE: 2.5,
            item_list.GREEN_BEANS: 0.25,
            item_list.BELL_PEPPER: 0.5,
            item_list.GARLIC: 0.5,
            item_list.SESAME: 0.125,
            item_list.TAMARI: 0.25,
            item_list.SALMON: 5,
            item_list.SWEET_CHILI_SAUCE: 1.5,
            item_list.LIME: 0.5,
        },
    ),
    Recipe(
        name_dict={
            "en": "Lemon-Caper Pork Cutlets & Parmesan Polenta with Rosemary & Garlic Roasted Green Beans",
            "zh": "柠檬刺山柑猪排和帕尔马玉米粥 配 迷迭香和大蒜烤青豆",
        },
        items={
            item_list.CHIVES: 0.125,
            item_list.ROSEMARY: 0.125,
            item_list.GARLIC: 0.5,
            item_list.LEMON: 0.5,
            item_list.PARMESAN: 0.375,
            item_list.POLENTA: 1.5,
            item_list.PORK: 6,
            item_list.TURKEY_BROTH_CON: 0.5,
            item_list.GREEN_BEANS: 0.25,
            item_list.CAPER: 0.5,
        },
    ),
    Recipe(
        name_dict={
            "en": "Shrimp in Purgatory with Orzo Pilaf & Charred Broccoli",
            "zh": "炼狱虾 配 米粒面和烤西兰花",
        },
        items={
            item_list.ORZO: 3,
            item_list.BROCCOLI: 0.25,
            item_list.GARLIC: 1,
            item_list.PARMESAN: 0.375,
            item_list.PANKO: 0.5,
            item_list.SHRIMP: 5,
            item_list.MARINARA: 4,
            item_list.CAPER: 0.5,
            item_list.CRUSHED_PEPPER: 1,
        },
        info="Parmesan is optional.",
    )
    # Add new recipes here
]

# DO NOT MODIFY
NAME_TO_RECIPE = {
    name: recipe for recipe in ALL_RECIPES for _, name in recipe.name_dict.items()
}
