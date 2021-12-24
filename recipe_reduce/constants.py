from typing import List, Optional


class Lang:
    ALL: List[str] = ["en", "zh"]
    lang: Optional[str] = None

    @classmethod
    def set(cls, lang: str):
        assert lang in cls.ALL
        cls.lang = lang

    @classmethod
    def get(cls):
        assert cls.lang is not None
        return cls.lang


ITEM_CSV_FNAME = "data/items.csv"

# Item List

RICE = "rice"
GREEN_BEANS = "green_beans"
BELL_PEPPER = "bell_pepper"
SESAME = "sesame"
TAMARI = "tamari"
SALMON = "salmon"
SWEET_CHILI_SAUCE = "sweet_chili_sauce"
LIME = "lime"
CHIVES = "chives"
ROSEMARY = "rosemary"
GARLIC = "garlic"
LEMON = "lemon"
PARMESAN = "parmesan"
POLENTA = "polenta"
PORK = "pork"
TURKEY_BROTH_CON = "turkey_broth_con"
CAPER = "caper"
