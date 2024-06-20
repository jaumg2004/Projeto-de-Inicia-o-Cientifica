import numpy as np
import random

# Classes dos canais
from Cenário1 import RuidoNuloCanalUnitario
from Cenário2 import BaixoRuidoCanalUnitario
from Cenário3 import BaixoRuidoCanalRayleigh
from Cenário4 import AltoRuidoCanalUnitario
from Cenário5 import AltoRuidoCanalRayleigh
from Plotagem import Plotagem


# Funções dos cenários
def cenario1():

    ruidoNuloCanalUnitario = RuidoNuloCanalUnitario(media, variancia, ntestes)

    n1 = nBits

    print('x =', x)
    y1 = ruidoNuloCanalUnitario.calculaY(x, n1)
    print('y1 =', y1)
    errosY1 = ruidoNuloCanalUnitario.encontraErros(x, y1)
    print('erros do y1 =', errosY1)
    y2 = ruidoNuloCanalUnitario.calculaY(x, n1)
    print('y2 =', y2)
    errosY2 = ruidoNuloCanalUnitario.encontraErros(x, y2)
    print('erros do y2 =', errosY2)

    toStringY1 = ''.join(map(str, y1))

    if n1 == 7:
        tabela = ['0000000', '1101001', '0101010', '1000011', '1001100', '0100101', '1100110', '0001111',
                  '1110000', '0011001', '1011010', '0110011', '0111100', '1010101', '0010110', '1111111']
    elif n1 == 15:
        tabela = ruidoNuloCanalUnitario.generate_hamming_codes_15_bits()
    elif n1 == 31:
        tabela = ruidoNuloCanalUnitario.generate_space_amostral_sample_31_bits(ntestes)
    elif n1 == 63:
        tabela = ruidoNuloCanalUnitario.generate_space_amostral_sample_63_bits(ntestes)
    elif n1 == 127:
        tabela = ruidoNuloCanalUnitario.generate_space_amostral_sample_127_bits(ntestes)
    elif n1 == 255:
        tabela = ruidoNuloCanalUnitario.generate_space_amostral_sample_255_bits(ntestes)


    P = ruidoNuloCanalUnitario.encontraParidade(y1, tabela)
    chave = ruidoNuloCanalUnitario.comparaSinais(y2, P, tabela)
    print("Chave gerada:",chave)

    contagemDeAcertos = 0
    for bit_chave, bit_y1 in zip(chave, toStringY1):
        if bit_chave == bit_y1:
            contagemDeAcertos += 1

    porcentagem_de_acertos = 100 * contagemDeAcertos / n1

    print(f"Porcentagem de vezes que a chave gerada foi encontrada na tabela: {porcentagem_de_acertos:.2f}%")

    ruidoNuloCanalUnitario.plotar(x, y1, y2, len(x))

    return porcentagem_de_acertos

def cenario2():

    baixoRuidoCanalUnitario = BaixoRuidoCanalUnitario(media, variancia, ntestes)

    n2 = nBits

    print('\nx =', x)
    y1 = baixoRuidoCanalUnitario.calculaY(x, variancia - 1.3, media, n2)
    print('y1 =', y1)
    errosY1 = baixoRuidoCanalUnitario.encontraErros(x, y1)
    print('erros do y1 =', errosY1)
    y2 = baixoRuidoCanalUnitario.calculaY(x, variancia - 1.3, media, n2)
    print('y2 =', y2)
    errosY2 = baixoRuidoCanalUnitario.encontraErros(x, y2)
    print('erros do y2 =', errosY2)

    toStringY1 = ''.join(map(str, y1))

    if n2 == 7:
        tabela = ['0000000', '1101001', '0101010', '1000011', '1001100', '0100101', '1100110', '0001111',
                  '1110000', '0011001', '1011010', '0110011', '0111100', '1010101', '0010110', '1111111']
    elif n2 == 15:
        tabela = baixoRuidoCanalUnitario.generate_hamming_codes_15_bits()
    elif n2 == 31:
        tabela = baixoRuidoCanalUnitario.generate_space_amostral_sample_31_bits(ntestes)
    elif n2 == 63:
        tabela = baixoRuidoCanalUnitario.generate_space_amostral_sample_63_bits(ntestes)
    elif n2 == 127:
        tabela = baixoRuidoCanalUnitario.generate_space_amostral_sample_127_bits(ntestes)
    elif n2 == 255:
        tabela = baixoRuidoCanalUnitario.generate_space_amostral_sample_255_bits(ntestes)


    P = baixoRuidoCanalUnitario.encontraParidade(y1, tabela)
    chave = baixoRuidoCanalUnitario.comparaSinais(y2, P, tabela)
    print("Chave gerada:",chave)

    contagemDeAcertos = 0
    for bit_chave, bit_y1 in zip(chave, toStringY1):
        if bit_chave == bit_y1:
            contagemDeAcertos += 1

    porcentagem_de_acertos = 100 * contagemDeAcertos / n2

    print(f"Porcentagem de vezes que a chave gerada foi encontrada na tabela: {porcentagem_de_acertos:.2f}%")

    baixoRuidoCanalUnitario.plotar(x, y1, y2, len(x))

    return porcentagem_de_acertos

