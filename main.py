class Player:
    # method
    # -- -> artinya private hanya bisa digunakan di class yang kita buat
    def __init__(self,name ,health=100, energy=100):
        self.name = name
        self.health = health
        self.energy = energy
    
    def attack(self,target,damage = 1):
        target.health -= damage
        self.energy -= damage
        target.damage = 10
        print(f"{self.name} attack {damage} damage to monster")
        if target.is_attacked():
            print(f"monster attack {target.damage} damage to {self.name}")
    def show_info(self):
        print(f"{self.name} health {self.health} left")
        print(f"{self.name} energy {self.energy} left")

class Monster:
    def __init__(self, health = 100):
        self.health = health
        self.health_init = self.health
    def is_attacked(self):
        return self.health < self.health_init
    def show_info(self):
        print(f"monster health {self.health} left")

player1 = Player(name="Jawir",health=200)
player2 = Player(name="Sukirman",health=150)
monster = Monster(health=500)


player1.attack(monster,damage=30)
player2.attack(monster,damage=50)
player1.show_info()
player2.show_info()
monster.show_info()