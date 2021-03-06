from unittest import TestCase

from Calculadora import Calculadora

class CalculadoraTest(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora().sumar(""), 0, "Cadena vacia")

    def test_sumar_unacadena(self):
        self.assertEqual(Calculadora().sumar("1"), 1, "Un numero")

    def test_sumar_cadenasConUnNumero(self):
        self.assertEqual(Calculadora().sumar("1"), 1, "Un numero")
        self.assertEqual(Calculadora().sumar("2"), 2, "Un numero")

    def test_sumar_cadenaConDosNumero(self):
        self.assertEqual(Calculadora().sumar("1,3"), 4, "Dos numeros")

    def test_sumar_cadenaConMultiplesNumero(self):
        self.assertEqual(Calculadora().sumar("5,2,4,1"), 12, "Multiples numeros")

    def test_sumar_cadenaConMultiplesNumeroConSeparadores(self):
        self.assertEqual(Calculadora().sumar("5,2&4:1:2&8"), 22, "Multiples numeros distintos separadores")
