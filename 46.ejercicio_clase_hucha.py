class Hucha:
    def __init__(self, importe_inicial=0):
        self.__importe = importe_inicial

    def obtener_importe(self):
        return self.__importe

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__importe += cantidad
        else:
            print("la cantidad ingresada debe ser mayor que 0")

    def sacar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__importe:
            self.__importe -= cantidad
            print(f"el saldo actual es: {self.__importe}")
        else:
            print("la cantidad ingresada debe ser mayor que 0 y no puede exceder el importe actual")

    def mostar_importe(self):
        return f"el importe actual en la huca  es: {self.__importe}"


mihucha = Hucha(100)
mihucha.ingresar(50)
print(mihucha.mostar_importe())
mihucha.sacar(100)
#print(mihucha.mostar_importe())
print(mihucha.obtener_importe())
