# We're bringing in a tool ('random' module) that helps us with randomizing things.
import random

# Now we're creating a virtual vending machine that will hold and manage our motorcycle inventory.
class VendingMachine:
    # This is like the vending machine's brain. It gets activated when we create a new vending machine.
    def __init__(self):
        # Here, we set up a dictionary to keep track of our motorcycles and their details.
        self.items = {
            "Ninja": {
                1: {"name": "Ninja 400", "price": 5300.50, "stock": random.randint(0, 10)},  # It will display it's available stock, It will make a random number between 0-10
                2: {"name": "Ninja E-1", "price": 7600.00, "stock": random.randint(0, 9)}, # It will display it's available stock, It will make a random number between 0-9
                3: {"name": "Ninja ZX-4R", "price": 9400.25, "stock": random.randint(0, 7)}, # It will display it's available stock, It will make a random number between 0-7
                4: {"name": "Ninja ZX 6R", "price": 11400.50, "stock": random.randint(0, 5)}, # It will display it's available stock, It will make a random number between 0-5
                5: {"name": "Ninja H2 SX", "price": 28000.00, "stock": random.randint(0, 4)}, # It will display it's available stock, It will make a random number between 0-4
                6: {"name": "Ninja H2", "price": 32000.50, "stock": random.randint(0, 4)}, # It will display it's available stock, It will make a random number between 0-4
            },
            "Vulcan": {
                1: {"name": "Vulcan S", "price": 7200.00, "stock": random.randint(0, 10)}, # It will display it's available stock, It will make a random number between 0-10
                2: {"name": "Vulcan 900 Custom", "price": 8500.75, "stock": random.randint(0, 5)}, # It will display it's available stock, It will make a random number between 0-5
                3: {"name": "Vulcan 1700 Voyager", "price": 14500.50, "stock": random.randint(0, 4)}, # It will display it's available stock, It will make a random number between 0-4
            },
        }
        # We're initializing some variables to keep track of money, the shopping basket, and purchase history.
        self.balance = 0.0  # It is a floating point number where it indicate a momentary value.
        self.basket = []  # A list that will store dictionaries representing each selected motorcycle including its name and price.
        self.purchase_history = {}  # Tracking on how many times does a motorcycle has been brought




    # This function shows the different types of motorcycles available for purchase.
    def display_motor_series(self):
        print("Available motor series:")
        # We go through the list of motorcycle series and show them to the user.
        for series in self.items.keys():  # Initiates a loop that iterates over the keys (motor series) of the self.items dictionary.
            print(f"- {series}")  #  )rints each motor series with a preceding dash ("-") to indicate a list item.
        print("-" * 30) # Here, it will print a line to separate it



    # Here, we ask the user to pick a motorcycle series, like choosing a category.
    def select_motor_series(self):
        while True:
            series_choice = input("Select a motor series: ").capitalize()  # Prompts the user to input their choice of motor series. 
            # We check if the user's choice is valid. If not, we ask again.
            if series_choice in self.items:
                return series_choice
            else:
                print("Invalid series. Please select a valid series.")



    # This function displays the available motorcycles within a chosen series.
    def display_motor_items(self, category):
        print(f"{category} series:")  #  Prints the name of the chosen motor series, indicating that the following lines will display details about motorcycles in that series.
        # We show details about each motorcycle in the chosen series.
        for key, item in self.items[category].items():  # Loop that iterates over the items (motorcycles) within the chosen series. 
            print(f"  {key}. {item['name']} - ${item['price']:.2f} | Stock: {item['stock']}")
        print("-" * 30) # Here, it will print a line to separate it



    # Here, we suggest another motorcycle for the user to consider based on their last purchase.
    def suggest_purchase(self):
        if self.basket:
            last_purchase = self.basket[-1]["name"]
            # We suggest a motorcycle that wasn't the last one bought and is still in stock.
            suggested_items = [item for category_items in self.items.values() for item in category_items.values() if
                               item["name"] != last_purchase and item["stock"] > 0]
            if suggested_items:
                suggested_item = random.choice(suggested_items)
                print("-" * 10)
                print(f"We noticed you purchased {last_purchase}. How about trying {suggested_item['name']}?")
                print("-" * 30) # Here, it will print a line to separate it
                # We ask if the user wants to add the suggested motorcycle to their basket.
                add_recommendation_choice = input("Do you want to add the recommended item to your basket? (yes/no): ").lower()
                if add_recommendation_choice == "yes":
                    # If yes, we add it to the basket.
                    self.add_to_basket_by_name(suggested_item["name"])



    # This function prompts the user to choose a specific motorcycle within a series.
    def select_motor_item(self, category):
        while True:
            try:
                choice = int(input(f"Select a motor (1-{len(self.items[category])}): "))
                # We make sure the chosen motorcycle is within the valid range.
                if 1 <= choice <= len(self.items[category]):
                    return choice
                else:
                    print(f"Invalid choice. Please enter a number between 1 and {len(self.items[category])}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")



    # Here, we add the selected motorcycle to the basket.
    def add_to_basket(self, category, item_choice):
        item = self.items[category][item_choice]
        item_name = item["name"]

        # If the selected motorcycle is in stock, we add it to the basket and reduce the stock.
        if item["stock"] > 0:
            self.basket.append({"name": item_name, "price": item["price"]})
            print(f"{item_name} added to your basket.")
            item["stock"] -= 1
        else:
            print(f"Sorry, {item_name} is out of stock.")
        print("-" * 30) # Here, it will print a line to separate it



    # This function adds a motorcycle to the basket based on its name.
    def add_to_basket_by_name(self, item_name):
        for category, items in self.items.items():
            for key, item in items.items():
                if item["name"] == item_name:
                    if item["stock"] > 0:
                        self.basket.append({"name": item_name, "price": item["price"]})
                        print(f"{item_name} added to your basket.")
                        item["stock"] -= 1
                    else:
                        print(f"Sorry, {item_name} is out of stock.")
                    print("-" * 30) # Here, it will print a line to separate it
                    return
        print(f"Item {item_name} not found.")



    # This function shows the items in the basket and their total price.
    def view_basket(self):
        if self.basket:
            total_price = sum(item["price"] for item in self.basket)
            print("Items in your basket:")
            for item in self.basket:
                print(f"- {item['name']} - ${item['price']:.2f}")
            print(f"Total: ${total_price:.2f}")
        else:
            print("Your basket is empty.")
        print("-" * 30) # Here, it will print a line to separate it



    # This function handles the return of a motorcycle, updating balance and stock.
    def process_return(self):
        return_item_name = input("Enter the name of the item you want to return (If no, type none): ")
        for item in self.basket:
            if item["name"] == return_item_name:
                return_price = item["price"]
                self.balance += return_price
                print(f"Return successful! ${return_price:.2f} has been returned.")
                self.basket.remove(item)
                self.update_stock(return_item_name)
                self.view_basket()
                break
        else:
            print(f"Item {return_item_name} not found in your basket.")



    # This function updates stock when a motorcycle is returned.
    def update_stock(self, item_name):
        for category, items in self.items.items():
            for key, item in items.items():
                if item["name"] == item_name:
                    item["stock"] += 1
                    print(f"Stock of {item_name} updated.")
                    break



    # This function clears the basket (removes all items).
    def clear_basket(self):
        self.basket = []



    # This function handles the checkout process, managing payment, updating purchase history, and clearing the basket.
    def checkout(self):
        total_price = sum(item["price"] for item in self.basket)
        while self.balance < total_price:
            print("Insufficient funds. Please insert more money.")
            self.insert_money()

        self.balance -= total_price
        print("Checkout successful!")
        print(f"Total price: ${total_price:.2f}")
        if self.balance > 0:
            print(f"Your change: ${self.balance:.2f}")
        print("Dispensing keys for your items.")
        print("Thank you for shopping!")
        self.update_purchase_history()
        self.clear_basket()
        print("-" * 30) # Here, it will print a line to separate it



    # This function updates the purchase history based on items in the basket.
    def update_purchase_history(self):
        for item in self.basket:
            item_name = item["name"]
            if item_name in self.purchase_history:
                self.purchase_history[item_name] += 1
            else:
                self.purchase_history[item_name] = 1



    # This function manages the overall interaction between the user and the vending machine.
    def user_interaction(self):
        while True:
            self.display_motor_series()
            category_choice = self.select_motor_series()
            self.display_motor_items(category_choice)  # Is responsible for displaying details about the available motorcycles
            item_choice = self.select_motor_item(category_choice)
            self.add_to_basket(category_choice, item_choice)
            self.suggest_purchase()
            more_items_choice = input("Do you want to add more items to your basket? (yes/no): ").lower()
            if more_items_choice == "no":
                break

        self.view_basket()
        self.process_return()
        self.insert_money()
        checkout_choice = input("Do you want to proceed to checkout? (yes/no): ").lower()
        if checkout_choice == "yes":
            self.checkout()
        else:
            print("Thank you for shopping. Your items are still in the basket.")



    # This function handles the insertion of money by the user.
    def insert_money(self):
        while True:
            try:
                amount = float(input("Insert money ($): "))
                if amount >= 0:
                    self.balance += amount
                    break
                else:
                    print("Invalid amount. Please enter a non-negative value.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        print("-" * 30) # Here, it will print a line to separate it


# This is where we start the whole process by creating an instance of the VendingMachine class.
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.user_interaction()
