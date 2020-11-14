class Coffee:
    def __init__(self, water, milk, beans, money, cups):
        self.water = int(water)
        self.milk = int(milk)
        self.beans = int(beans)
        self.money = int(money)
        self.cups = int(cups)
machine = Coffee(400, 540, 120, 550, 9)
espresso = Coffee(250, 0, 16, 4, 1)
latte = Coffee(350, 75, 20, 7, 1)
cappuccino = Coffee(200, 100, 12, 6, 1)

def display():
    print(f"""The coffee machine has:
{machine.water} of water
{machine.milk} of milk
{machine.beans} of beans
{machine.cups} of disposable cups
{machine.money} of money""")

def buy_coffee(item):
    if item == "1":
        machine.water -= espresso.water
        machine.beans -= espresso.beans
        machine.money += espresso.money
        machine.cups -= espresso.cups
        print("\n")
        display()
    elif item == "2":
        machine.water -= latte.water
        machine.milk -= latte.milk
        machine.beans -= latte.beans
        machine.money += latte.money
        machine.cups -= latte.cups
        print("\n")
        display()
    elif item == "3":
        machine.water -= cappuccino.water
        machine.milk -= cappuccino.milk
        machine.beans -= cappuccino.beans
        machine.money += cappuccino.money
        machine.cups -= cappuccino.cups
        print("\n")
        display()
def fill_machine():
    add_water = int(input("Write how many ml of water do you want to add:\n"))
    add_milk = int(input("Write how may ml of milk do you want to add:\n"))
    add_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
    add_cups = int(input("Write how many disposable ccups of coffee do you want to add\n"))
    machine.water += add_water
    machine.milk += add_milk
    machine.beans += add_beans
    machine.cups += add_cups
    print("\n")
    display()
def take_money():
    print(f"I gave you ${machine.money}\n")
    machine.money -= machine.money


display()
action = input("\nWrite action (buy, fill, take):\n")
if action == "buy":
    item = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
    buy_coffee(item)
elif action == "fill":
    fill_machine()
elif action == "take":
    take_money()
    display()
