from abc import ABCMeta, abstractmethod

class Pokemon:
  @abstractmethod
  def __init__(self, name, type1, type2, hp):
    self._name = name
    self._type1 = type1
    self._type2 = type2
    self._hp = hp

  def attack(self):
    print(f"{self._name}のこうげき！")