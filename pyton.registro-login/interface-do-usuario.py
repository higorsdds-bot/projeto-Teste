
def login():
	name_register = input(" resgistre seu nome: ")
	nivel_acess = int(input(" informe o nivel de acesso -> 1] ADM, 2] comum "))
	register_acess = input(" registre uma senha \n -> ")
	# informações passadas pelo usuário. Logo abaixo verificação para prosseguir 

	name = input(" Informe sua nome: ")
	password = input("  Informe sua senha: " )

	# verifica se o usuário e a senha coincidem com o cadastro
	if name == name_register and password == register_acess:
		if nivel_acess == 1:
			print(" Bem vindo, administrador ")
		elif nivel_acess == 2:
			print(f" Bem vindo {name}")
		else:
			print(" Nível de acesso inválido ")
	else:
		print(" Usuário ou senha incorreto ")
	return

login()
# SEGUNDO PROGRAMA ------------------ |||
 
print ("\t ^^ TABELA DE AVALIAÇÃO ^^ ")

num_students = int(input(" Informe quantos aluno deseja avaliar: "))
students = []
for i in range(num_students):
 name = input(" Informe o nome do aluno: ")
 note = float(input(f" Informe a nota do {name}: "))
 observation = (input(" Informe o comportamento: "))
 students.append({"name": name, "note": note, "observação": observation})

print("\nResultados:")
for s in students:
    
	print(f"{s['name']}: {s['note']}: {s['observação']}")
 
 

   







 