# Decorator/alldecorators/CoffeeShop.py
# Coffee example using decorators
class SaborComponent:
    def getDescription(self):
        return self.__class__.__name__
    
    def getTotalCost(self):
        return self.__class__.cost

class Massa(SaborComponent):
    cost = 10.0

class Decorator(SaborComponent):
    def __init__(self, saborComponent):
        self.component = saborComponent
    
    def getTotalCost(self):
        return self.component.getTotalCost() + SaborComponent.getTotalCost(self)
    
    def getDescription(self):
        return self.component.getDescription() + ' '+SaborComponent.getDescription(self)


class Calabresa(Decorator):
    cost = 5.0
    def __init__(self, saborComponent):
        Decorator.__init__(self, saborComponent)

class Pepperoni(Decorator):
    cost = 8.0
    def __init__(self, saborComponent):
        Decorator.__init__(self, saborComponent)

class Mussarela(Decorator):
    cost = 5.0
    def __init__(self, saborComponent):
        Decorator.__init__(self, saborComponent)

class Chevre(Decorator):
    cost = 7.5
    def __init__(self, saborComponent):
        Decorator.__init__(self, saborComponent)

class Mel(Decorator):
    cost = 2.5
    def __init__(self, saborComponent):
        Decorator.__init__(self, saborComponent)

class Chocolate(Decorator):
    cost = 10.0
    def __init__(self, saborComponent):
        Decorator.__init__(self, saborComponent)


if __name__ == '__main__':
    chevreEtMiel = Chevre(Mel(Massa()))
    print(chevreEtMiel.getDescription()+ ": $" + str(chevreEtMiel.getTotalCost()))
    calabresa = Calabresa(Mussarela(Massa( )))
    print(calabresa.getDescription()+ ": $" + str(calabresa.getTotalCost()))
    pepperoni = Pepperoni(Mussarela(Massa( )))
    print(pepperoni.getDescription()+ ": $" + str(pepperoni.getTotalCost()))