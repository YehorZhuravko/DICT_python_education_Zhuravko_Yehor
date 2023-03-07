# Початкові значення
water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550


class CoffeeMachine:
    def init(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    # Виведення параметрів для функції remaining
    def print_state(self):
        print(f"The coffee machine has:")
        print(f"{water} of water")
        print(f"{milk} of milk")
        print(f"{coffee_beans} of coffee beans")
        print(f"{cups} of disposable cups")
        print(f"{money} of money")

    # Перевірка заповнення кавомашини
    def check_resources(self, water_needed, milk_needed, coffee_needed):
        if water < water_needed:
            return "water"
        elif milk < milk_needed:
            return "milk"
        elif coffee_beans < coffee_needed:
            return "coffee_beans"
        elif cups < 1:
            return "cups"
        else:
            return "enough"

    # Купівля кави для функції buy
    def buy_coffee(self):
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - come back,: ")
        if coffee_type == "4":
            return
        elif coffee_type not in ["1", "2", "3"]:
            print("Invalid input.")
            return

        if coffee_type == "1":
            water_needed = 250
            milk_needed = 0
            coffee_needed = 16
            cost = 4
        elif coffee_type == "2":
            water_needed = 350
            milk_needed = 75
            coffee_needed = 20
            cost = 7
        else:
            water_needed = 200
            milk_needed = 100
            coffee_needed = 12
            cost = 6

        if self.check_resources(water_needed, milk_needed, coffee_needed) == "enough":
            print("I have enough resources, making you a coffee!")
            global water, milk, coffee_beans, cups, money
            water -= water_needed
            milk -= milk_needed
            coffee_beans -= coffee_needed
            cups -= 1
            money += cost
        else:
            print(f"Sorry, not enough {self.check_resources(water_needed, milk_needed, coffee_needed)}!")

    # Функція fill для заповнення параметрів кавомашини
    def refill_machine(self):
        global water, milk, coffee_beans, cups
        water += int(input("How many ml of water do you want to add: "))
        milk += int(input("How many ml of milk do you want to add: "))
        coffee_beans += int(input("How many grams of coffee beans do you want to add: "))
        cups += int(input("How many disposable cups do you want to add: "))

    # Виведення грошей для функції take
    def take_money(self):
        global money
        print(f"I gave you ${money}")
        money = 0


#Запуск кавомашини
def machine():
    coffee_machine = CoffeeMachine()
    while True:
        action = input("Write action (buy, fill, take, remaining, exit): ")
        if action == "buy":
            coffee_machine.buy_coffee()
        elif action == "fill":
            coffee_machine.refill_machine()
        elif action == "take":
            coffee_machine.take_money()
        elif action == "remaining":
            coffee_machine.print_state()
        elif action == "exit":
            break
        else:
            print("Invalid input.")


machine()
