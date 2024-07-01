# despesas.py
class Despesa:
    """
    Classe que representa uma despesa recorrente.

    Atributos:
        nome (str): Nome da despesa.
        valor (float): Valor da despesa.
        categoria (str): Categoria da despesa.
    """
    def __init__(self, nome, valor, categoria):
        self.nome = nome
        self.valor = valor
        self.categoria = categoria

class GerenciadorDespesas:
    """
    Classe que gerencia as despesas recorrentes.

    Atributos:
        despesas (list): Lista de objetos Despesa.
    """
    def __init__(self):
        self.despesas = []

    def adicionar_despesa(self, nome, valor, categoria):
        """
        Adiciona uma nova despesa à lista de despesas.

        Args:
            nome (str): Nome da despesa.
            valor (float): Valor da despesa.
            categoria (str): Categoria da despesa.
        """
        despesa = Despesa(nome, valor, categoria)
        self.despesas.append(despesa)

    def calcular_despesas_mensais(self):
        """
        Calcula o total das despesas mensais.

        Returns:
            float: Total das despesas mensais.
        """
        return sum(despesa.valor for despesa in self.despesas)
