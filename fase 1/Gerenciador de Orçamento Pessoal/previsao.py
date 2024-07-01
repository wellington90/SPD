# previsao.py
class PrevisaoGastos:
    """
    Classe que faz a previsão de gastos futuros com base em médias passadas.

    Atributos:
        historico_gastos (dict): Dicionário com histórico de gastos por categoria.
    """
    def __init__(self):
        self.historico_gastos = {}

    def adicionar_gasto_passado(self, categoria, valor):
        """
        Adiciona um gasto passado ao histórico de gastos.

        Args:
            categoria (str): Categoria do gasto.
            valor (float): Valor do gasto.
        """
        if categoria not in self.historico_gastos:
            self.historico_gastos[categoria] = []
        self.historico_gastos[categoria].append(valor)

    def prever_gastos_futuros(self):
        """
        Preve os gastos futuros com base na média dos gastos passados.

        Returns:
            dict: Dicionário com previsão de gastos futuros por categoria.
        """
        previsao = {}
        for categoria, gastos in self.historico_gastos.items():
            previsao[categoria] = sum(gastos) / len(gastos) if gastos else 0
        return previsao
