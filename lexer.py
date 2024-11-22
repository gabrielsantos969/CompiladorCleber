import ply.lex as lex

tokens = (
    'CLEBER',
    'CLEBERINT',
    'CLEBERSTRING',
    'CLEBERBOOL',
    'CLEBERPRINT',
    'IFCLEBER',
    'ELSECLEBER',
    'IDENTIFIER',
    'ASSIGN',
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'INTEGER',
    'STRING',
    'BOOLEAN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'GREATER',
    'LESS',
    'GTE',
    'LTE',
    'NOTEQUAL'
)


def t_IFCLEBER(t):
    r'\bifCleber\b'
    return t

def t_ELSECLEBER(t):
    r'\belseCleber\b'
    return t

def t_CLEBER(t):
    r'\bcleber\b'
    return t

def t_CLEBERINT(t):
    r'\bcleberInt\b'
    return t

def t_CLEBERSTRING(t):
    r'\bcleberString\b'
    return t

def t_STRING(t):
    r'"([^"\\]|\\.)*"'  # Aceita strings entre aspas duplas, incluindo escapadas
    try:
        # Decodifica sequências de escape e converte para UTF-8
        t.value = t.value[1:-1].encode('latin1').decode('utf-8')
    except UnicodeDecodeError:
        print(f"Erro ao decodificar a string: {t.value}")
        t.value = t.value[1:-1]  # Retorna a string sem as aspas
    return t

def t_CLEBERBOOL(t):
    r'\bcleberBool\b'
    return t

def t_CLEBERPRINT(t):
    r'\bcleberPrint\b'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t


t_ASSIGN = r'='
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_INTEGER = r'-?\d+'
t_BOOLEAN = r'\bcleberVerdadeiro\b|\bcleberFalso\b'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_EQUALS = r'=='
t_GREATER = r'>'
t_LESS = r'<'
t_GTE = r'>='
t_LTE = r'<='
t_NOTEQUAL = r'!='

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caracter inválido '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Função de teste para verificar os tokens reconhecidos
def test_lexer(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)



