class NameService:
  @property
  def name(self):
    # print("Getter is called")
    return self._name

  @name.setter
  def name(self, name):
    # print("Setter is called")
    if name == "うんこ":
      raise ValueError("不適切な名前です")
    self._name = name