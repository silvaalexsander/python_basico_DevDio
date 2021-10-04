#metodo eh uma DEF
'''
class Calculadora:
    def __init__(self, num, num2):
        self.a = num
        self.b = num2 #iniciando as variaveis

    def soma(self):#COMO O METODO ESTA DENTRO DE UMA CLASSE, OS PARAMETROS TER'AO QUE SER SELF
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


calculadora = Calculadora(10, 2) #instanciando a classe
print(calculadora.soma())
print(calculadora.sub())
print(calculadora.mult())
print(calculadora.div())
'''
class Calculadora:
    def __init__(self):
        pass

    def soma(self, a, b):#COMO O METODO ESTA DENTRO DE UMA CLASSE, OS PARAMETROS TER'AO QUE SER SELF
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

