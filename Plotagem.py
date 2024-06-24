from matplotlib import pyplot as plt
from np.magic import np


class Plotagem:
    def __init__(self):
        pass

    def plota_diferencas(self, x, y1, y2, tam):
        fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (15, 10))

        indices = range(tam)  # Cria uma lista de índices de 0 a tam-1

        axes[0].plot(indices, x, 'r--', label='X')
        axes[0].plot(indices, y1, 'b', label='Y1')
        axes[0].set_title('Y1')
        axes[0].set_xlabel('Índice do Bit')
        axes[0].set_ylabel('Valor do Bit')
        axes[0].legend()

        axes[1].plot(indices, x, 'r--', label='X')
        axes[1].plot(indices, y2, 'b', label='Y2')
        axes[1].set_title('Y2')
        axes[1].set_xlabel('Índice do Bit')
        axes[1].set_ylabel('Valor do Bit')
        axes[1].legend()

        plt.tight_layout()
        plt.show()

    def fixPlot(self, aux):
        y = []
        for i in range(len(aux)):
            for k in range(100):
                y.append(aux[i])
        return y

    def plotar(self, x, y1, y2, tam):
        x = self.fixPlot(x)
        y1 = self.fixPlot(y1)
        y2 = self.fixPlot(y2)
        self.plota_diferencas(x, y1, y2, tam * 100)


    def plota_resultados(self, porcentagens):
        cenarios = [f'Cenário {i+1}' for i in range(len(porcentagens))]
        fig, ax = plt.subplots(figsize=(10, 6))

        ax.bar(cenarios, porcentagens, color='blue')

        ax.set_xlabel('Cenários')
        ax.set_ylabel('Porcentagem de Estabelecimento de Chave')
        ax.set_title('Porcentagem de Estabelecimento de Chave em Cada Cenário')

        plt.show()

