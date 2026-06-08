import re
codigo = 'nao sei oque nao 1234 que la '

saida = re.findall(r'\d+',codigo)[0]
print(saida)