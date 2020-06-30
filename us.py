import food

class ChlorinatedChicken(food.Chicken):
    def eat(self):
        super().eat()
        print("you die")

chlorinated_chicken = ChlorinatedChicken()
