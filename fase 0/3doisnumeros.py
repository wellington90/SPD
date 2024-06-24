
"""
Vamos resolver este problema de forma eficiente usando um mapa hash (dicionário em Python) para atingir uma complexidade de tempo de
𝑂(𝑛) Sobre​.

Plano:
1° Iterar pelo array nums.
2° Para cada elemento, calcule o valor do complemento necessário para atingir target(ou seja, complement = target - nums[i]).
3° Verifique se o complemento já está no mapa hash.
    - Se for, retorne os índices do elemento atual e do complemento.
    - Caso contrário, adicione o elemento atual e seu índice ao mapa hash.
"""


def two_sum(nums, target):
    """
    Retorna os índices dos dois números na lista nums que somam para o target.

    Args:
        nums (List[int]): Lista de inteiros.
        target (int): Valor alvo que a soma de dois elementos de nums deve alcançar.

    Returns:
        List[int]: Lista contendo os índices dos dois números que somam para o target.
    """
    # Cria um dicionário para armazenar os números e seus respectivos índices
    num_to_index = {}

    # Itera sobre a lista nums com seus índices
    for i, num in enumerate(nums):
        # Calcula o complemento necessário para atingir o target
        complement = target - num

        # Verifica se o complemento já está no dicionário
        if complement in num_to_index:
            # Se estiver, retorna os índices do número atual e do complemento
            return [num_to_index[complement], i]

        # Caso contrário, adiciona o número atual e seu índice ao dicionário
        num_to_index[num] = i

    # Se não encontrar uma solução (de acordo com o enunciado, sempre haverá uma solução)
    return []

# Exemplo de uso
nums1 = [2, 7, 11, 15]
target1 = 9
output1 = two_sum(nums1, target1)
print(f"Output: {output1}")  # Output esperado: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
output2 = two_sum(nums2, target2)
print(f"Output: {output2}")  # Output esperado: [1, 2]

nums3 = [3, 3]
target3 = 6
output3 = two_sum(nums3, target3)
print(f"Output: {output3}")  # Output esperado: [0, 1]



"""
Explicação do código:
Dicionário num_to_index: Armazena os números da lista como chaves e seus índices como valores.
Iteração com enumerate: Permite acessar tanto o índice quanto o valor de cada elemento da lista.
Cálculo do Complemento: Para cada elemento, calcula o valor que, somado ao elemento atual, iguala ao target.
Verificação no Dicionário: Se o complemento já estiver no dicionário, significa que encontramos os dois números cuja soma é igual ao target.
Atualização do Dicionário: Se o complemento não estiver no dicionário, adiciona o elemento atual e seu índice ao dicionário.
Vamos testar o código para garantir que ele está funcionando corretamente.

[python] Os resultados dos testes confirmam que a função two_sum está funcionando corretamente. Aqui estão os resultados detalhados:

Exemplo 1:
Entrada: nums = [2, 7, 11, 15], target = 9
Saída: [0, 1]
Explicação: nums[0] + nums[1] == 9, portanto retornamos [0, 1].

Exemplo 2:
Entrada: nums = [3, 2, 4], target = 6
Saída: [1, 2]
Explicação: nums[1] + nums[2] == 6, portanto retornamos [1, 2].

Exemplo 3:
Entrada: nums = [3, 3], target = 6
Saída: [0, 1]
Explicação: nums[0] + nums[1] == 6, portanto retornamos [0, 1].
"""