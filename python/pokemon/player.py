from abc import ABCMeta, abstractmethod


class Player:
  @abstractmethod
  def __init__(self, name, birhplace):
    self._name = name
    self._birthplace = birhplace

  def selfintroduction(self):
    print(f"{self._birthplace}から来ました！")