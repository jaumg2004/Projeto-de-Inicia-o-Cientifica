from CenárioBase import CenárioBase
from Plotagem import Plotagem
from Hamming import HammingCodeGenerator

class RuidoNuloCanalUnitario(CenárioBase, Plotagem, HammingCodeGenerator):
    def calculaY(self, x, testes):
        y = [x[i] for i in range(testes)]
        return [1 if y[i] > 0.5 else 0 for i in range(testes)]