import json 
from datetime import datetime, datetime, timedelta

name = input (" Informe seu nome: ")
age = int (input (" Informe sua idade: "))	
register =  float (input (" Informe uma senha para regitro: "))  
pasword = float (input (" Informe sua senha para login: "))	 

while (pasword != register):
	print (" Senha incorreta, tente novamente. ")
	pasword = float (input (" Informe sua senha para login: "))
print (f" Seja bem vindo(a) {name}, seu login foi realizado com sucesso! ")
 
while (0!= 4):
	print("""
		[1]menu 
		[2]faça um agendamento
		[3]meus agendamentos
		[4]sair
		""")
	opcao = int(input("Digite sua opção: "))

def opcao(valor):
 match valor:
		case 1:
			print("Opção 1 selecionada")
		case 2:
			print("Opção 2 selecionada")
		case 3:
			print("Opção 3 selecionada")
		case 4:
			print("Saindo do programa...")
			return



            