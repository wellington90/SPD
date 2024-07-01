 Para criar um Gerenciador de Orçamento Pessoal, vamos desenvolver um programa que inclua:

1° Registro e cálculo de despesas mensais fixas.
2° Previsão de gastos futuros com base em médias de gastos passados.
3° Análise de economia com sugestões de dicas de economia.
4° Vamos organizar o código em módulos para facilitar a manutenção e a compreensão.

Estrutura do Projeto
1° main.py - Script principal para rodar o gerenciador de orçamento.
2° despesas.py - Módulo para registrar e calcular despesas mensais fixas.
3° previsao.py - Módulo para prever gastos futuros com base em médias de gastos passados.
4° analise.py - Módulo para analisar a economia e sugerir dicas.



Explicação do Código
despesas.py
Classe Despesa:

Representa uma despesa recorrente com atributos nome, valor e categoria.
Classe GerenciadorDespesas:

Gerencia uma lista de despesas.
Método adicionar_despesa: Adiciona uma nova despesa à lista.
Método calcular_despesas_mensais: Calcula o total das despesas mensais somando os valores de todas as despesas na lista.
previsao.py
Classe PrevisaoGastos:
Armazena o histórico de gastos por categoria.
Método adicionar_gasto_passado: Adiciona um gasto passado ao histórico.
Método prever_gastos_futuros: Preve os gastos futuros calculando a média dos gastos passados por categoria.
analise.py
Classe AnaliseEconomia:
Analisa a economia mensal e sugere dicas de economia.
Método calcular_economia: Calcula a economia mensal subtraindo as despesas da renda mensal.
Método sugerir_dicas_economia: Sugere dicas de economia se alguma categoria de gasto for muito alta em relação à renda mensal.
main.py
Função main:
Define a renda mensal do usuário.
Cria uma instância de GerenciadorDespesas e adiciona despesas.
Calcula o total das despesas mensais e imprime.
Cria uma instância de PrevisaoGastos, adiciona gastos passados e calcula previsões futuras, imprimindo os resultados.
Cria uma instância de AnaliseEconomia, calcula a economia mensal e imprime sugestões de economia.