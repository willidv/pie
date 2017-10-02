class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
        self.returned = False
        self.box_opened = False
        self.defective = False

    def sell(self):
        self.status = "sold"
        if self.status == "sold":
            self.price = float(self.price) + self.price * .15
            return self

    def returned(self):
        self.returned = True
        if self.defective:
            self.status = "defective"
            self.price = 0
            return self
        if box_opened:
            self.status = "used"
            self.price = float(self.price) / .20
            return self
        elif box_opened == False:
            self.status = "for sale"
            self.price = price
            return self
            




        