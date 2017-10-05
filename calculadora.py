# -*- coding: utf-8 -*-
#Funcionalidad Calculadora sencilla
#Eduardo Daniel Campos Loera
#Pruebas y Mantenimiento
class Calculadora():

    resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def suma(self, num1, num2):
        try:
            self.resultado = int(num1) + int(num2)
        except ValueError:
                print 'Datos incorrectos'

    def resta(self, num1, num2):
            self.resultado = int(num1) - int(num2)

    def multiplicacion(self, num1, num2):
            self.resultado = int(num1) * int(num2)

    def division(self, num1, num2):
            if int(num2) <= 0:
                print('No se puede dividir entre cero')
            else:
                self.resultado = int(num1) / int(num2)

    def potencia(self, num1, num2):
            self.resultado = int(num1) ** int(num2)

    def raiz(self, num1, num2):
            self.resultado = round(num1**(1.0/num2),1)
