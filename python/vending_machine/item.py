class Drink:
  def __init__(self, name, price):
    self._name = name
    self._price = price

  def get_total_price(self, count):
    total_price = self.price * count
    return total_price
  
  @property
  def name(self):
    return self._name
  
  @property
  def price(self):
    return self._price
  
item1 = Drink("Pepsi", 150)
item2 = Drink("Monster", 230)
item3 = Drink("Irohasu", 120)
items = [item1, item2, item3]
