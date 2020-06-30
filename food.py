class Food(object):
    def eat(self):
        print("you eat " + self.__class__.__name__)
        
class Chicken(Food):
    pass
