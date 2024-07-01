# datas.py
from collections import defaultdict
from datetime import datetime, timedelta

class PlanejadorDatas:
    """
    Classe que planeja datas ideais para eventos com base na disponibilidade dos participantes.

    Atributos:
        disponibilidades (dict): Dicionário com disponibilidades dos participantes.
    """
    def __init__(self):
        self.disponibilidades = defaultdict(list)

    def adicionar_disponibilidade(self, participante, data_disponivel):
        """
        Adiciona uma data disponível para um participante.

        Args:
            participante (str): Nome do participante.
            data_disponivel (str): Data disponível no formato 'YYYY-MM-DD'.
        """
        data = datetime.strptime(data_disponivel, '%Y-%m-%d').date()
        self.disponibilidades[participante].append(data)

    def calcular_data_ideal(self):
        """
        Calcula a data ideal para o evento com base nas disponibilidades dos participantes.

        Returns:
            str: Data ideal no formato 'YYYY-MM-DD' ou mensagem indicando impossibilidade.
        """
        contador_datas = defaultdict(int)
        for datas in self.disponibilidades.values():
            for data in datas:
                contador_datas[data] += 1
        
        if not contador_datas:
            return "Nenhuma data disponível foi informada."
        
        data_ideal = max(contador_datas, key=contador_datas.get)
        return data_ideal.strftime('%Y-%m-%d')
