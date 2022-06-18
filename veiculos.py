from abc import ABCMeta, abstractclassmethod

class IVeiculo(metaclass=ABCMeta):

    @abstractclassmethod
    def descricao(self):
        """ Interface da descricao do veiculo """

class Carro(IVeiculo):
    def __init__(self, motor):
        self.motor = motor

    def descricao(self):
        print("Eu sou um Carro "+self.motor.type())


class Caminhao(IVeiculo):
    def __init__(self, motor):
        self.motor = motor

    def descricao(self):
        print("Eu sou um Caminhao "+self.motor.type())

class IMotor(metaclass=ABCMeta):

    @abstractclassmethod
    def type(self):
        """ Interface do motor """

class Eletrico(IMotor):
    def __init__(self):
        return

    def type(self):
        return "Eletrico"

class Hibrido(IMotor):
    def __init__(self):
        return 

    def type(self):
        return "Hibrido"

class Combustao(IMotor):
    def __init__(self):
        return 

    def type(self):
        return "Combustao"

class VeiculoFactory:

    @staticmethod
    def build_veiculo(veiculo_type, choice_motor):
        if choice_motor == "Eletrico":
            motor = Eletrico()
        elif choice_motor == "Hibrido":
            motor = Hibrido()
        elif choice_motor == "Combustao":
            motor = Combustao()
        else:
            print("Motor Invalido")
            return -1
        
        if veiculo_type == "Carro":
            return Carro(motor)
        if veiculo_type == "Caminhao":
            return Caminhao(motor)
        print("Veiculo invalido")
        return -1

if __name__ == "__main__":
    choice_veiculo  = input("Qual veiculo sera criado?\n")
    choice_motor = input("Qual o motor do seu veiculo?\n")
    Veiculo = VeiculoFactory.build_veiculo(choice_veiculo, choice_motor)
    Veiculo.descricao()