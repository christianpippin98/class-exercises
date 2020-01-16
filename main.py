from classes import Pizza

meat_lovers = Pizza()
meat_lovers.size = 20
meat_lovers.crust_toss = "hand-tossed"
meat_lovers.crust_type = "gluten-free"
meat_lovers.cheese = "mozzarella"
meat_lovers.add_topping("pepperoni")
meat_lovers.add_topping("bacon")
meat_lovers.add_topping("sausage")
meat_lovers.add_topping("ham")
meat_lovers.order()

veggie = Pizza()
veggie.size = 18
veggie.crust_toss = "thin"
veggie.crust_type = "flour"
veggie.cheese = "cheddar"
veggie.add_topping("spinach")
veggie.add_topping("mushroom")
veggie.add_topping("tomato")
veggie.add_topping("artichoke")
veggie.order()