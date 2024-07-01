# tarefas.py
from collections import defaultdict

class OrganizadorTarefas:
    """
    Classe que organiza tarefas entre os participantes do evento.

    Atributos:
        tarefas (dict): Dicionário com tarefas e seus responsáveis.
    """
    def __init__(self):
        self.tarefas = defaultdict(list)

    def adicionar_tarefa(self, tarefa, responsavel):
        """
        Adiciona uma tarefa a um participante.

        Args:
            tarefa (str): Descrição da tarefa.
            responsavel (str): Nome do responsável pela tarefa.
        """
        self.tarefas[responsavel].append(tarefa)

    def listar_tarefas(self):
        """
        Lista todas as tarefas e seus responsáveis.

        Returns:
            dict: Dicionário com tarefas e seus responsáveis.
        """
        return self.tarefas
