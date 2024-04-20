# Este arquivo contém a definição dos tokens usados no analisador léxico.

# REGISTRO DE CARACTERES
TOKEN_NUM = "0123456789"
TOKEN_HEXA = "ABCDEF"
TOKEN_ALFABETO_MAX = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
TOKEN_ALFABETO_MIN = "abcdefghijklmnopqrstuvwxyz"

# PALAVRAS RESERVADAS
tk_rotina = "rotina"
tk_fim_rotina = "fim_rotina"
tk_se = "se"
tk_senao = "senao"
tk_imprima = "imprima"
tk_leia = "leia"
tk_para = "para"
tk_enquanto = "enquanto"

# Dicionário para armazenar os tokens
tokens = {
    "TK_INT": 0,
    "TK_FLOAT": 0,
    "TK_DATA": 0,
    "TK_END": 0,
    "TK_CADEIA": 0,
    "TK_ID": 0,
    "TK_MENOS": 0,
    "TK_NEGACAO": 0,
    "TK_MAIS": 0,
    "TK_MULTIPLICACAO": 0,
    "TK_DIVISAO": 0,
    "TK_AND": 0,
    "TK_OR": 0,
    "TK_MAIOR_QUE": 0,
    "TK_MAIOR_IGUAL": 0,
    "TK_IGUAL": 0,
    "TK_MENOR_QUE": 0,
    "TK_MENOR_IGUAL": 0,
    "TK_DIFERENTE": 0,
    "TK_ATRIBUICAO": 0,
    "TK_DOIS_PONTOS": 0,
    "TK_ABR_PARENTESES": 0,
    "TK_FEC_PARENTESES": 0,
    "TK_ROTINA": 0,
    "TK_FIM_ROTINA": 0,
    "TK_SE": 0,
    "TK_SENAO": 0,
    "TK_IMPRIMA": 0,
    "TK_LEIA": 0,
    "TK_PARA": 0,
    "TK_ENQUANTO": 0,
    "TK_TOTAL": 0
}