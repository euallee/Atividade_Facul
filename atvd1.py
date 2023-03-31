import time
    
qtdCombustivel = float(input('''
+--------------------------+
|Bem-vindo ao Posto do Alê!|
|==========================|
|  Preço dos combustíveis  |
|    -> Álcool R$3,50      |
|    -> Gasolina R$5,67    |
+--------------------------+
    	
Quantos litros de combustível: '''))
    
time.sleep(1)

while True:
    
    print(f'''
    +-------------------------------------+
    |    Você gostaria abastecer com?     |
    |=====================================|
    | [ A ] - Álcool     [ G ] - Gasolina |
    +-------------------------------------+
    ''')
    
    time.sleep(1)
    
    tipoCombustivel = input('''
    Tipo do combustível: ''')
    convertTipo = tipoCombustivel.upper()
    
    alcool = 3.50 * qtdCombustivel
    gasolina = 5.67 * qtdCombustivel
    
    descontoUm = 0.03
    descontoDois = 0.05
    
    descontoTres = 0.04
    descontoQuatro = 0.06
    
    if convertTipo == 'A':
        if alcool <= 20:
            combustivelDesconto = alcool-(alcool*descontoUm)
            print("Fazendo resumo do pedido...")
            time.sleep(2)
            print("Abastecendo...")
            time.sleep(2)
            print(f'''
            +--------------------+
            |       Resumo       |
            |                    |
            | Litros(L): {qtdCombustivel}
            | Tipo: {convertTipo}
            | Preço: {alcool:.2f}
            | Preço com desconto
            | de 3%: {combustivelDesconto:.2f}
            +--------------------+''')
            break
        elif alcool >= 20:
            combustivelDesconto = alcool-(alcool*descontoDois)
            print("Fazendo resumo do pedido...")
            time.sleep(2)
            print("Abastecendo...")
            time.sleep(2)
            print(f'''
            +--------------------+
            |       Resumo       |
            |                    |
            | Litros(L): {qtdCombustivel}
            | Tipo: {convertTipo}
            | Preço: {alcool:.2f}
            | Preço com desconto
            | de 5%: {combustivelDesconto:.2f}
            +--------------------+''')
            break
        else:
            print("Nenhum desconto aplicado.")
            break
            
    elif convertTipo == 'G':
        if gasolina <= 20:
            combustivelDesconto = gasolina-(gasolina*descontoTres)
            print("Fazendo resumo do pedido...")
            time.sleep(2)
            print("Abastecendo...")
            time.sleep(2)
            print(f'''
            +--------------------+
            |       Resumo       |
            |                    |
            | Litros(L): {qtdCombustivel}
            | Tipo: {convertTipo}
            | Preço: {gasolina:.2f}
            | Preço com desconto
            | de 4%: {combustivelDesconto:.2f}
            +--------------------+''')
            break
        elif gasolina >= 20:
            combustivelDesconto = gasolina-(gasolina*descontoQuatro)
            print("Fazendo resumo do pedido...")
            time.sleep(2)
            print("Abastecendo...")
            time.sleep(2)
            print(f'''
            +--------------------+
            |       Resumo       |
            |                    |
            | Litros(L): {qtdCombustivel}
            | Tipo: {convertTipo}
            | Preço: {gasolina:.2f}
            | Preço com desconto
            | de 6%: {combustivelDesconto:.2f}
            +--------------------+''')
            break
        else:
            print("Nenhum desconto aplicado.")
            break
            
    else:
        print("Escolha as opções existentes.")