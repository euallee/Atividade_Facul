import datetime

saberData = datetime.date.today()
aData = saberData.strftime("%d/%m/%y")
#print(aData)
saberHora = datetime.datetime.now()
aHora = saberHora.strftime("%H:%M:%S")
#print(aHora)

kgCompra1 = float(input("Quantos Kg de Morangos foram compradas? "))
kgCompra2 = float(input("Quantos Kg de Maçãs foram compradas? "))

formaPag = []
carrinhoKg = []
carrinhoReal = []

carrinhoKg.append(kgCompra1)
carrinhoKg.append(kgCompra2)
kg = sum(carrinhoKg)
#print(f"Total Kg: {kg:,.0f}Kg")

while True:
    pagamento = input('''
    ----------------------------
    |    FORMA DE PAGAMENTO    |
    ----------------------------
        [1]   PIX
        [2]   DINHEIRO
        [3]   CARTÃO DE CRÉDITO
        [4]   CARTÃO DE DÉBITO
    ----------------------------
    PAGAMENTO: ''')

    if pagamento == "1":
        pag = "PIX"
        formaPag.append(pag)
        break
    elif pagamento == "2":
        pag = "DINHEIRO"
        formaPag.append(pag)
        break
    elif pagamento == "3":
        pag = "CARTÃO DE CRÉDITO"
        formaPag.append(pag)
        break
    elif pagamento == "4":
        pag = "CARTÃO DE DÉBITO"
        formaPag.append(pag)
        break
    else:
        print("Forma de pagamento não disponivel! Tente de novo.")

if kgCompra1 <= 5:
    valor1 = 2.5
    morangoReal1 = kgCompra1 * valor1
    qtd1 = (kgCompra1 * valor1)/valor1
    #print(f"Preço do morango até 5Kg: R${morangoReal1:,.2f}")
    carrinhoReal.append(morangoReal1)
else:
    valor1 = 2.2
    morangoReal1 = kgCompra1 * valor1
    qtd1 = (kgCompra1 * valor1)/valor1
    #print(f"Preço do morango depois de 5Kg: R${morangoReal1:,.2f}")
    carrinhoReal.append(morangoReal1)

if kgCompra2 <= 5:
    valor2 = 1.8
    macaReal2 = kgCompra2 * valor2
    qtd2 = (kgCompra2 * valor2)/valor2
    #print(f"Preço da maçã até 5Kg: R${macaReal2:,.2f}")
    carrinhoReal.append(macaReal2)
else:
    valor2 = 1.5
    macaReal2 = kgCompra2 * valor2
    qtd2 = (kgCompra2 * valor2)/valor2
    #print(f"Preço da maçã depois de 5Kg: R${macaReal2:,.2f}")
    carrinhoReal.append(macaReal2)

real = sum(carrinhoReal)

if kg > 8 or real > 25:
    porcentagem = 0.10
    desc = real - (real * porcentagem)
    diferenca = desc - real
    print(f'''
HORTIFRUTI DO ALÊ LTDA.
Rua River Shopping, 6000, Centro - Petrolina - PE
CNPJ:99.123.342/0001-32
----------------------------------------------------------------
{aData} {aHora}
                           NOTA FISCAL
| ITEM | CÓDIGO | DESCRIÇÃO | QTD. | VL. UNIT. (R$) | VL. ITEM |
----------------------------------------------------------------
    1       2      MORANGO     {qtd1:.0f}          {valor1:,.2f}         {morangoReal1:,.2f}
    2       4       MAÇÃ       {qtd2:.0f}          {valor2:,.2f}         {macaReal2:,.2f}
                                                    ------------
                    TOTAL KG   {kg:.0f}         TOTAL R$     {real:,.2f}
DIFERENÇA R$                                           {diferenca:,.2f}
TOTAL COM DESCONTO R$                                  {desc:,.2f}   
FORMA DE PAGAMENTO: {pag}

Val Aprox dos Tributos  R$  95,32  (48,97%)  Fonte: IPIRANGA

VOLTE SEMPRE!!!!!!!!!!!!!!!!! :)
----------------------------------------------------------------
VERSÃO DA NF 00.123.321 FEITA POR: ALEXANDER JOSHUA
DATA: 01/04/2023 HORA: 22:38:20
PIX PARA CONTRIBUIÇÃO: alexanderjoshua2004@gmail.com
                                                            BR
''')

else:
    diferenca = 0.00
    desc = "SEM DESCONTO"
    print(f'''
HORTIFRUTI DO ALÊ LTDA.
Rua River Shopping, 6000, Centro - Petrolina - PE
CNPJ:99.123.342/0001-32
----------------------------------------------------------------
{aData} {aHora}
                           NOTA FISCAL
| ITEM | CÓDIGO | DESCRIÇÃO | QTD. | VL. UNIT. (R$) | VL. ITEM |
----------------------------------------------------------------
    1       2      MORANGO     {qtd1:.0f}          {valor1:,.2f}         {morangoReal1:,.2f}
    2       4       MAÇÃ       {qtd2:.0f}          {valor2:,.2f}         {macaReal2:,.2f}
                                                    ------------
                    TOTAL KG   {kg:.0f}         TOTAL R$     {real:,.2f}
DIFERENÇA R$                                           {diferenca}
TOTAL COM DESCONTO R$                            {desc}   
FORMA DE PAGAMENTO: {pag}

Val Aprox dos Tributos  R$  95,32  (48,97%)  Fonte: IPIRANGA

VOLTE SEMPRE!!!!!!!!!!!!!!!!! :)
----------------------------------------------------------------
VERSÃO DA NF 00.123.321 FEITA POR: ALEXANDER JOSHUA
DATA: 01/04/2023 HORA: 22:38:20
PIX PARA CONTRIBUIÇÃO: alexanderjoshua2004@gmail.com
                                                            BR
''')