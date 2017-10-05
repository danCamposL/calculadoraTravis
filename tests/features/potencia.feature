Feature: Potencia de dos numeros
	Como usuario de la calculadora
	deseo realizar la potencia de dos numeros
	para obtener el resultado preciso

	Scenario: Potencia de 2 elevado 2
		Dado que ingreso los numeros "2" elevado "2"
		cuando realizo la operación
		entonces obtengo el resultado "4"

	Scenario: Potencia de 7 elevado 5
		Dado que ingreso los numeros "10" elevado "5"
		cuando realizo la operación
		entonces obtengo el resultado "100000"

	Scenario: Potencia de 0 elevado 7
		Dado que ingreso los numeros "0" elevado "7"
		cuando realizo la operación
		entonces obtengo el resultado "0"

	Scenario: Potencia de 1000 elevado 100
		Dado que ingreso los numeros "10" elevado "6"
		cuando realizo la operación
		entonces obtengo el resultado "1000000"
