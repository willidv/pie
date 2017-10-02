class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
        self.displayed = False
        self.ridden = False
        self.reversed = False
    def displayinfo(self):
        self.displayed = True
        print self.price , self.max_speed , self.miles
        return self
        displayinfo.__call__
    def ride(self):
        self.ridden = True
        if self.ridden == True:
            print "Riding"
            self.miles = self.miles + 10
            print self.miles
        return self
    def reverse(self):
        self.reversed = True
        print "Reversing"
        self.miles = self.miles -5
        print self.miles
        return self
bike1 = Bike("100$", "40mph", 0)
bike2 = Bike("200$", "50mph", 0)
bike3 = Bike("300$", "60mph", 0)
