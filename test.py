import random

mapQuest2 = ['i34', 'i37', 'i40']
posicaoQuest2 = [0, 1, 2]
pesosQuest2 = [1, 2, 1]
aleatorioQuest2 = random.choices(posicaoQuest2, pesosQuest2, k=1)[0]

print(mapQuest2[aleatorioQuest2])