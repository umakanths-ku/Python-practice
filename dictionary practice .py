warehouse_inventory = {
    "Laptop": {"price": 999.99, "stock": 5},
    "Smartphone": {"price": 499.99, "stock": 12},
    "Headphones": {"price": 89.50, "stock": 25},
    "Mouse": {"price": 25.00, "stock": 0}
} 
#OBJECTIVE 
#Calculate and print the total dollar value for each individual item (price*stock).
#Calculate and return the grand total value of the entire warehouse. 
c=0
for x,y in warehouse_inventory.items():
  dollar_value=warehouse_inventory[x].get("price")*warehouse_inventory[x].get("stock") 
  print(f"{x:10}: Total dollar value: ${dollar_value:.2f} ") 
  c+=dollar_value 

print("----------------")
print(f" The grand total of the warehouse is: ${c:.2f}")  




