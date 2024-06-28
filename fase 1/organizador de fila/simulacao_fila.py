# simulacao_fila.py
from queue import Queue
from gerador_aleatorio import gerar_tempo_entre_chegadas, gerar_tempo_atendimento

class Cliente:
    """
    Representa um cliente na fila de atendimento.
    
    Atributos:
        tempo_chegada (float): Tempo de chegada do cliente.
        tempo_inicio_atendimento (float): Tempo em que o atendimento do cliente começa.
        tempo_fim_atendimento (float): Tempo em que o atendimento do cliente termina.
    """
    
    def __init__(self, tempo_chegada):
        self.tempo_chegada = tempo_chegada
        self.tempo_inicio_atendimento = None
        self.tempo_fim_atendimento = None

    def definir_tempo_atendimento(self, tempo_inicio, duracao_atendimento):
        """
        Define os tempos de início e fim do atendimento.
        
        Args:
            tempo_inicio (float): Tempo em que o atendimento começa.
            duracao_atendimento (float): Duração do atendimento.
        """
        self.tempo_inicio_atendimento = tempo_inicio
        self.tempo_fim_atendimento = tempo_inicio + duracao_atendimento

class SimulacaoFila:
    """
    Simula uma fila de atendimento, como em um banco ou supermercado.
    
    Atributos:
        taxa_chegada (float): Taxa média de chegada de clientes.
        taxa_atendimento (float): Taxa média de atendimento.
        tempo_simulacao (float): Tempo total da simulação.
        fila (Queue): Fila de clientes esperando atendimento.
        clientes (list): Lista de todos os clientes que chegaram durante a simulação.
        tempo_atual (float): Tempo atual na simulação.
        proxima_chegada (float): Tempo até a próxima chegada de cliente.
        proximo_fim_atendimento (float): Tempo até o próximo cliente terminar o atendimento.
        servidor_ocupado (bool): Indica se o servidor (atendente) está ocupado.
    """
    
    def __init__(self, taxa_chegada, taxa_atendimento, tempo_simulacao):
        self.taxa_chegada = taxa_chegada
        self.taxa_atendimento = taxa_atendimento
        self.tempo_simulacao = tempo_simulacao
        self.fila = Queue()
        self.clientes = []
        self.tempo_atual = 0
        self.proxima_chegada = gerar_tempo_entre_chegadas(taxa_chegada)
        self.proximo_fim_atendimento = float('inf')
        self.servidor_ocupado = False

    def executar(self):
        """Executa a simulação até que o tempo total seja alcançado."""
        while self.tempo_atual < self.tempo_simulacao or not self.fila.empty() or self.servidor_ocupado:
            if self.proxima_chegada < self.proximo_fim_atendimento and self.tempo_atual < self.tempo_simulacao:
                self.tempo_atual = self.proxima_chegada
                self.evento_chegada()
            else:
                self.tempo_atual = self.proximo_fim_atendimento
                self.evento_saida()

    def evento_chegada(self):
        """Processa um evento de chegada de cliente."""
        cliente = Cliente(self.tempo_atual)
        self.clientes.append(cliente)
        self.fila.put(cliente)
        self.proxima_chegada = self.tempo_atual + gerar_tempo_entre_chegadas(self.taxa_chegada)
        
        if not self.servidor_ocupado:
            self.iniciar_atendimento()

    def iniciar_atendimento(self):
        """Inicia o atendimento de um cliente da fila."""
        if not self.fila.empty():
            cliente = self.fila.get()
            self.servidor_ocupado = True
            duracao_atendimento = gerar_tempo_atendimento(self.taxa_atendimento)
            cliente.definir_tempo_atendimento(self.tempo_atual, duracao_atendimento)
            self.proximo_fim_atendimento = self.tempo_atual + duracao_atendimento

    def evento_saida(self):
        """Processa um evento de término de atendimento de cliente."""
        self.servidor_ocupado = False
        self.proximo_fim_atendimento = float('inf')
        if not self.fila.empty():
            self.iniciar_atendimento()
