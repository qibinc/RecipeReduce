from dataclasses import dataclass
from typing import Dict, List, Optional, Union

from recipe_reduce.lang import Lang


@dataclass
class Item:

    ID = 0
    HEADERS = ["Name", "Quantity", "Unit", "Link"]

    def __init__(
        self,
        name_dict: Dict[str, str],
        unit: str,
        url: Optional[str] = None,
        amount: Optional[float] = None,
    ) -> None:
        self.name_dict = name_dict
        self.unit = unit
        self.url = url
        self.amount = amount
        self.id = Item.ID
        Item.ID += 1

    @property
    def name(self) -> str:
        return self.name_dict.get(Lang.get(), self.name_dict[Lang.DEFAULT])

    def __hash__(self) -> int:
        return hash(self.name_dict.get(Lang.DEFAULT, list(self.name_dict.values())[0]))

    def to_row(self) -> List[Optional[Union[float, str]]]:
        return [self.name, self.amount, self.unit, self.url]
