"""
Vamos resolver esse problema passo a passo. Criaremos uma função removeElement 
que modificará o array no local para remover todas as instâncias vale retornar o número de elementos que não são iguais a val. Aqui está o plano:

1° Itere sobre o array com um ponteiro i.
2° Use outro ponteiro kpara rastrear a posição dos elementos diferentes de val.
3° Se um elemento não for igual a val, coloque-o na k-ésima posição e aumente k.
4° Por fim, return kque representa o número de elementos do array que não são iguais a val.
"""


def removeElement(nums, val):
    """
    Remove todas as ocorrências de val na lista nums in-place.
    Retorna o número de elementos em nums que não são iguais a val.

    Args:
        nums (List[int]): Lista de inteiros.
        val (int): Valor a ser removido da lista.

    Returns:
        int: Número de elementos em nums que não são iguais a val.
    """
    # Inicializa o ponteiro k que irá rastrear a posição dos elementos que não são iguais a val
    k = 0

    # Itera sobre cada elemento da lista nums
    for i in range(len(nums)):
        # Se o elemento nums[i] não for igual a val
        if nums[i] != val:
            # Coloca o elemento na posição k
            nums[k] = nums[i]
            # Incrementa o ponteiro k
            k += 1

    # Retorna o número de elementos que não são iguais a val
    return k

# Exemplo de uso
nums1 = [3, 2, 2, 3]
val1 = 3
k1 = removeElement(nums1, val1)
print(f"Output: {k1}, nums = {nums1[:k1]}")  # Output esperado: 2, nums = [2, 2]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
k2 = removeElement(nums2, val2)
print(f"Output: {k2}, nums = {nums2[:k2]}")  # Output esperado: 5, nums = [0, 1, 3, 0, 4]



"""
    Explicação do código
Docstring: Descreve o propósito da função e seus argumentos.
Ponteiro k: Inicializa um ponteiro para rastrear a posição dos elementos que não são iguais a val.
Laço for: Itera sobre cada elemento da lista nums.
Verificação: Se o elemento atual não é igual a val, ele é movido para a posição k, e k é incrementado.
Retorno: A função retorna o valor de k, que é o número de elementos em nums que não são iguais a val.
Vamos testar o código para garantir que está funcionando corretamente.

[python] Os resultados dos testes mostram que a função está funcionando conforme esperado. Aqui estão os resultados detalhados:

Exemplo 1:

Entrada: nums = [3, 2, 2, 3], val = 3
Saída: k = 2, nums = [2, 2, _, _]
Explicação: A função retorna k = 2, com os dois primeiros elementos de nums sendo 2.
Exemplo 2:

Entrada: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
Saída: k = 5, nums = [0, 1, 3, 0, 4, _, _, _]
Explicação: A função retorna k = 5, com os primeiros cinco elementos de nums sendo 0, 1, 3, 0, 4.
Isso confirma que a função está removendo todas as ocorrências de val e retornando o número correto de elementos restantes.
"""