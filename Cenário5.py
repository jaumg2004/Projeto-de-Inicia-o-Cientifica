import random

from CenárioBase import CenárioBase
from Plotagem import Plotagem
from Hamming import HammingCodeGenerator

class AltoRuidoCanalRayleigh(CenárioBase, Plotagem, HammingCodeGenerator):
    def calculaY(self, h, x, variancia, media, ntestes):
        # Função para gerar ruído com distribuição normal
        def geraRuido(variancia, media, ntestes):
            return [random.gauss(media, variancia + 1.3) for _ in range(ntestes)]

        n = geraRuido(variancia, media, ntestes)
        y = [h[i] * x[i] + n[i] for i in range(ntestes)]
        return [1 if y[i] > 0.5 else 0 for i in range(ntestes)]