def cenario3():

    baixoRuidoCanalRayleigh = BaixoRuidoCanalRayleigh(media, variancia, ntestes)

    n3 = nBits

    print('\nx =', x)
    y1 = baixoRuidoCanalRayleigh.calculaY(h, x, variancia - 1.3, media, n3)
    print('y1 =', y1)
    errosY1 = baixoRuidoCanalRayleigh.encontraErros(x, y1)
    print('erros do y1 =', errosY1)
    y2 = baixoRuidoCanalRayleigh.calculaY(h, x, variancia - 1.3, media, n3)
    print('y2 =', y2)
    errosY2 = baixoRuidoCanalRayleigh.encontraErros(x, y2)
    print('erros do y2 =', errosY2)

    toStringY1 = ''.join(map(str, y1))

    if n3 == 7:
        tabela = ['0000000', '1101001', '0101010', '1000011', '1001100', '0100101', '1100110', '0001111',
                  '1110000', '0011001', '1011010', '0110011', '0111100', '1010101', '0010110', '1111111']
    elif n3 == 15:
        tabela = baixoRuidoCanalRayleigh.generate_hamming_codes_15_bits()
    elif n3 == 31:
        tabela = baixoRuidoCanalRayleigh.generate_space_amostral_sample_31_bits(ntestes)
    elif n3 == 63:
        tabela = baixoRuidoCanalRayleigh.generate_space_amostral_sample_63_bits(ntestes)
    elif n3 == 127:
        tabela = baixoRuidoCanalRayleigh.generate_space_amostral_sample_127_bits(ntestes)
    elif n3 == 255:
        tabela = baixoRuidoCanalRayleigh.generate_space_amostral_sample_255_bits(ntestes)


    P = baixoRuidoCanalRayleigh.encontraParidade(y1, tabela)
    chave = baixoRuidoCanalRayleigh.comparaSinais(y2, P, tabela)
    print("Chave gerada:",chave)

    contagemDeAcertos = 0
    for bit_chave, bit_y1 in zip(chave, toStringY1):
        if bit_chave == bit_y1:
            contagemDeAcertos += 1

    porcentagem_de_acertos = 100 * contagemDeAcertos / n3

    print(f"Porcentagem de vezes que a chave gerada foi encontrada na tabela: {porcentagem_de_acertos:.2f}%")

    baixoRuidoCanalRayleigh.plotar(x, y1, y2, len(x))

    return porcentagem_de_acertos


