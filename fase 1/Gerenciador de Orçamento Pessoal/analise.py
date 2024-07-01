# analise.py
class AnaliseEconomia:
    """
    Classe que faz a análise de economia e sugere dicas.

    Atributos:
        renda_mensal (float): Renda mensal do usuário.
        despesas_mensais (float): Total das despesas mensais.
        previsao_gastos (dict): Previsão de gastos futuros por categoria.
    """
    def __init__(self, renda_mensal, despesas_mensais, previsao_gastos):
        self.renda_mensal = renda_mensal
        self.despesas_mensais = despesas_mensais
        self.previsao_gastos = previsao_gastos

    def calcular_economia(self):
        """
        Calcula a economia mensal.

        Returns:
            float: Valor economizado no mês.
        """
        return self.renda_mensal - self.despesas_mensais

    def sugerir_dicas_economia(self):
        """
        Sugere dicas de economia com base nos hábitos de consumo.

        Returns:
            list: Lista de dicas de economia.
        """
        dicas = []
        for categoria, valor in self.previsao_gastos.items():
            if valor > 0.2 * self.renda_mensal:  # Se uma categoria representa mais de 20% da renda
                dicas.append(f"Tente reduzir seus gastos com {categoria}.")
        return dicas
