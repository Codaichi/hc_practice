from item import items, Drink

class VendingMachine:
  def __init__(self, items):
    self._sales = 0
    self._items = items
    self._stock = len(items) * [5]
  
  def get_stock(self, item):
    if item in self._items:
      index = self._items.index(item)
      return self._stock[index]
    return 0
  
  def display_info(self, item):
    return f"{item.name}: {item.price}(In stock: {self.get_stock(item)})"
  
  # check in stock
  def check_in_stock(self, item, count):
    if count < 0:
      raise ValueError("Order can not be negative. Plrase enter the integer.")
    return self.get_stock(item) >= count 
  
  # check can purchase
  def check_can_purchase(self, item, suica, count):
    return suica.get_balance() >= item.price * count

  # execute purchase
  def execute_purchase(self, item, suica, count):
    if not self.check_in_stock(item, count):
      raise ValueError("Item out of stock")
    if not self.check_can_purchase(item, suica, count):
      raise ValueError("Insufficient balance")

    total_price = item.price * count
    index = self._items.index(item)
    self._stock[index] -= count
    self._sales += total_price
    suica.deduct(total_price)    

  # get sales
  def get_sales(self):
    return self._sales
  
  def add_stock(self, item, restock_count):
    if restock_count < 0:
      raise ValueError("Stock can not be negative. Plrase add stock at least 1 bottle.")
    if item in self._items:
      index = self._items.index(item)
      self._stock[index] += restock_count
    else:
      raise ValueError("Item not found in Vending Machine.")

  @property
  def stock(self):
    return self._stock
  
  @stock.setter
  def stock(self, value):
    self._stock = value

vending_machine = VendingMachine(items)
