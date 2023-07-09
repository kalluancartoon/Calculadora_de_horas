horas_dia = input("Quantas horas você trabalha por dia ?")
horas_semanal = int(horas_dia) * 5
horas_trabalhadas_por_mes = horas_semanal * 5
salario_mensal = input("Qual é o seu salario mensal ?")
valor_hora = int(salario_mensal) / int(horas_trabalhadas_por_mes)
print(valor_hora)  