class StockItem:
  def __init__(self, name, price, stock):
    self._name = name
    self._price = price
    self._stock = stock
  
  def get_stock(self):
    return self.stock
  
  def display_info(self):
    # print(f"Item name: {self.name}\nPrice: {self.price}\nIn stock: {self.stock}")
    return f"{self.name}: {self.price}(In stock: {self.stock})"

  def get_total_price(self, count):
    total_price = self.price * count
    return total_price
  
  def add_stock(self, restock_count):
    if restock_count < 0:
      raise ValueError("Stock can not be negative. Plrase add stock at least 1 bottle.")
    self.stock += restock_count

  # def check_in_stock(self, count):
  #   return self.stock >= count
  
  @property
  def name(self):
    # print("name getter called")
    return self._name
  
  @property
  def price(self):
    # print("price getter called")
    return self._price
  
  @property
  def stock(self):
    # print("stock getter called")
    return self._stock
  
  @stock.setter
  def stock(self, value):
    # print("stock setter called")
    self._stock = value

  
item1 = StockItem("Pepsi", 150, 5)
item2 = StockItem("Monster", 230, 5)
item3 = StockItem("Irohasu", 120, 5)
items = [item1, item2, item3]
