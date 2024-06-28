# gerador_aleatorio.py
import random

def gerar_tempo_entre_chegadas(taxa: float) -> float:
    """
    Gera o tempo entre chegadas de clientes baseado na taxa fornecida.
    
    Utiliza a distribuição exponencial para simular tempos entre chegadas,
    que é comum em modelos de filas.
    
    Args:
        taxa (float): Taxa de chegada (ex. 1/5 significa uma chegada a cada 5 minutos em média).
        
    Returns:
        float: Tempo até a próxima chegada.
    """
    return random.expovariate(taxa)

def gerar_tempo_atendimento(taxa: float) -> float:
    """
    Gera o tempo de atendimento baseado na taxa fornecida.
    
    Utiliza a distribuição exponencial para simular tempos de serviço.
    
    Args:
        taxa (float): Taxa de serviço (ex. 1/8 significa um atendimento a cada 8 minutos em média).
        
    Returns:
        float: Duração do atendimento.
    """
    return random.expovariate(taxa)
