class Coordinates:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

    def to_json(self):
        return [self.position_x, self.position_y]
