import random

from CenárioBase import CenárioBase
from Plotagem import Plotagem
from Hamming import HammingCodeGenerator

class AltoRuidoCanalRayleigh(CenárioBase, Plotagem, HammingCodeGenerator):
    def calculaY(self, h, x, variancia, media, ntestes):
        # Função para gerar ruído com distribuição normal
        def geraRuido(variancia, media, ntestes):
            return [random.gauss(media, variancia + 0.2) for _ in range(ntestes)]

        n = geraRuido(variancia, media, ntestes)
        y = [h[i] * x[i] + n[i] for i in range(ntestes)]
        return [1 if y[i] > 0.5 else 0 for i in range(ntestes)]

    def cenario(self, x, h1, h2, nBits):

        n5 = nBits

        print('x =', x)
        y1 = self.calculaY(x, h1, self.variancia, self.media, n5)
        print('y1 =', y1)
        errosY1 = self.encontraErros(x, y1)
        print('erros do y1 =', errosY1)
        y2 = self.calculaY(x, h2, self.variancia, self.media, n5)
        print('y2 =', y2)
        errosY2 = self.encontraErros(x, y2)
        print('erros do y2 =', errosY2)

        toStringY1 = ''.join(map(str, y1))

        if n5 == 7:
            tabela = ['0000000', '1101001', '0101010', '1000011', '1001100', '0100101', '1100110', '0001111',
                      '1110000', '0011001', '1011010', '0110011', '0111100', '1010101', '0010110', '1111111']
        elif n5 == 15:
            tabela = self.generate_hamming_codes_15_bits()
        elif n5 == 31:
            tabela = self.generate_space_amostral_sample_31_bits(self.ntestes)
        elif n5 == 63:
            tabela = self.generate_space_amostral_sample_63_bits(self.ntestes)
        elif n5 == 127:
            tabela = self.generate_space_amostral_sample_127_bits(self.ntestes)
        elif n5 == 255:
            tabela = self.generate_space_amostral_sample_255_bits(self.ntestes)

        P = self.encontraParidade(y1, tabela)
        chave = self.comparaSinais(y2, P, tabela)
        print("Chave gerada:", chave)

        contagemDeAcertos = 0
        for bit_chave, bit_y1 in zip(chave, toStringY1):
            if bit_chave == bit_y1:
                contagemDeAcertos += 1

        porcentagem_de_acertos = 100 * contagemDeAcertos / n5

        print(f"Porcentagem de vezes que a chave gerada foi encontrada na tabela: {porcentagem_de_acertos:.2f}%")

        self.plotar(x, y1, y2, len(x))

        return porcentagem_de_acertos