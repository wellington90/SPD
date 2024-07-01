# lembretes.py
from datetime import datetime, timedelta

class GerenciadorLembretes:
    """
    Classe que gerencia os lembretes de eventos.

    Atributos:
        data_evento (date): Data do evento.
        lembretes (list): Lista de lembretes a serem enviados.
    """
    def __init__(self, data_evento):
        self.data_evento = datetime.strptime(data_evento, '%Y-%m-%d').date()
        self.lembretes = []

    def adicionar_lembrete(self, mensagem, dias_antes):
        """
        Adiciona um lembrete para o evento.

        Args:
            mensagem (str): Mensagem do lembrete.
            dias_antes (int): Número de dias antes do evento para enviar o lembrete.
        """
        data_lembrete = self.data_evento - timedelta(days=dias_antes)
        self.lembretes.append((data_lembrete, mensagem))

    def verificar_lembretes(self, data_atual):
        """
        Verifica se há lembretes para enviar na data atual.

        Args:
            data_atual (str): Data atual no formato 'YYYY-MM-DD'.

        Returns:
            list: Lista de mensagens de lembrete para a data atual.
        """
        data_atual = datetime.strptime(data_atual, '%Y-%m-%d').date()
        lembretes_hoje = [mensagem for data_lembrete, mensagem in self.lembretes if data_lembrete == data_atual]
        return lembretes_hoje
