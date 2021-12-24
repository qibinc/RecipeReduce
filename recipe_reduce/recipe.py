from dataclasses import dataclass
from typing import Dict, Optional

from recipe_reduce.item import Item
from recipe_reduce.lang import Lang


@dataclass
class Recipe:
    name_dict: Dict[str, str]
    items: Dict[Item, float]
    info: Optional[str] = None

    @property
    def name(self) -> str:
        return self.name_dict.get(Lang.get(), self.name_dict[Lang.DEFAULT])
