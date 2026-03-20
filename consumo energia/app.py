aparelho = input ("Informe o nome do aparelho")
potencia = float (input ("informe a potência do aparelho em watts"))
tempo = float (input ("informe o tempo de uso do aparelho em horas por dia"))
consumo = (potencia * tempo * 30) / 1000
valor_kwh = 0.75
custo = consumo * valor_kwh
print(f"\nAparelho: {aparelho}")
print(f"Consumo estimado: {consumo:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo:.2f} por mês")


