class bike():
    def  __init__(self,price,max_speed):
        self.miles = 0
        self.price = price
        self.max_speed = max_speed
    def displayinfo(self):
        print "Price is " + self.price
        print "Speed is " + self.max_speed
        print self.miles
        return self
    def ride(self):
        print "Riding..."
        self.miles = self.miles * 10
        return self
    def reverse(self):
        print "Reversing..."
        #keep miles out of negative
        if (self.miles >= 5):
            self.miles -= 5
        return self

bike("$200", "35mph").ride().ride().ride().reverse().displayinfo()
bike("$400", "50mph").ride().ride().reverse().reverse().displayinfo()
bike("$35", "10mph").reverse().reverse().reverse().displayinfo()
