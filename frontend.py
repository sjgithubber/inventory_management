# frontend
from inventory_db import InventoryDB


def main1():
    db = InventoryDB()
    while True:
        print("\n1. Add Item\n2. View Inventory\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Product name: ")
            quantity = int(input("Quantity: "))
            db.add_item(name, quantity)
            print("Item added!")
        
        elif choice == "2":
            items = db.get_all_items()
            for item in items:
                print(f"ID: {item[0]}, Name: {item[1]}, Qty: {item[2]}, Last Updated: {item[3]}")
        
        elif choice == "3":
            db.close()
            break

if __name__ == "__main__":
    main1()