class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.aBig = big
        self.aMed = medium
        self.aSmall = small

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if(carType == 3):
            if self.aSmall >= 1:
                self.aSmall -= 1
                return True
            else:
                return False
        elif(carType == 2):
            if self.aMed >= 1:
                self.aMed -= 1
                return True
            else:
                return False
        else:
            if self.aBig >= 1:
                self.aBig -= 1
                return True
            else:
                return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
