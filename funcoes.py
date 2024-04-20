import tokens as tk

def gravar_somatorio():
    """
    Grava o somatório dos tokens em um arquivo chamado "Total_de_tokens.txt".
    
    Essa função cria um arquivo chamado "Total_de_tokens.txt" e grava o somatório dos tokens nele.
    O arquivo terá um formato de tabela com duas colunas: "TOKENS" e "TOTAL".
    """
    with open("Total_de_tokens.txt", 'w') as arquivo:
        arquivo.write('+------------------------------+----------+\n' + 
                      f'|{"TOKENS":^30}|{"TOTAL":^10}|\n' + 
                      '+------------------------------+----------+\n'
        )
        for nome_token, valor in tk.tokens.items():
            arquivo.write(f'|{nome_token:<30}|{valor:<10}|\n')
            arquivo.write('+------------------------------+----------+\n')

def gravar_lexema(linha: int, coluna: int, token_tipo: str, lexema: str = ''):
    """
    Grava um lexema no formato de uma linha de tabela.

    Args:
        linha (int): O número da linha onde o lexema foi encontrado.
        coluna (int): O número da coluna onde o lexema começa.
        token_tipo (str): O tipo de token do lexema.
        lexema (str): O lexema em si.

    Returns:
        str: A linha formatada contendo as informações do lexema.
    """
    return f'\n|{linha:<5}|{coluna:<5}|{token_tipo:<20}|{lexema:<20}|\n' + \
    '''+-----+-----+--------------------+--------------------+'''