def cenario4():

    altoRuidoCanalUnitario = AltoRuidoCanalUnitario(media, variancia, ntestes)

    n4 = nBits

    print('\nx =', x)
    y1 = altoRuidoCanalUnitario.calculaY(x, variancia - 1.3, media, n4)
    print('y1 =', y1)
    errosY1 = altoRuidoCanalUnitario.encontraErros(x, y1)
    print('erros do y1 =', errosY1)
    y2 = altoRuidoCanalUnitario.calculaY(x, variancia - 1.3, media, n4)
    print('y2 =', y2)
    errosY2 = altoRuidoCanalUnitario.encontraErros(x, y2)
    print('erros do y2 =', errosY2)

    toStringY1 = ''.join(map(str, y1))

    if n4 == 7:
        tabela = ['0000000', '1101001', '0101010', '1000011', '1001100', '0100101', '1100110', '0001111',
                  '1110000', '0011001', '1011010', '0110011', '0111100', '1010101', '0010110', '1111111']
    elif n4 == 15:
        tabela = altoRuidoCanalUnitario.generate_hamming_codes_15_bits()
    elif n4 == 31:
        tabela = altoRuidoCanalUnitario.generate_space_amostral_sample_31_bits(ntestes)
    elif n4 == 63:
        tabela = altoRuidoCanalUnitario.generate_space_amostral_sample_63_bits(ntestes)
    elif n4 == 127:
        tabela = altoRuidoCanalUnitario.generate_space_amostral_sample_127_bits(ntestes)
    elif n4 == 255:
        tabela = altoRuidoCanalUnitario.generate_space_amostral_sample_255_bits(ntestes)


    P = altoRuidoCanalUnitario.encontraParidade(y1, tabela)
    chave = altoRuidoCanalUnitario.comparaSinais(y2, P, tabela)
    print("Chave gerada:",chave)

    contagemDeAcertos = 0
    for bit_chave, bit_y1 in zip(chave, toStringY1):
        if bit_chave == bit_y1:
            contagemDeAcertos += 1

    porcentagem_de_acertos = 100 * contagemDeAcertos / n4

    print(f"Porcentagem de vezes que a chave gerada foi encontrada na tabela: {porcentagem_de_acertos:.2f}%")

    altoRuidoCanalUnitario.plotar(x, y1, y2, len(x))

    return porcentagem_de_acertos


def cenario5():

    altoRuidoCanalRayleigh = AltoRuidoCanalRayleigh(media, variancia, ntestes)

    n5 = nBits

    print('\nx =', x)
    y1 = altoRuidoCanalRayleigh.calculaY(h, x, variancia - 1.3, media, n5)
    print('y1 =', y1)
    errosY1 = altoRuidoCanalRayleigh.encontraErros(x, y1)
    print('erros do y1 =', errosY1)
    y2 = altoRuidoCanalRayleigh.calculaY(h, x, variancia - 1.3, media, n5)
    print('y2 =', y2)
    errosY2 = altoRuidoCanalRayleigh.encontraErros(x, y2)
    print('erros do y2 =', errosY2)

    toStringY1 = ''.join(map(str, y1))

    if n5 == 7:
        tabela = ['0000000', '1101001', '0101010', '1000011', '1001100', '0100101', '1100110', '0001111',
                  '1110000', '0011001', '1011010', '0110011', '0111100', '1010101', '0010110', '1111111']
    elif n5 == 15:
        tabela = altoRuidoCanalRayleigh.generate_hamming_codes_15_bits()
    elif n5 == 31:
        tabela = altoRuidoCanalRayleigh.generate_space_amostral_sample_31_bits(ntestes)
    elif n5 == 63:
        tabela = altoRuidoCanalRayleigh.generate_space_amostral_sample_63_bits(ntestes)
    elif n5 == 127:
        tabela = altoRuidoCanalRayleigh.generate_space_amostral_sample_127_bits(ntestes)
    elif n5 == 255:
        tabela = altoRuidoCanalRayleigh.generate_space_amostral_sample_255_bits(ntestes)


    P = altoRuidoCanalRayleigh.encontraParidade(y1, tabela)
    chave = altoRuidoCanalRayleigh.comparaSinais(y2, P, tabela)
    print("Chave gerada:",chave)

    contagemDeAcertos = 0
    for bit_chave, bit_y1 in zip(chave, toStringY1):
        if bit_chave == bit_y1:
            contagemDeAcertos += 1

    porcentagem_de_acertos = 100 * contagemDeAcertos / n5

    print(f"Porcentagem de vezes que a chave gerada foi encontrada na tabela: {porcentagem_de_acertos:.2f}%")

    altoRuidoCanalRayleigh.plotar(x, y1, y2, len(x))

    return porcentagem_de_acertos


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
scale1 = 1.0
h = np.random.rayleigh(scale1, size)

def coletar_porcentagens():
    porcentagens = []
    porcentagens.append(cenario1())
    porcentagens.append(cenario2())
    porcentagens.append(cenario3())
    porcentagens.append(cenario4())
    porcentagens.append(cenario5())
    return porcentagens

# Executa os cenários e coleta as porcentagens de acertos
porcentagens = coletar_porcentagens()

# Instancia a classe de plotagem
plotagem = Plotagem()

# Plota os resultados
plotagem.plota_resultados(porcentagens)

