import numpy as np
import random

# Classes dos canais
from Cenário1 import RuidoNuloCanalUnitario
from Cenário2 import BaixoRuidoCanalUnitario
from Cenário3 import BaixoRuidoCanalRayleigh
from Cenário4 import AltoRuidoCanalUnitario
from Cenário5 import AltoRuidoCanalRayleigh
from Plotagem import Plotagem

# Variáveis globais
media = 0.5
variancia = 1.5

x = []

# Solicita ao usuário a quantidade de testes
ntestes = int(input("Entre com a quantidade de testes: "))

print("Entre com um dos valores possiveis para o tamanho da cadeia de Bits")
nBits = int(input("7 Bits, 15 Bits, 31 Bits, 63 Bits,127 Bits ou 255 Bits\n"))

# Gera uma lista de bits aleatórios (0 ou 1)
for i in range(nBits):
    x.append(random.randint(0, 1))

# Define o tamanho e os parâmetros de escala para a distribuição de Rayleigh
size = nBits
scale1 = 0.9
scale2 = 1.01
h1 = np.random.rayleigh(scale1, size)
h2 = np.random.rayleigh(scale2, size)

ruidoNuloCanalUnitario = RuidoNuloCanalUnitario(media, variancia, ntestes)
baixoRuidoCanalUnitario = BaixoRuidoCanalUnitario(media, variancia, ntestes)
baixoRuidoCanalRayleigh = BaixoRuidoCanalRayleigh(media, variancia, ntestes)
altoRuidoCanalUnitario = AltoRuidoCanalUnitario(media, variancia, ntestes)
altoRuidoCanalRayleigh = AltoRuidoCanalRayleigh(media, variancia, ntestes)

def coletar_porcentagens():
    porcentagens = []
    porcentagens.append(ruidoNuloCanalUnitario.cenario(x, h1, h2, media, variancia, ntestes, nBits))
    porcentagens.append(baixoRuidoCanalUnitario.cenario(x, h1, h2, media, variancia, ntestes, nBits))
    porcentagens.append(baixoRuidoCanalRayleigh.cenario(x, h1, h2, media, variancia, ntestes, nBits))
    porcentagens.append(altoRuidoCanalUnitario.cenario(x, h1, h2, media, variancia, ntestes, nBits))
    porcentagens.append(altoRuidoCanalRayleigh.cenario(x, h1, h2, media, variancia, ntestes, nBits))
    return porcentagens

# Executa os cenários e coleta as porcentagens de acertos
porcentagens = coletar_porcentagens()

# Instancia a classe de plotagem
plotagem = Plotagem()

# Plota os resultados
plotagem.plota_resultados(porcentagens)

