# main.py
from simulacao_fila import SimulacaoFila
from estatisticas import calcular_estatisticas

def main():
    """
    Função principal que configura e executa a simulação de fila de atendimento,
    e imprime as estatísticas resultantes.
    """
    taxa_chegada = 1/5  # Média de 5 minutos entre chegadas
    taxa_atendimento = 1/8  # Média de 8 minutos para atendimento
    tempo_simulacao = 60 * 8  # Simulação de 8 horas

    # Cria e executa a simulação
    simulacao = SimulacaoFila(taxa_chegada, taxa_atendimento, tempo_simulacao)
    simulacao.executar()

    # Calcula estatísticas da simulação
    tempo_medio_espera, tempo_medio_sistema, ocupacao_servidor = calcular_estatisticas(simulacao.clientes)

    # Imprime os resultados
    print(f"Tempo médio de espera: {tempo_medio_espera:.2f} minutos")
    print(f"Tempo médio no sistema: {tempo_medio_sistema:.2f} minutos")
    print(f"Taxa de ocupação do servidor: {ocupacao_servidor:.2f}")

if __name__ == "__main__":
    main()
