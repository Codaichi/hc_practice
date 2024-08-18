# type: ignore
import sys
from balance import Suica
from item import items, Drink
from purchase import VendingMachine 

new_suica = Suica()
vending_machine = VendingMachine()

print(f"Now, you have : {new_suica.get_balance()} JPY")

# charge balance
new_amount = int(input("Enter the amount to charge(at least 100) :"))

new_suica.charge(new_amount)
print(f"after the charge {new_amount}, your balance is {new_suica.get_balance()} JPY")

# buy drink
print(f"------------------------\nStock info :")

for idx, item in enumerate(items):
  print(f"{idx} : {item.display_info()}")

print("------------------------")

# get user order
order = int(input("Enter the order number(0~2):"))

try:
   selected_item = items[order]
except:
   print(f"Item must be number(0~2). Please enter the integer.")
   sys.exit(1)

count = int(input("Enter the number to order :"))
print(f"Your order is :{count} bottle of {selected_item.name}")

# calculate total price
result = selected_item.get_total_price(count)
print(f"Total price is {result} JPY")

try:
    vending_machine.execute_purchase(selected_item, new_suica, count)
    print(f"You bought {count} bottles of {selected_item.name}")
    if new_suica.get_balance() == 0:
        print("Now your money has run out")
except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)

print(f"Your balance is {new_suica.get_balance()} JPY")
print(f"------------------------\nUpdated Stock info:")
for idx, item in enumerate(items):
   print(f"{idx}: {item.display_info()}")

# Add stock
print(f"------------------------\nPlease add Stocks")
restock = int(input("Enter the number to restock item(0~2) :"))

try:
   selected_restock_item = items[restock]
except:
   print(f"Item must be number(0~2). Please enter the integer.")
   sys.exit(1)

print(f"You're adding stock to {selected_restock_item.name}")
restock_count = int(input("Enter the number to restock :"))

try:
    selected_restock_item.add_stock(restock_count)
    print(f"Succesfully added {restock_count} to {selected_restock_item.name}'s stock")
except ValueError as e:
    print(f"Error : {e}")
    sys.exit(1)

# final info
print(f"------------------------\nHere are new stock info :")

for idx, item in enumerate(items):
  print(f"{idx} : {item.display_info()}")

print(f"------------------------\nVending Machine sales: {vending_machine.get_sales()} JPY")