variables = {}

def execute_program(program):
    if program is not None:
        for statement in program[1]:
            execute_statement(statement)
    else:
        print("Erro: Nenhum programa a ser executado.")

def execute_statement(statement):
    if statement[0] == 'declaration':
        _, var_type, var_name, var_value = statement
        if var_value:
            var_value = evaluate_expression(var_value)
        variables[var_name] = (var_type, var_value)
    elif statement[0] == 'assignment':
        _, var_name, var_value = statement
        var_value = evaluate_expression(var_value)
        if var_name in variables:
            variables[var_name] = (variables[var_name][0], var_value)
        else:
            print(f"Variável '{var_name}' não declarada")
    elif statement[0] == 'print':
        _, value = statement
        print(evaluate_expression(value))
    elif statement[0] == 'if':
        _, condition, if_block, else_block = statement
        if evaluate_expression(condition):
            execute_block(if_block)
        elif else_block:
            execute_block(else_block)

def execute_block(block):
    for statement in block[1]:
        execute_statement(statement)


def evaluate_expression(expression):
    if isinstance(expression, tuple) and expression[0] == 'operation':
        op = expression[1]
        left = evaluate_expression(expression[2])
        right = evaluate_expression(expression[3])
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left / right
        
    elif isinstance(expression, tuple) and expression[0] == 'comparison':
        comp = expression[1]
        left = evaluate_expression(expression[2])
        right = evaluate_expression(expression[3])
        if comp == 'equals':
            return left == right
        elif comp == 'greater':
            return left > right
        elif comp == 'less':
            return left < right
        elif comp == 'gte':
            return left >= right
        elif comp == 'lte':
            return left <= right
        elif comp == 'notequal':
            return left != right
        
    elif isinstance(expression, str) and expression.startswith('"') and expression.endswith('"'):
        return expression[1:-1]
    
    elif expression.isdigit() or (expression.startswith('-') and expression[1:].isdigit()):
        return int(expression)
    
    elif expression == 'cleberVerdadeiro':
        return True
    
    elif expression == 'cleberFalso':
        return False
    
    elif isinstance(expression, str) and (expression.isdigit() or (expression.startswith('-') and expression[1:].isdigit())):
        return int(expression)
    
    return variables.get(expression, (None, expression))[1]

# Teste para verificar se tudo está funcionando corretamente
if __name__ == "__main__":
    data = [
        ('declaration', 'cleberInt', 'num1', 10),
        ('declaration', 'cleberInt', 'num2', 5),
        ('declaration', 'cleberString', 'str1', '"Hello"'),
        ('declaration', 'cleberString', 'str2', '"World"'),
        ('declaration', 'cleberBool', 'bool1', 'cleberVerdadeiro'),
        ('declaration', 'cleberBool', 'bool2', 'cleberFalso'),
        ('print', ('operation', '+', 'num1', 'num2')),
        ('print', ('operation', '+', 'str1', '" - "', 'str2')),
        ('print', 'bool1'),
        ('print', 'bool2')
    ]
    execute_program(('program', data))
