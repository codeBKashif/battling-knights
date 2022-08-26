class ItemPower:
    def __init__(self, attack, defence):
        self.attack: float = attack
        self.defence: float = defence

    def to_json(self):
        return [self.attack, self.defence]
