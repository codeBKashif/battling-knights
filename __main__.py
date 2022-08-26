from asyncio.log import logger
import logging
from os import error
from arena import Board, Knight, Item, ItemTypes, Knights
import input_moves
import output_json


def main():
    board = Board(8)

    axe = Item(ItemTypes.AXE, 2, 2, 2.0, 0.0)
    dagger = Item(ItemTypes.DAGGER, 2, 5, 1.0, 0.0)
    magic_staff = Item(ItemTypes.MAGIC_STAFF, 5, 2, 1.0, 1.0)
    helmet = Item(ItemTypes.HELMET, 5, 5, 0.0, 1.0)

    board.add_item(axe)
    board.add_item(magic_staff)
    board.add_item(dagger)
    board.add_item(helmet)

    red = Knight(Knights.RED, 0, 0)
    blue = Knight(Knights.BLUE, 7, 0)
    green = Knight(Knights.GREEN, 7, 7)
    yellow = Knight(Knights.YELLOW, 0, 7)

    board.add_knight(red)
    board.add_knight(green)
    board.add_knight(blue)
    board.add_knight(yellow)

    knight_keys = {"R": red, "B": blue, "G": green, "Y": yellow}

    try:
        knight_moves = input_moves.validate_and_get_moves()
        for knight_move in knight_moves:
            _knight, move = knight_move
            knight = knight_keys[_knight] if _knight in knight_keys.keys() else None
            if knight != None:
                board.move_knight(knight, move)
    except BaseException as e:
        logging.error(str(e))

    output = {
        "red": red.to_json(),
        "blue": blue.to_json(),
        "green": green.to_json(),
        "yellow": yellow.to_json(),
        "axe": axe.to_json(),
        "magic_staff": magic_staff.to_json(),
        "dagger": dagger.to_json(),
        "helmet": helmet.to_json(),
    }

    output_json.write_output(output)


if __name__ == "__main__":
    main()
