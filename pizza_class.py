class Pizza:

    def __init__(self):
        self.crust_type = ""
        self.crust_toss = ""
        self.cheese = ""
        self.toppings = set()
        self.size = ""

    def add_topping(self, new_topping):
        self.toppings.add(new_topping)

    def order(self):
        topping_list = ""
        for item in self.toppings:
            topping_list += f" {item}"
        print(f'I would like a {self.size}", {self.crust_type}, {self.crust_toss} pizza with{topping_list} and {self.cheese} cheese.')