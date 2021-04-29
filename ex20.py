#Problema "tabuada" Ler um número inteiro N, daí mostrar na tela a tabuada de N para 1 a 10. Curso Algorítmos - Nelio Alves

numero = int(input("Digite um número: "))
cont = 0

while cont <= 10:
	tabuada = numero * cont
	print(numero ," x ", cont, " = ", tabuada)
	cont +=1
