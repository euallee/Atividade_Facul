dep = int(input("Valor a ser despositado: "))
tax = float(input("Valor taxa poupança: "))
x = 1
valorMes = []
while x <=12:
    ganhosTotais = dep * tax
    dep += ganhosTotais
    valorMes.append(ganhosTotais)
    moneyAno = sum(valorMes)
    print(f"No mês {x} você ganhou R${ganhosTotais:,.2f}")
    x += 1
print(f"Valor total por ano é de R${moneyAno:,.2f}")