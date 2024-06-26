import funcoes as f
import tokens as tk

if __name__ == "__main__":
    """
    Este script realiza análise léxica em um arquivo fornecido.
    Ele lê caracteres do arquivo e identifica tokens com base em regras predefinidas.
    Os tokens identificados são então escritos em um arquivo de texto.
    """

    # Abre o arquivo para escrever a lista de tokens
    tk_lista = open("Lista_de_tokens.txt", 'w', encoding='utf-8')
    tk_lista.write('+-----+-----+--------------------+--------------------+\n' +
                   f'|{"LIN":^5}|{"COL":^5}|{"TOKEN":^20}|{"LEXEMA":^20}|\n' +
                   '+-----+-----+--------------------+--------------------+'
                   ) 
    
    # Define os nomes dos arquivos de entrada e de erro
    arquivo = "ex1"
    arquivo_erros = arquivo + "_erro"

    # Gera as extensões dos arquivos
    arquivo = f.gerador_extensao(arquivo, "cic")
    arquivo_erros = f.gerador_extensao(arquivo_erros, "txt")

    # Inicializa as variáveis
    token_tipo = ""
    lexema = ""
    msg_erro = ""
    posicao_atual = 0
    linha = 0
    coluna = 0
    estado = 0

    # Adiciona um marcador de fim de arquivo ao arquivo de entrada
    with open(arquivo, 'a') as arquivo_novo:
        arquivo_novo.write("$")

    # Abre o arquivo de entrada e o arquivo de erro
    with open(arquivo, 'r') as arquivo, open(arquivo_erros, 'w') as arquivo_erros:
        linhas = arquivo.readlines()
        token_anterior = None
        for indice_linha in range(len(linhas)):
            linha += 1
            coluna = 0
            linha_atual = linhas[indice_linha]
            arquivo_erros.write(f"[{indice_linha+1}]{linha_atual}")
            indice_caractere = 0
            
            while indice_caractere < len(linha_atual):
                token = linha_atual[indice_caractere]
                coluna +=1

                if not token:
                    print("Fim do arquivo")
                    break
        
                match estado:
                    case 0: #0 -> [1,19,23,24,25,26,27,28,29,30,31,32,33,43,45,48,58,64,68,85] 
                        if token in tk.TOKEN_NUM:
                            estado = 1
                            lexema += token
                        elif token in tk.TOKEN_ALFABETO_MIN:
                            estado = 19
                            lexema += token
                        elif token == ":":
                            estado = 23
                        elif token == ")":
                            estado = 24
                        elif token == "(":
                            estado = 25
                        elif token == "-":
                            estado = 26
                        elif token == "~":
                            estado = 27
                        elif token == "+":
                            estado = 28
                        elif token == "*":
                            estado = 29
                        elif token == "%":
                            estado = 30
                        elif token == "&":
                            estado = 31
                        elif token == "|":
                            estado = 32
                        elif token == "<":
                            estado = 33
                        elif token == '"':
                            estado = 43
                        elif token == ">":
                            estado = 45
                        elif token == "=":
                            estado = 48
                        elif token in tk.TOKEN_HEXA:
                            estado = 58
                            lexema += token
                        elif token == "#":
                            estado = 64
                        elif token == " " or token == "\n" or token == "\t":
                            pass
                        elif token == ".":
                            estado = 68
                        elif token == "$":
                            print("Fim do arquivo")
                            break
                        else:
                            msg_erro = f"Erro linha {linha}, coluna {coluna}: caractere '{token}' inválido."
                            estado = 85
                    case 1: #1 -> [2,51,59,75]
                        if token == ".":
                            estado = 51
                            lexema  += token
                        elif token in tk.TOKEN_NUM:
                            estado = 2
                            lexema += token
                        elif token == "x":
                            estado = 59
                            lexema += token
                        else:
                            estado = 75
                            indice_caractere -= 1
                            coluna -=1
                    case 2: #2 -> [3,4,49,51,75]
                        if token in tk.TOKEN_NUM:
                            estado = 49
                            lexema += token
                        elif token == "/":
                            estado = 3
                            lexema += token
                        elif token == ".":
                            estado = 51
                            lexema += token
                        elif token == "_":
                            estado = 4
                            lexema += token
                        else:
                            estado = 75
                    case 3: #3 -> [5,85]
                        if token in tk.TOKEN_NUM:
                            estado = 5
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: data mal formatada {lexema}"
                            indice_caractere -= 1
                            coluna -=1
                    case 4: #4 -> [6,85]
                        if token in tk.TOKEN_NUM:
                            estado = 6
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: data mal formatada {lexema}"
                            indice_caractere -= 1
                            coluna -=1
                    case 5: #5 -> [8,85]
                        if token in tk.TOKEN_NUM:
                            estado = 8
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: data mal formatada {lexema}"
                    case 6: #6 -> [7,85]
                        if token in tk.TOKEN_NUM:
                            estado = 7
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: data mal formatada {lexema}"
                    case 7: #7 -> [10,85]
                        if token == "_":
                            estado = 10
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: data mal formatada {lexema}"
                    case 8: #8 -> [9,85]
                        if token == "/":
                            estado = 9
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: data mal formatada {lexema}"
                    case 9: #9 -> [11,85]
                        if token in tk.TOKEN_NUM:
                            estado = 11
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: data mal formatada {lexema}"
                    case 10: #10 -> [15,85]
                        if token in tk.TOKEN_NUM:
                            estado = 15
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: data mal formatada {lexema}"
                    case 11: #11 -> [12,85]
                        if token in tk.TOKEN_NUM:
                            estado = 12
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: data mal formatada {lexema}"
                    case 12: #12 -> [13,85]
                        if token in tk.TOKEN_NUM:
                            estado = 13
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: data mal formatada {lexema}"
                    case 13: #13 -> [14,85]
                        if token in tk.TOKEN_NUM:
                            estado = 14
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: data mal formatada {lexema}"
                    case 14: #data
                        token_tipo = "TK_DATA"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo, lexema))
                        tk.tokens["TK_DATA"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        lexema = ""
                        indice_caractere -= 1
                        coluna -=1
                    case 15: #15 -> [16,85]
                        if token in tk.TOKEN_NUM:
                            estado = 16
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: data mal formatada {lexema}"
                            indice_caractere -= 1
                            coluna -=1
                    case 16: #16 -> [17,85]
                        if token in tk.TOKEN_NUM:
                            estado = 17
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: data mal formatada {lexema}"
                            indice_caractere -= 1
                            coluna -=1
                    case 17: #17 -> [18,85]
                        if token in tk.TOKEN_NUM:
                            estado = 18
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: data mal formatada {lexema}"
                    case 18: #data
                        token_tipo = "TK_DATA"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo, lexema))
                        tk.tokens["TK_DATA"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        lexema = ""
                        indice_caractere -= 1
                        coluna -=1
                    case 19: #19 -> [20,37,85]
                        if token in tk.TOKEN_ALFABETO_MAX:
                            estado = 20
                            lexema += token
                        elif token in tk.TOKEN_ALFABETO_MIN:
                            estado = 37
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}"
                            indice_caractere -= 1
                            coluna -=1
                    case 20: #20 -> [21,22]
                        if token in tk.TOKEN_ALFABETO_MIN:
                            estado = 21
                            lexema += token
                        else:
                            estado = 22
                            indice_caractere -= 1
                            coluna -=1
                    case 21: #21 -> [20,22]
                        if token in tk.TOKEN_ALFABETO_MAX:
                            estado = 20
                            lexema += token
                        else:
                            estado = 22
                            indice_caractere -= 1
                            coluna -=1
                    case 22: #identificador
                        token_tipo = "TK_ID"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo, lexema))
                        tk.tokens["TK_ID"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        lexema = ""
                        indice_caractere -= 1
                        coluna -=1
                    case 23: #dois pontos
                        token_tipo = "TK_DOIS_PONTOS"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_DOIS_PONTOS"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 24: #fecha parenteses
                        token_tipo = "TK_FEC_PARENTESES"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_FEC_PARENTESES"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 25: #abre parenteses
                        token_tipo = "TK_ABR_PARENTESES"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_ABR_PARENTESES"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 26: #menos
                        token_tipo = "TK_MENOS"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_MENOS"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 27: #negacao
                        token_tipo = "TK_NEGACAO"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_NEGACAO"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 28: #mais
                        token_tipo = "TK_MAIS"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_MAIS"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 29: #multiplicacao
                        token_tipo = "TK_MULTIPLICACAO"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_MULTIPLICACAO"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 30: #divisao
                        token_tipo = "TK_DIVISAO"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_DIVISAO"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 31: #and
                        token_tipo = "TK_AND"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_AND"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 32: #or
                        token_tipo = "TK_OR"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_OR"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 33: #33 -> [34,35,36,62]
                        if token == ">":
                            estado = 34
                        elif token == "=":
                            estado = 36
                        elif token == "<":
                            estado = 62
                        else:
                            estado = 35
                            indice_caractere -= 1
                            coluna -=1
                    case 34: #diferente
                        token_tipo = "TK_DIFERENTE"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_DIFERENTE"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 35: #menor que
                        token_tipo = "TK_MENOR_QUE"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_MENOR_QUE"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 36: #36 -> [38,39]
                        if token == "=":
                            estado = 39
                        else:
                            estado = 38
                            indice_caractere -= 1
                            coluna -=1
                    case 37: #37 -> [37,42]
                        if token in tk.TOKEN_ALFABETO_MIN + "_":
                            estado = 37
                            lexema += token
                        else:
                            estado = 42
                            indice_caractere -= 1
                            coluna -=1
                    case 38: #menor igual
                        token_tipo = "TK_MENOR_IGUAL"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_MENOR_IGUAL"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 39: #atribuicao
                        token_tipo = "TK_ATRIBUICAO"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_ATRIBUICAO"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 40: #igual
                        token_tipo = "TK_IGUAL"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_IGUAL"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 42: #palavras reservadas
                        if lexema == tk.tk_rotina:
                            token_tipo = "TK_ROTINA"
                            tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                            tk.tokens["TK_ROTINA"] += 1
                            tk.tokens["TK_TOTAL"] += 1
                            estado = 0
                        elif lexema == tk.tk_fim_rotina:
                            token_tipo = "TK_FIM_ROTINA"
                            tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                            tk.tokens["TK_FIM_ROTINA"] += 1
                            tk.tokens["TK_TOTAL"] += 1
                            estado = 0
                        elif lexema == tk.tk_se:
                            token_tipo = "TK_SE"
                            tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                            tk.tokens["TK_SE"] += 1
                            tk.tokens["TK_TOTAL"] += 1
                            estado = 0
                        elif lexema == tk.tk_senao:
                            token_tipo = "TK_SENAO"
                            tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                            tk.tokens["TK_SENAO"] += 1
                            tk.tokens["TK_TOTAL"] += 1
                            estado = 0
                        elif lexema == tk.tk_imprima:
                            token_tipo = "TK_IMPRIMA"
                            tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                            tk.tokens["TK_IMPRIMA"] += 1
                            tk.tokens["TK_TOTAL"] += 1
                            estado = 0
                        elif lexema == tk.tk_leia:
                            token_tipo = "TK_LEIA"
                            tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                            tk.tokens["TK_LEIA"] += 1
                            tk.tokens["TK_TOTAL"] += 1
                            estado = 0
                        elif lexema == tk.tk_para:
                            token_tipo = "TK_PARA"
                            tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                            tk.tokens["TK_PARA"] += 1
                            tk.tokens["TK_TOTAL"] += 1
                            estado = 0
                        elif lexema == tk.tk_enquanto:
                            token_tipo = "TK_ENQUANTO"
                            tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                            tk.tokens["TK_ENQUANTO"] += 1
                            tk.tokens["TK_TOTAL"] += 1
                            estado = 0
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: palavra reservada inválida {lexema}"
                        
                        lexema = ""
                        indice_caractere -= 1
                        coluna -=1
                    case 43: #43 -> [43,44,85]
                        if token == '"':
                            estado = 44
                        elif token == "\n":
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: cadeia inválida"
                            indice_caractere -= 1
                            coluna -=1
                        else:
                            estado = 43
                            lexema += token
                    case 44: #cadeia
                        token_tipo = "TK_CADEIA"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo, lexema))
                        tk.tokens["TK_CADEIA"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        lexema = ""
                        indice_caractere -= 1
                        coluna -=1
                    case 45: #45 -> [46,47] 
                        if token == "=":
                            estado = 46
                        else:
                            estado = 47
                            indice_caractere -= 1
                            coluna -=1
                    case 46: #maior igual
                        token_tipo = "TK_MAIOR_IGUAL"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_MAIOR_IGUAL"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 47: #maior que
                        token_tipo = "TK_MAIOR_QUE"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo))
                        tk.tokens["TK_MAIOR_QUE"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                    case 48: #48 -> [40,85]
                        if token == "=":
                            estado = 40
                        else:
                            estado = 85       
                            msg_erro = f"Erro linha {linha} coluna {coluna}: caractere '=' esperado"
                            indice_caractere -= 1
                            coluna -=1
                    case 49: #49 -> [51,75,76]
                        if token == ".":
                            estado = 51
                            lexema += token
                        elif token in tk.TOKEN_NUM:
                            estado = 76
                            lexema += token
                        else: 
                            estado = 75
                            indice_caractere -= 1
                            coluna -=1
                    case 51: #51 -> [52,53,70]
                        if token in tk.TOKEN_NUM:
                            estado = 52
                            lexema += token
                        elif token == "e":
                            estado = 53
                            lexema += token
                        else:
                            estado = 70
                    case 52: #52 -> [52,53,57]
                        if token in tk.TOKEN_NUM:
                            estado = 52
                            lexema += token
                        elif token == "e":
                            estado = 53
                            lexema += token
                        else:
                            estado = 57
                    case 53: #53 -> [54,55,85]
                        if token in tk.TOKEN_NUM:
                            estado = 55
                            lexema += token
                        elif token == "-":
                            estado = 54
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: float mal formatado {lexema}"
                            indice_caractere -= 1
                            coluna -=1
                    case 54: #54 -> [55,85]
                        if token in tk.TOKEN_NUM:
                            estado = 55
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: float mal formatado {lexema}"
                            indice_caractere -= 1
                            coluna -=1
                    case 55: #55 -> [55,56]
                        if token in tk.TOKEN_NUM:
                            estado = 55
                            lexema += token
                        else:
                            estado = 56
                            indice_caractere -= 1
                            coluna -=1
                    case 56: #float
                        token_tipo = "TK_FLOAT"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo, lexema))
                        tk.tokens["TK_FLOAT"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        lexema = ""
                        indice_caractere -= 1
                        coluna -=1
                    case 57: #float
                        token_tipo = "TK_FLOAT"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo, lexema))
                        tk.tokens["TK_FLOAT"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        lexema = ""
                        indice_caractere -= 1
                        coluna -=1
                    case 58: #58 -> [59,85]
                        if token == "x":
                            estado = 59
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: endereco mal formatado {lexema}"
                            indice_caractere -= 1
                            coluna -=1
                    case 59: #59 -> [60,85]
                        if token in tk.TOKEN_NUM + tk.TOKEN_HEXA:
                            estado = 60
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: endereco mal formatado {lexema}"
                            indice_caractere -= 1
                            coluna -=1
                    case 60: #60 -> [60,61]
                        if token in tk.TOKEN_NUM + tk.TOKEN_HEXA:
                            estado = 60
                            lexema += token
                        else:
                            estado = 61
                            indice_caractere -= 1
                            coluna -=1
                    case 61: #endereco
                        token_tipo = "TK_END"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo, lexema))
                        tk.tokens["TK_END"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        lexema = ""
                        indice_caractere -= 1
                        coluna -=1
                    case 62: #62 -> [63,85]
                        if token == "<":
                            estado = 63
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: erro em abertura de comentario em bloco"
                    case 63: #63 -> [63,66]
                        if token == ">":
                            estado = 66
                        else:
                            estado = 63
                    case 64: #64 -> [64,65]
                        if token == "\n":
                            estado = 65
                        else:
                            estado = 64
                    case 65: #comentario em linha 
                        #o comentario em linha foi formatado de maneira correta
                        estado = 0
                        ...
                    case 66: #66 -> [63,67]
                        if token == ">":
                            estado = 67
                        else:
                            estado = 63
                    case 67: #67 -> [63,69]
                        if token == ">":
                            estado = 69
                        else:
                            estado = 63
                    case 68: #68 -> [53,85]
                        if token == "e":
                            estado = 53
                            lexema += token
                        else:
                            estado = 85
                            msg_erro = f"Erro linha {linha} coluna {coluna}: float mal formatado {lexema}"
                            indice_caractere -= 1
                            coluna -=1
                    case 69: #comentario em bloco
                        #o comentario em bloco foi formatado de maneira correta
                        estado = 0
                        ...
                    case 70: #float
                        token_tipo = "TK_FLOAT"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo, lexema))
                        tk.tokens["TK_FLOAT"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        lexema = ""
                        indice_caractere -= 1
                        coluna -=1
                    case 75: #int
                        token_tipo = "TK_INT"
                        tk_lista.write(f.gravar_lexema(linha, coluna, token_tipo, lexema))
                        tk.tokens["TK_INT"] += 1
                        tk.tokens["TK_TOTAL"] += 1
                        estado = 0
                        lexema = ""
                        indice_caractere -= 1
                        coluna -=1
                    case 76: #76 -> [75,76]
                        if token in tk.TOKEN_NUM:
                            estado = 76
                            lexema += token
                        else:
                            estado = 75
                    case 85:
                        arquivo_erros.write(msg_erro + '\n')
                        msg_erro = ""  # Limpa a mensagem de erro após escrevê-la
                        lexema = ""
                        estado = 0
                        indice_caractere -= 1
                        coluna -=1
                        ...
                indice_caractere += 1
        tk_lista.close()
f.gravar_somatorio()