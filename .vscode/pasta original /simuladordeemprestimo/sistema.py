#simulador de emprestimo
import json 
from datetime import datetime, datetime, timedelta

agora=datetime.now()
print (" Horario de login do sistema ")
print (f"\t {agora:%d/%m/%Y %H:%M:%S} \n") 

print ("\t *Sistema de emprestimo*\n ")
name = input (" Informe seu nome: ")
years = int (input(" Informe sua idade: "))    
valuer = float (input (" Informe seu salario mensal: "))
cessão = int (input (" Informe o valor deseja para seu empréstimo:\n ->  "))  # cessao informação que deseja que seja cedido
parcelas = int (input (" Informe o número das parcelas (12 a 60 meses):\n ->  "))
historico = input ("\n possui nome sujo (sim/não): ").strip().lower()  

valor_parcela = cessão / parcelas

print (f"\n |Cliente, {name}|")
print (f" idade: {years} anos")
print (f" valor do empréstimo solicitado: R$ {cessão:.2f}")
print (f" número de parcelas: {parcelas} meses")     

if historico == "sim":  
    print ("\n Empréstimo negado! \n Motivo: Cliente com nome sujo no SPC/Serasa. ")    
elif valor_parcela > (valuer * 0.3):     # calculo de 30% do salario mensal   
    print ("\n Empréstimo negado! \n Motivo: Valor da parcela excede 30% do salário mensal. ")
else:
    print ("\n Empréstimo aprovado! \n Parabéns, seu empréstimo foi aprovado com sucesso. ")
    print (f" Valor da parcela mensal: R$ {valor_parcela:.2f}\n")
      
agora=datetime.now()
print ("\t Horario de aprovação do empréstimo \n  ")
print (f"\t -> {agora:%d/%m/%Y %H:%M:%S} <-\n ")



