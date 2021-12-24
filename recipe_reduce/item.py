import csv
from dataclasses import dataclass
from typing import Dict

from recipe_reduce import constants


@dataclass
class Item:
    unit: str
    url: str
    name_dict: Dict[str, str]

    @property
    def name(self) -> str:
        return self.name_dict[constants.Lang.get()]
