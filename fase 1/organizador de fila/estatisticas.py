# estatisticas.py
def calcular_estatisticas(clientes):
    """
    Calcula as estatísticas da simulação.

    Args:
        clientes (list): Lista de objetos Cliente que passaram pela simulação.

    Returns:
        tuple: Contendo tempo médio de espera, tempo médio no sistema e taxa de ocupação do servidor.
    """
    total_tempo_espera = 0
    total_tempo_sistema = 0
    total_tempo_servico = 0
    clientes_atendidos = [c for c in clientes if c.tempo_inicio_atendimento is not None]

    for cliente in clientes_atendidos:
        tempo_espera = cliente.tempo_inicio_atendimento - cliente.tempo_chegada
        tempo_sistema = cliente.tempo_fim_atendimento - cliente.tempo_chegada
        tempo_servico = cliente.tempo_fim_atendimento - cliente.tempo_inicio_atendimento

        total_tempo_espera += tempo_espera
        total_tempo_sistema += tempo_sistema
        total_tempo_servico += tempo_servico

    num_clientes = len(clientes_atendidos)
    tempo_medio_espera = total_tempo_espera / num_clientes if num_clientes > 0 else 0
    tempo_medio_sistema = total_tempo_sistema / num_clientes if num_clientes > 0 else 0
    tempo_total_simulacao = clientes_atendidos[-1].tempo_fim_atendimento if clientes_atendidos else 1
    ocupacao_servidor = total_tempo_servico / tempo_total_simulacao

    return tempo_medio_espera, tempo_medio_sistema, ocupacao_servidor
