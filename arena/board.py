from .types import KnightStatus, KnightMoves
from .knight import Knight
from .tile import Tile
from .item import Item


class Board:
    def __init__(self, size):
        self.board = [[Tile() for j in range(size)] for i in range(size)]

        self.size = size
        self.knights = []
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def add_knight(self, knight: Knight):
        self.knights.append(knight)
        self.move_knight(knight)

    def move_knight(self, knight: Knight, move: KnightMoves = None):

        if knight.status != KnightStatus.LIVE:
            return

        if move != None:

            prev_coord = knight.coordinates
            self.board[prev_coord.position_x][prev_coord.position_y].knight = None

            knight.calculate_coordinates(move)

            if (
                knight.coordinates.position_x >= self.size
                or knight.coordinates.position_y >= self.size
                or knight.coordinates.position_x < 0
                or knight.coordinates.position_y < 0
            ):

                self._drop_item(knight)
                knight.drowned()
            elif knight.item != None:
                knight.item.coordinates.position_x = knight.coordinates.position_x
                knight.item.coordinates.position_y = knight.coordinates.position_y

        tile = self.board[knight.coordinates.position_x][knight.coordinates.position_y]

        self._pick_available_item(knight)

        # check if there is already an other night in tile
        if tile.knight != None and tile.knight.status == KnightStatus.LIVE:
            self._fight(knight, tile)
        else:
            tile.knight = knight

    def _fight(self, knight: Knight, tile: Tile):

        defence = tile.knight.power.defence
        knight.add_surpirse_attack()
        attack = knight.power.attack

        if defence >= attack:
            knight.status = KnightStatus.DEAD
            self._drop_item(knight)

        else:
            tile.knight.status = KnightStatus.DEAD
            self._drop_item(tile.knight)
            self._pick_available_item(knight)
            tile.knight = knight

        knight.remove_surprise_attack()

    def _pick_available_item(self, knight: Knight):

        # if already have an item, then ignore it
        if knight.item != None:
            return None

        items = list(
            filter(
                lambda item: item.coordinates.position_x
                == knight.coordinates.position_x
                and item.coordinates.position_y == knight.coordinates.position_y,
                self.items,
            )
        )

        if len(items) == 0:
            return None

        items[0].equipped = True
        knight.add_item(items[0])

    def _drop_item(self, knight: Knight):
        if knight.item != None:
            knight.item.equipped = False
            knight.item = None
