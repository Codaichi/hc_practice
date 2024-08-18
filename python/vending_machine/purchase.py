class VendingMachine:  
  # sales amount
  def __init__(self):
    self._sales = 0
  
  # check in stock
  def check_in_stock(self, item, count):
    if count < 0:
      raise ValueError("Order can not be negative. Plrase enter the integer.")
    return item.stock >= count 
  
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
    item.stock -= count
    self._sales += total_price
    suica.deduct(total_price)

  # get sales
  def get_sales(self):
    return self._sales
