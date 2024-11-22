import ply.yacc as yacc
from lexer import tokens

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
                 | if_statement'''
    p[0] = p[1]

def p_if_statement(p):
    '''if_statement : IFCLEBER LPAREN expression RPAREN LBRACE statement_list RBRACE else_statement'''
    p[0] = ('if', p[3], ('block', p[6]), p[8])

def p_else_statement(p):
    '''else_statement : ELSECLEBER LBRACE statement_list RBRACE
                      | empty'''
    if len(p) == 5:
        p[0] = ('block', p[3])
    else:
        print("Else vazio")
        p[0] = None



def p_empty(p):
    'empty :'
    p[0] = None

def p_block(p):
    '''block : LBRACE statement_list RBRACE'''
    p[0] = ('block', p[2])

def p_declaration(p):
    '''declaration : CLEBER type IDENTIFIER ASSIGN expression SEMICOLON
                   | CLEBER type IDENTIFIER SEMICOLON'''
    if len(p) == 7:
        p[0] = ('declaration', p[2], p[3], p[5])
    else:
        p[0] = ('declaration', p[2], p[3], None)

def p_assignment(p):
    'assignment : IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = ('assignment', p[1], p[3])

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
                  | expression NOTEQUAL expression'''
    if len(p) == 2:
        p[0] = p[1]  # Valor simples
    else:
        # Operações aritméticas
        if p[2] in ['+', '-', '*', '/']:
            p[0] = ('operation', p[2], p[1], p[3])
        # Operações de comparação
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
