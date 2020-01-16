import datetime

class Building:
    def __init__(self, name, address, stories):
        self.name = name
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


