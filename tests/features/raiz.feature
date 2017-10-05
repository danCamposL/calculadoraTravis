Feature: Raiz de dos numeros
	Como usuario de la calculadora
	deseo realizar la raíz de dos numeros
	para obtener el resultado preciso

	Scenario: Raiz de 2 raiz 2
		Dado que ingreso los numeros "2" raiz "2"
		cuando realizo la operación
		entonces obtengo el resultado "1"

	Scenario: Raiz de 10 raiz 5
		Dado que ingreso los numeros "10" raiz "5"
		cuando realizo la operación
		entonces obtengo el resultado "2"

	Scenario: Raiz de 0 raiz 7
		Dado que ingreso los numeros "0" raiz "7"
		cuando realizo la operación
		entonces obtengo el resultado "0"

	Scenario: Raiz de 10 raiz 6
		Dado que ingreso los numeros "10" raiz "6"
		cuando realizo la operación
		entonces obtengo el resultado "1"
