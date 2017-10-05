# -*- coding: utf-8 -*-
#Pruebas unitarias para Calculadora sencilla
#Eduardo Daniel Campos Loera

import unittest

from calculadora import Calculadora

class CalculadoraTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_valor_de_inicio_igual_a_cero(self):
        self.calc = Calculadora()
        self.assertEquals(self.calc.obtener_resultado(), 0)

    def test_sumar_2_mas_2_igual_4(self):
        self.calc.suma(2,2)
        self.assertEquals(self.calc.obtener_resultado(), 4)

    def test_suma_negativa(self):
        self.calc.suma(4,-1)
        self.assertEquals(self.calc.obtener_resultado(), 3)

    def test_suma_letra(self):
        self.calc.suma('w',-1)
        self.assertEquals(self.calc.obtener_resultado(), 0)

    def test_resta(self):
        self.calc.resta(3,1)
        self.assertEquals(self.calc.obtener_resultado(), 2)

    def test_resta_num2_negativo(self):
        self.calc.resta(3, -1)
        self.assertEquals(self.calc.obtener_resultado(), 4)

    def test_resta_negativo(self):
        self.calc.resta(-3, -1)
        self.assertEquals(self.calc.obtener_resultado(), -2)

    def test_resta_letra(self):
        self.calc.suma('w',-1)
        self.assertEquals(self.calc.obtener_resultado(), 0)

    def test_multiplicacion(self):
        self.calc.multiplicacion(6,8)
        self.assertEquals(self.calc.obtener_resultado(), 48)

    def test_multiplicacion_por_cero(self):
        self.calc.multiplicacion(6,0)
        self.assertEquals(self.calc.obtener_resultado(), 0)

    def test_multiplicacion_letra(self):
        self.calc.suma('w',-1)
        self.assertEquals(self.calc.obtener_resultado(), 0)

    def test_division(self):
        self.calc.division(8,2)
        self.assertEquals(self.calc.obtener_resultado(), 4)

    def test_division_0(self):
        self.calc.division(8,0)
        self.assertEquals(self.calc.obtener_resultado(), 0)

    def test_division_num1_0(self):
        self.calc.division(0,8)
        self.assertEquals(self.calc.obtener_resultado(), 0)

    def test_division_letra(self):
        self.calc.suma('w',1)
        self.assertEquals(self.calc.obtener_resultado(), 0)

    def test_potencia(self):
        self.calc.potencia(2,3)
        self.assertEquals(self.calc.obtener_resultado(), 8)

    def test_raiz(self):
        self.calc.raiz(25,5)
        self.assertEquals(self.calc.obtener_resultado(), 1.9)

    def test_raiz_letra(self):
        self.calc.suma('w',1)
        self.assertEquals(self.calc.obtener_resultado(), 0)

if __name__ == '__main__':
	unittest.main()
