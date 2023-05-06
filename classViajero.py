class ViajeroFrecuente:
    __numViajero = 0
    __dni = ""
    __nom = ""
    __ape = ""
    __millasAc = 0
    def __init__(self, num, dni, nom, ape, mil):
        self.__numViajero = num
        self.__dni = dni
        self.__nom = nom
        self.__ape = ape
        self.__millasAc = mil
    def cantidadTotalMillas(self):
        return self.__millasAc
    def acumularMillas(self, millas):
        self.__millasAc = self.__millasAc + millas
        return self.__millasAc
    def canjearMillas(self, millasCanje):
        self.__millasAc = self.__millasAc - millasCanje
        return self.__millasAc
    def getNumero(self):
        return self.__numViajero