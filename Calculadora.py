class Calculadora:
    def sumar(self, cadena):
        if cadena == "":
            return 0
        elif  "," in cadena:
            numeros = cadena.split(",")
            suma = 0
            for num in numeros:
                suma+=int(num)
            return suma
        else:
            return int(cadena)