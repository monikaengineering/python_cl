class Dryer(object):
    condition = "new"
    def __init__(self,brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color
    def show_dryer(self):
        return ("This is a" + self.color + " " + self.brand + " " + self.model + " dryer.")
    def use_dryer(self):
        self.condition = " used "
my_dryer = Dryer("Ecolux" , "Natural" , "silver")
print(my_dryer.show_dryer())
print(my_dryer.condition)
my_dryer.use_dryer()
print(my_dryer.condition)