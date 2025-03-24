class Item:
    def __init__(self, item_id, name, description, price):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Item ID must be a positive integer.")
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(description, str):
            raise ValueError("Description must be a string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")

        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Price: {self.price:.2f}"

class ItemManager:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print("Item added successfully.")

    def view_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items:
                print(item)

    def update_item(self, item_id, new_name, new_description, new_price):
        for item in self.items:
            if item.item_id == item_id:
                try:
                    item.name = new_name
                    item.description = new_description
                    item.price = float(new_price)
                    print("Item updated successfully.")
                except ValueError:
                    print("Invalid price. Please enter a number.")
                return
        print("Item not found.")

    def delete_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                print("Item deleted successfully.")
                return
        print("Item not found.")

def main():
    manager = ItemManager()

    while True:
        print("\nItem Management Menu")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                item_id = int(input("Enter Item ID: "))
                name = input("Enter Item Name: ")
                description = input("Enter Item Description: ")
                price = float(input("Enter Item Price: "))
                item = Item(item_id, name, description, price)
                manager.add_item(item)

            elif choice == "2":
                manager.view_items()

            elif choice == "3":
                item_id = int(input("Enter Item ID to update: "))
                new_name = input("Enter New Name: ")
                new_description = input("Enter New Description: ")
                new_price = float(input("Enter New Price: "))
                manager.update_item(item_id, new_name, new_description, new_price)

            elif choice == "4":
                item_id = int(input("Enter Item ID to delete: "))
                manager.delete_item(item_id)

            elif choice == "5":
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please enter a number between 1-5.")

        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
