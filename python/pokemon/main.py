# type: ignore
from name import NameService
from pokemon import Pokemon
from player import Player


class Pikachu(Pokemon, NameService):
  def __init__(self, name, type1, type2, hp):
    super().__init__(name, type1, type2, hp)

  def attack(self):
    super().attack()
    print(f"{self._name}の10万ボルト！")


class Charizard(Pokemon, NameService):
  def __init__(self, name, type1, type2, hp):
    super().__init__(name, type1, type2, hp)

  def attack(self):
    super().attack()
    print(f"{self._name}のほのおのうず！")


class AshKetchum(Player, NameService):
  def __init__(self, name, birhplace):
    super().__init__(name, birhplace)

  def selfintroduction(self):
    super().selfintroduction()
    print(f"{self._name}です！")


pikachu = Pikachu("ピカチュウ", "でんき", "", 10)
charizard = Charizard("リザードン", "ほのお", "ひこう", 100)
ash_ketchum = AshKetchum("サトシ","マサラタウン")

pikachu.attack()
charizard.attack()
ash_ketchum.selfintroduction()

pikachu.name = "ライチュウ"
print(pikachu.name)

ash_ketchum.name = "うんこ"
print(ash_ketchum.name)

