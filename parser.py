from lexer import tokens
import ply.yacc as yacc  # Adicionando a importação do módulo yacc

symbol_table = {}

def p_program(p):
    'program : statement_list'
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : declaration
                 | assignment
                 | print_statement
                 | if_statement
                 | for_statement'''
    p[0] = p[1]

def p_if_statement(p):
    '''if_statement : IFCLEBER LPAREN expression RPAREN LBRACE statement_list RBRACE else_statement'''
    p[0] = ('if', p[3], ('block', p[6]), p[8])

def p_else_statement(p):
    '''else_statement : ELSECLEBER LBRACE statement_list RBRACE
                      | empty'''
    if len(p) == 5:
        p[0] = ('else', ('block', p[3]))
    else:
        p[0] = None

def p_for_statement(p):
    '''for_statement : FORCLEBER LPAREN for_initialization COMMA expression COMMA for_update RPAREN block'''
    p[0] = ('for', p[3], p[5], p[7], p[9])

def p_for_initialization(p):
    '''for_initialization : declaration
                          | assignment'''
    p[0] = p[1]

def p_for_update(p):
    '''for_update : assignment'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    p[0] = None

def p_block(p):
    '''block : LBRACE statement_list RBRACE'''
    p[0] = ('block', p[2])

def p_declaration(p):
    '''declaration : CLEBER type IDENTIFIER ASSIGN expression SEMICOLON
                   | CLEBER type IDENTIFIER SEMICOLON
                   | CLEBER type IDENTIFIER ASSIGN expression
                   | CLEBER type IDENTIFIER
                   | CLEBER CLEBERBLOCO IDENTIFIER ASSIGN block SEMICOLON'''
    if len(p) == 7:
        p[0] = ('declaration', p[2], p[3], p[5])
        symbol_table[p[3]] = {'type': p[2], 'value': p[5]}
    elif len(p) == 4:
        p[0] = ('declaration', p[2], p[3], None)
        symbol_table[p[3]] = {'type': p[2], 'value': None}
    elif len(p) == 6:
        p[0] = ('declaration', p[2], p[3], p[5])
        symbol_table[p[3]] = {'type': p[2], 'value': p[5]}
    else:
        p[0] = ('declaration', p[2], p[3], None)
        symbol_table[p[3]] = {'type': p[2], 'value': None}

def p_assignment(p):
    '''assignment : IDENTIFIER ASSIGN expression SEMICOLON
                  | IDENTIFIER DOT IDENTIFIER ASSIGN expression SEMICOLON'''
    if len(p) == 5:
        p[0] = ('assignment', p[1], p[3])
    else:
        p[0] = ('assignment', f"{p[1]}.{p[3]}", p[5])
    if p[1] in symbol_table:
        symbol_table[p[1]]['value'] = p[3]
    else:
        print(f"Erro: Variável '{p[1]}' não declarada.")

def p_print_statement(p):
    'print_statement : CLEBERPRINT LPAREN expression RPAREN SEMICOLON'
    p[0] = ('print', p[3])

def p_expression(p):
    '''expression : value
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression EQUALS expression
                  | expression GREATER expression
                  | expression LESS expression
                  | expression GTE expression
                  | expression LTE expression
                  | expression NOTEQUAL expression
                  | IDENTIFIER DOT IDENTIFIER'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4 and p[2] == '.':
        p[0] = ('member_access', p[1], p[3])
    else:
        if p[2] in ['+', '-', '*', '/']:
            p[0] = ('operation', p[2], p[1], p[3])
        elif p[2] == '==':
            p[0] = ('comparison', 'equals', p[1], p[3])
        elif p[2] == '>':
            p[0] = ('comparison', 'greater', p[1], p[3])
        elif p[2] == '<':
            p[0] = ('comparison', 'less', p[1], p[3])
        elif p[2] == '>=':
            p[0] = ('comparison', 'gte', p[1], p[3])
        elif p[2] == '<=':
            p[0] = ('comparison', 'lte', p[1], p[3])
        elif p[2] == '!=':
            p[0] = ('comparison', 'notequal', p[1], p[3])

def p_value(p):
    '''value : INTEGER
             | STRING
             | BOOLEAN
             | IDENTIFIER'''
    p[0] = p[1]

def p_type(p):
    '''type : CLEBERINT
            | CLEBERSTRING
            | CLEBERBOOL'''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Erro de sintaxe em '{p.value}' (Token: {p.type}) na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final da entrada")

parser = yacc.yacc()

def write_symbol_table_to_file(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for identifier, info in symbol_table.items():
            file.write(f"{identifier}: {info['type']} = {info['value']}\n")