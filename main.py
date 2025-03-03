from person import Knight
from weapon import Sword

sword_middle = Sword(name="Меч | Средний класс", power=20)
knight_richmond = Knight(name="Рыцарь Ричмонд", health=100, armor=100, weapon=sword_middle)

sword_mistery = Sword(name="Меч | Высший класс", power=40)
knight_genrikh = Knight(name="Рыцарь Генрих", health=120, armor=150, weapon=sword_mistery)


knight_genrikh.hit(knight_richmond)
"""
На экран должно быть выведено: 

Рыцарь Генрих атакует Рыцарь Ричмонд с оружием Меч | Высший класс
Рыцарь Ричмонд получает 0 урона! Осталось здоровья: 100, брони: 60
"""


knight_richmond.hit(knight_genrikh)
"""
На экран должно быть выведено: 

Рыцарь Ричмонд атакует Рыцарь Генрих с оружием Меч | Средний класс
Рыцарь Генрих получает 0 урона! Осталось здоровья: 120, брони: 130
"""
