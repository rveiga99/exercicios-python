class Calculadora:

    def calcular(self, op, num1, num2):
        if op == "+":
            return self.__adicionar(num1, num2)

        elif op == "-":
            return self.__subtrair(num1, num2)

        else:
            print("Operação Inválida")

    def __adicionar(self,num1, num2):
        return num1 + num2

    def __subtrair(self,num1, num2):
        return num1 - num2

calculadora = Calculadora()
resultado = calculadora.calcular("+", 10, 20)
print(resultado)
resultado1 = calculadora.calcular("-", 10, 20)
print(resultado1)
resultado2 = calculadora.calcular("*", 10, 20)
print(resultado2)