from arena.item_power import ItemPower

from .types import ItemTypes
from .coordinates import Coordinates


class Item:
    def __init__(self, name: ItemTypes, position_x, position_y, attack, defence):
        self.name = name
        self.coordinates = Coordinates(position_x, position_y)
        self.equipped = False
        self.power = ItemPower(attack, defence)

    def to_json(self):
        return [
            [self.coordinates.position_x, self.coordinates.position_y],
            self.equipped,
        ]
