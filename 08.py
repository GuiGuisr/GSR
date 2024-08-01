##  Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite

## Velocidade superior à máxima em mais de 20% e até 50% (infração grave): valor de R$ 195,23 e 5 pontos descontados da carteira; Velocidade superior à máxima em mais de 50% (infração gravíssima): a multa deve ser multiplicada em três vezes - desta forma, deverá ser pago o valor de R$ 880,41 (R$ 293,47 x 3).

cont1 = 0
cont2 = 0
while True:
    
    veloc = float(input("Qual a velocidade que você estava ? "))
    limit = float(input("Qual era o limite permitido ? "))

    c = veloc-limit
    l1 = (limit * 0.20) + limit
    l2 = (limit * 0.50) + limit

    if veloc>= l1 and veloc < l2: 
        print(f'Você estava {c} Km/h acima do permitido. Velocidade superior à máxima em mais de 20% e até 50% (infração grave): valor de R$ 195,23 e 5 pontos descontados da carteira! ')
        cont1 = cont1 + 1
    
    elif veloc >= l2:
        print(f'Você estava a {c} Km/h acima do permitido. Velocidade superior à máxima em mais de 50% (infração gravíssima): a multa deve ser multiplicada em três vezes - desta forma, deverá ser pago o valor de R$ 880,41 (R$ 293,47 x 3). ')
        cont2 = cont2 + 1
    variavel = input()
    k = str(input("Deseja consultar suas multas ? ")).lower().strip()[0]
    if k == "n":
    
        print(f"Você teve {cont1} infração grave contabilizadas no valor de R$ 195,23 \n {cont2} infração gravíssima contabilizadas no valor de 880,41")
    
    variavel = input()




