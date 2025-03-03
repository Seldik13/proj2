class Person:
    def __init__(self,name,health,armor,weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.weapon = weapon

class Knight(Person):
    def __init__(self,name,health,armor,weapon):
        super().__init__(name,health,armor,weapon)
    
    def hit(self, Knight):

        print(f"{self.name} атакует {Knight.name} с оружием {self.weapon.name}")

        if Knight.armor > self.weapon.power:
            a = 0
            Knight.armor -= self.weapon.power
        else:
            a = self.weapon.power - Knight.armor
            Knight.armor = 0
            Knight.health -= a
        print(f"{Knight.name} получает {a} урона! Осталось здоровья: {Knight.health}, брони: {Knight.armor}")
   



