tabu = int(input("Qual a tabuada que dejesa usar: "))

for i in range(0, 11):
    calc = tabu * i
    print(f'{i} X {tabu} = {calc}')