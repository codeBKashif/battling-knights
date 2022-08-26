from .types import KnightStatus, Knights, KnightMoves
from .item_power import ItemPower
from .item import Item
from .coordinates import Coordinates


class Knight:
    def __init__(self, name: Knights, position_x, position_y):
        self.name = name
        self.coordinates = Coordinates(position_x, position_y)

        self.status = KnightStatus.LIVE
        self.power = ItemPower(1.0, 1.0)
        self.item = None

    def add_item(self, item: Item):
        if self.item == None:
            self.power.attack += item.power.attack
            self.power.defence += item.power.defence
            self.item = item

    def drowned(self):
        self.status = KnightStatus.DROWNED
        self.coordinates.position_x = -1
        self.coordinates.position_y = -1
        self.power.attack = 0
        self.power.defence = 0

    def add_surpirse_attack(self):
        self.power.attack += 0.5

    def remove_surprise_attack(self):
        self.power.attack -= 0.5

    def calculate_coordinates(self, move: KnightMoves):
        if move == KnightMoves.S:
            self.coordinates.position_x += 1

        elif move == KnightMoves.N:
            self.coordinates.position_x -= 1

        elif move == KnightMoves.W:
            self.coordinates.position_y -= 1

        elif move == KnightMoves.E:
            self.coordinates.position_y += 1

    def to_json(self):
        return [
            [self.coordinates.position_x, self.coordinates.position_y]
            if self.coordinates.position_x != -1 and self.coordinates.position_y != -1
            else None,
            str(self.status.value).upper(),
            str(self.item.name.value).upper() if self.item != None else None,
            self.power.attack,
            self.power.defence,
        ]
