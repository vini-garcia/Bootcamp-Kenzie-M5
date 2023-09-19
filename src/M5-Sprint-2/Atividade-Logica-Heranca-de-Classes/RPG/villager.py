class Villager:
    def __init__(self, name: str):
        self.name = name
        self.health = 50
        self.defense = 0
        self.attack = 0
        self.is_alive = True

    def check_health(self, incoming_attack_value: int):
        damage = incoming_attack_value - self.defense
        self.health -= damage
        self.health = self.health if self.health > 0 else 0
        if not self.health:
            self.is_alive = False
            return (False, "Target is dead!")

        return self.health

    def normal_attack(self, target):
        return target.check_health(self.attack)


class Mage(Villager):
    def __init__(self, name):
        super().__init__(name)
        self.attack = 10
        self.mana = 100

    def fire_ball(self, target):
        mana_spend = 20
        if self.mana < mana_spend:
            return (False, "Not enough mana!")
        self.mana -= mana_spend
        damage = self.attack + mana_spend
        return target.check_health(damage)
