import datetime

class Building:
    def __init__(self, address, stories):
        self.designer = "Christian Pippin"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()
        print(f"{self.address} was purchased by {self.owner} on {self.date_constructed.strftime('%x')} and has {self.stories} stories.")

    def purchase(self, purchaser):
        self.owner = purchaser


five_hundred_fifth = Building("500 5th St", 34)
four_twentieth = Building("4 20th St", 21)
twelfth_and_jefferson = Building("12th and Jefferson", 100)
six_bleeker = Building("6 Bleeker St", 3)
stark_tower = Building("600 Broadway", 150)

stark_tower.purchase("Tony Stark")
six_bleeker.purchase("Dr. Strange")
twelfth_and_jefferson.purchase("Thomas")
five_hundred_fifth.purchase("Jeff Bezos")
four_twentieth.purchase("Cheech and Chong")

stark_tower.construct()
four_twentieth.construct()
six_bleeker.construct()
five_hundred_fifth.construct()
twelfth_and_jefferson.construct()