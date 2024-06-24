"""
Vamos implementar a função que converte um numeral romano em um número inteiro, seguindo as regras descritas.

Passos:
1° Crie um dicionário para mapear os símbolos romanos aos seus valores inteiros.
2° Inicialize uma variável para armazenar o resultado.
3° Percorra a string do numeral romano.
4° Para cada caractere, verifique se o valor atual é menor que o próximo valor:
   - Se for, subtraia o valor atual do resultado.
   - Caso contrário, adicione o valor atual ao resultado.
5° Retorne o resultado.
"""


def romanToInt(s):
    """
    Converte um numeral romano em um número inteiro.

    Parâmetros:
    s (str): O numeral romano representado como uma string.

    Retorna:
    int: O valor inteiro correspondente ao numeral romano.
    
    Exemplo:
    >>> romanToInt("III")
    3
    >>> romanToInt("LVIII")
    58
    >>> romanToInt("MCMXCIV")
    1994
    """
    # Dicionário que mapeia os símbolos romanos aos seus valores inteiros
    valores_romanos = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    # Inicializa a variável que armazenará o resultado
    resultado = 0
    
    # Percorre cada caractere na string do numeral romano
    for i in range(len(s)):
        # Se o valor do símbolo atual é menor que o do próximo símbolo,
        # subtrai o valor atual do resultado (caso de subtração)
        if i + 1 < len(s) and valores_romanos[s[i]] < valores_romanos[s[i + 1]]:
            resultado -= valores_romanos[s[i]]
        else:
            # Caso contrário, adiciona o valor atual ao resultado
            resultado += valores_romanos[s[i]]
    
    return resultado

# Exemplos de uso:
print(romanToInt("III"))       # Saída: 3
print(romanToInt("LVIII"))     # Saída: 58
print(romanToInt("MCMXCIV"))   # Saída: 1994


"""
Explicação das Funções
1° Dicionário valores_romanos: Mapeia cada símbolo romano ao seu valor inteiro correspondente.
2° Iteração com for: Percorre cada caractere da string s.
3° Verificação de Subtração: Se o valor do símbolo atual for menor que o valor do próximo símbolo, subtrai esse valor do resultado. Caso contrário, adiciona o valor ao resultado.
4° Retorno do Resultado: Após percorrer toda a string, o resultado é retornado.

"""
