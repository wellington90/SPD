# Explicação do Código

## gerador_aleatorio.py
Este módulo contém funções para gerar tempos aleatórios utilizando a distribuição exponencial, comum em modelos de filas para simular tempos entre chegadas e tempos de atendimento.

gerar_tempo_entre_chegadas(taxa: float) -> float:
Gera o tempo entre a chegada de clientes baseado na taxa fornecida.
Utiliza random.expovariate para gerar um número aleatório conforme a distribuição exponencial.
A taxa (rate) representa a frequência de chegadas, por exemplo, 1/5 significa uma chegada a cada 5 minutos em média.
gerar_tempo_atendimento(taxa: float) -> float:
Gera o tempo de atendimento baseado na taxa fornecida.
Também utiliza random.expovariate.
A taxa representa a frequência de atendimento, por exemplo, 1/8 significa um atendimento a cada 8 minutos em média.

## simulacao_fila.py
Este módulo define as classes e métodos para simular a fila de atendimento.
Classe Cliente:
Representa um cliente na fila de atendimento.
Atributos:
tempo_chegada: Tempo de chegada do cliente.
tempo_inicio_atendimento: Tempo em que o atendimento do cliente começa.
tempo_fim_atendimento: Tempo em que o atendimento do cliente termina.
Método definir_tempo_atendimento(self, tempo_inicio, duracao_atendimento):
Define os tempos de início e fim do atendimento do cliente.
Classe SimulacaoFila:
Simula uma fila de atendimento, como em um banco ou supermercado.
Atributos:
taxa_chegada: Taxa média de chegada de clientes.
taxa_atendimento: Taxa média de atendimento.
tempo_simulacao: Tempo total da simulação.
fila: Fila de clientes esperando atendimento.
clientes: Lista de todos os clientes que chegaram durante a simulação.
tempo_atual: Tempo atual na simulação.
proxima_chegada: Tempo até a próxima chegada de cliente.
proximo_fim_atendimento: Tempo até o próximo cliente terminar o atendimento.
servidor_ocupado: Indica se o servidor (atendente) está ocupado.
Método executar(self):
Executa a simulação até que o tempo total seja alcançado.
Alterna entre eventos de chegada e eventos de saída (fim de atendimento).
Método evento_chegada(self):
Processa um evento de chegada de cliente.
Cria um novo cliente, adiciona à lista de clientes e à fila, e agenda a próxima chegada.
Inicia o atendimento se o servidor não estiver ocupado.
Método iniciar_atendimento(self):
Inicia o atendimento de um cliente da fila.
Define os tempos de início e fim do atendimento e agenda o próximo fim de atendimento.
Método evento_saida(self):
Processa um evento de término de atendimento de cliente.
Libera o servidor e agenda o próximo atendimento se houver clientes na fila.

## estatisticas.py
Este módulo contém a função para calcular as estatísticas da simulação.
Função calcular_estatisticas(clientes):
Calcula o tempo médio de espera, tempo médio no sistema e a taxa de ocupação do servidor a partir da lista de clientes.
Filtra os clientes atendidos (aqueles cujo tempo_inicio_atendimento não é None).
Calcula o tempo de espera (diferença entre tempo_inicio_atendimento e tempo_chegada), tempo no sistema (diferença entre tempo_fim_atendimento e tempo_chegada), e tempo de serviço (diferença entre tempo_fim_atendimento e tempo_inicio_atendimento).
Soma esses tempos para todos os clientes atendidos.
Calcula as médias dos tempos de espera e no sistema.
Calcula a taxa de ocupação do servidor como a proporção do tempo total de serviço sobre o tempo total da simulação.

## main.py
Este é o script principal que configura e executa a simulação e imprime as estatísticas resultantes.

Função main():

Define a taxa de chegada (taxa_chegada) e a taxa de atendimento (taxa_atendimento), bem como o tempo total de simulação (tempo_simulacao).
Cria e executa a simulação usando a classe SimulacaoFila.
Calcula as estatísticas da simulação usando a função calcular_estatisticas.
Imprime os resultados das estatísticas: tempo médio de espera, tempo médio no sistema e taxa de ocupação do servidor.
Garante que a função main() seja executada apenas quando o script é executado diretamente, e não quando é importado como um módulo em outro script.