import json
from datetime import datetime, datetime, timedelta 
json_string = '''{
	"produtos": [{
		"id": 101,
		"categoria": "Roupas",
		"tipo": "Camiseta",
		"marca": "Marca A",
		"descricao": "Camiseta 100% algodão, manga curta, disponível em várias cores",
		"tamanhos": ["P", "M", "G", "GG"],
		"cores": ["Preto", "Branco", "Azul", "Cinza"],
		"preco": 69.90,
		"estoque": 120
	},
	{
		"id": 102,
		"categoria": "Roupas",
		"tipo": "Calça Jeans",
		"marca": "Marca B",
		"descricao": "Calça jeans masculina, corte reto, lavagem escura",
		"tamanhos": ["38", "40", "42", "44"],
		"cores": ["Azul Escuro"],
		"preco": 149.90,
		"estoque": 80
	},
	{
		"id": 201,
		"categoria": "Calçados",
		"tipo": "Tênis Esportivo",
		"marca": "Marca C",
		"descricao": "Tênis leve para corrida, solado antiderrapante, respirável",
		"tamanhos": [38, 39, 40, 41, 42, 43],
		"cores": ["Branco", "Preto", "Cinza"],
		"preco": 199.90,
		"estoque": 60
	}]
}'''
dados = json.loads(json_string)  
print ( " >>  Loja  Senai  << " )   
print (" Pressione enter para prosseguir ")
input()
for i in range(1):
	id_compra = input("Informe o id da compra ")

produto_encontrado = False
for produto in dados["produtos"]:
	if str(produto["id"]) == id_compra:
		print(f"ID: {produto['id']}")
		print(f"Tipo: {produto['tipo']}")
		print(f"Descrição: {produto['descricao']}")
		print(f"Categoria: {produto['categoria']}")
		print(f"Marca: {produto['marca']}")
		print(f"Preço: {produto['preco']}")
		print(f"Estoque: {produto['estoque']}")
		produto_encontrado = True
		break

if not produto_encontrado:
	print("Produto não encontrado.")
   
 


