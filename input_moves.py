from arena import KnightMoves
from os import path

input_file = path.join(path.dirname(__file__), "data/moves.txt")
error_message = "Invalid Input"


def validate_and_get_moves():
    moves = []

    with open(input_file, "r") as file:

        first_line = file.readline().strip()

        if first_line != "GAME-START":
            raise Exception(error_message)

        while True:
            line = file.readline().strip()
            if not line:
                break
            elif line == "GAME-END":
                break

            items = line.split(":")
            if len(items) > 2:
                raise Exception(error_message)
            if items[1] not in [move.value for move in KnightMoves]:
                raise Exception(error_message)
            moves.append(items)

    return moves
