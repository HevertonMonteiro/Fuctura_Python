mesa = 4
pessoas = int(input("Quantas pessoas irão jantar? "))

if pessoas > mesa:
    quantidade_mesas = pessoas // mesa
    if pessoas % mesa != 0:
        quantidade_mesas += 1
    print(f"Serão necessárias {quantidade_mesas} mesas para acomodar todas as pessoas.")
elif pessoas == 0:
    print("Nenhuma mesa é necessária.")
else:
    print("Apenas uma mesa é suficiente para acomodar todas as pessoas.")