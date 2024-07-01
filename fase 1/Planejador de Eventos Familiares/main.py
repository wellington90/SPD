# main.py
from datas import PlanejadorDatas
from tarefas import OrganizadorTarefas
from lembretes import GerenciadorLembretes
from datetime import datetime

def main():
    """
    Função principal que gerencia o planejamento do evento familiar.
    """
    # Planejamento de datas
    planejador_datas = PlanejadorDatas()
    planejador_datas.adicionar_disponibilidade("Alice", "2024-07-01")
    planejador_datas.adicionar_disponibilidade("Bob", "2024-07-02")
    planejador_datas.adicionar_disponibilidade("Charlie", "2024-07-01")
    data_ideal = planejador_datas.calcular_data_ideal()
    print(f"Data ideal para o evento: {data_ideal}")

    # Organização de tarefas
    organizador_tarefas = OrganizadorTarefas()
    organizador_tarefas.adicionar_tarefa("Comprar bebidas", "Alice")
    organizador_tarefas.adicionar_tarefa("Preparar comidas", "Bob")
    organizador_tarefas.adicionar_tarefa("Decoração", "Charlie")
    tarefas = organizador_tarefas.listar_tarefas()
    print("Tarefas organizadas:")
    for responsavel, lista_tarefas in tarefas.items():
        print(f"{responsavel}: {', '.join(lista_tarefas)}")

    # Gerenciamento de lembretes
    data_evento = data_ideal
    gerenciador_lembretes = GerenciadorLembretes(data_evento)
    gerenciador_lembretes.adicionar_lembrete("Lembrar de confirmar presença", 7)
    gerenciador_lembretes.adicionar_lembrete("Comprar os ingredientes", 3)
    gerenciador_lembretes.adicionar_lembrete("Checar decoração", 1)

    data_atual = "2024-06-28"
    lembretes_hoje = gerenciador_lembretes.verificar_lembretes(data_atual)
    if lembretes_hoje:
        print("Lembretes para hoje:")
        for lembrete in lembretes_hoje:
            print(f"  - {lembrete}")
    else:
        print("Nenhum lembrete para hoje.")

if __name__ == "__main__":
    main()
