from building import Building
from city import City

five_hundred_fifty_five_fifth = Building("Five's", "555 5th St", 34)
four_twentieth = Building("Mary Jane's", "4 20th St", 21)
twelfth_and_jefferson = Building("Montichello", "12th and Jefferson", 100)
six_bleeker = Building("The New York Sanctum", "6 Bleeker St", 3)
stark_tower = Building("Stark Tower", "600 Broadway", 150)

stark_tower.purchase("Tony Stark")
six_bleeker.purchase("Dr. Strange")
twelfth_and_jefferson.purchase("Thomas")
five_hundred_fifty_five_fifth.purchase("Jeff Bezos")
four_twentieth.purchase("Cheech and Chong")

stark_tower.construct()
four_twentieth.construct()
six_bleeker.construct()
five_hundred_fifty_five_fifth.construct()
twelfth_and_jefferson.construct()

gothom = City("Gothom City", "Alfred")

gothom.add_building(stark_tower)
gothom.add_building(six_bleeker)
gothom.add_building(five_hundred_fifty_five_fifth)
gothom.add_building(four_twentieth)
gothom.add_building(twelfth_and_jefferson)

for building in gothom.buildings:
    print(f"\n{building.name} is on {building.address}. It has {building.stories} stories and is owned by {building.owner}. It was built on {building.date_constructed.strftime('%x')} by {building.designer}.")