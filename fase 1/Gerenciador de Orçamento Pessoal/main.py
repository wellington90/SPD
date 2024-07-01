# main.py
from despesas import GerenciadorDespesas
from previsao import PrevisaoGastos
from analise import AnaliseEconomia

def main():
    """
    Função principal que gerencia o orçamento pessoal.
    """
    # Configuração inicial
    renda_mensal = 5000  # Renda mensal do usuário

    # Gerenciamento de despesas
    gerenciador_despesas = GerenciadorDespesas()
    gerenciador_despesas.adicionar_despesa("Aluguel", 1200, "Habitação")
    gerenciador_despesas.adicionar_despesa("Conta de Luz", 200, "Contas de Consumo")
    gerenciador_despesas.adicionar_despesa("Supermercado", 800, "Alimentação")
    total_despesas_mensais = gerenciador_despesas.calcular_despesas_mensais()
    print(f"Total das despesas mensais: R$ {total_despesas_mensais:.2f}")

    # Previsão de gastos futuros
    previsao_gastos = PrevisaoGastos()
    previsao_gastos.adicionar_gasto_passado("Habitação", 1200)
    previsao_gastos.adicionar_gasto_passado("Habitação", 1150)
    previsao_gastos.adicionar_gasto_passado("Contas de Consumo", 220)
    previsao_gastos.adicionar_gasto_passado("Contas de Consumo", 210)
    previsao_gastos.adicionar_gasto_passado("Alimentação", 750)
    previsao_gastos.adicionar_gasto_passado("Alimentação", 800)
    previsoes = previsao_gastos.prever_gastos_futuros()
    print("Previsão de gastos futuros:")
    for categoria, valor in previsoes.items():
        print(f"  {categoria}: R$ {valor:.2f}")

    # Análise de economia
    analise_economia = AnaliseEconomia(renda_mensal, total_despesas_mensais, previsoes)
    economia_mensal = analise_economia.calcular_economia()
    dicas_economia = analise_economia.sugerir_dicas_economia()
    print(f"Economia mensal: R$ {economia_mensal:.2f}")
    if dicas_economia:
        print("Dicas de economia:")
        for dica in dicas_economia:
            print(f"  - {dica}")

if __name__ == "__main__":
    main()
