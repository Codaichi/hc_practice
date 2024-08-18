class Suica:
  def __init__(self):
    self._balance = initial_balance
  
  def charge(self, amount):
    if amount < minimum_charge:
      raise ValueError("Charges must be at least 100 JPY")
    self._balance += amount
  
  def get_balance(self):
    return self._balance
  
  def deduct(self, amount):
    if amount > self._balance:
      raise ValueError("Insufficinet balance")
    self._balance -= amount

initial_balance = 500
minimum_charge = 100



