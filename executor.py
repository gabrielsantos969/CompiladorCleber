variables = {}

def write_intermed_py(file_path, data_output):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data_output)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def execute_program(program):
    if program is not None:
        python_code = generate_python_code(program)
        write_intermed_py("codigo_intermediario_compilado_gerado.py", python_code)
        exec(python_code, globals())
    else:
        print("Erro: Nenhum programa a ser executado.")

def generate_python_code(program):
    python_code = ""
    for statement in program[1]:
        python_code += generate_statement_code(statement) + "\n"
    return python_code

def generate_statement_code(statement):
    if statement[0] == 'declaration':
        _, var_type, var_name, var_value = statement
        if var_type == 'cleberBloco':
            code = f"class {var_name}:\n"
            for stmt in var_value[1]:
                code += "    " + generate_statement_code(stmt) + "\n"
            code += f"{var_name.lower()} = {var_name}()"
            return code
        elif var_value:
            return f"{var_name} = {generate_expression_code(var_value)}"
        else:
            return f"{var_name} = None"
    elif statement[0] == 'assignment':
        _, var_name, var_value = statement
        if '.' in var_name:
            block, member = var_name.split('.')
            return f"{block}.{member} = {generate_expression_code(var_value)}"
        else:
            return f"{var_name} = {generate_expression_code(var_value)}"
    elif statement[0] == 'print':
        _, value = statement
        return f"print({generate_expression_code(value)})"
    elif statement[0] == 'if':
        _, condition, if_block, else_block = statement
        code = f"if {generate_expression_code(condition)}:\n"
        code += generate_block_code(if_block)
        if else_block:
            code += "else:\n"
            code += generate_block_code(else_block)
        return code
    elif statement[0] == 'for':
        _, init, condition, update, block = statement
        code = f"for {generate_statement_code(init)}; {generate_expression_code(condition)}; {generate_statement_code(update)}:\n"
        code += generate_block_code(block)
        return code
    elif statement[0] == 'block':
        _, statements = statement
        code = "{\n"
        for stmt in statements:
            code += generate_statement_code(stmt) + "\n"
        code += "}"
        return code

def generate_block_code(block):
    code = ""
    for statement in block[1]:
        code += "    " + generate_statement_code(statement) + "\n"
    return code

def generate_expression_code(expression):
    if isinstance(expression, tuple) and expression[0] == 'operation':
        _, op, left, right = expression
        return f"({generate_expression_code(left)} {op} {generate_expression_code(right)})"
    elif isinstance(expression, tuple) and expression[0] == 'comparison':
        _, comp, left, right = expression
        return f"({generate_expression_code(left)} {comp} {generate_expression_code(right)})"
    elif isinstance(expression, tuple) and expression[0] == 'member_access':
        _, block, member = expression
        return f"{block}.{member}"
    elif isinstance(expression, tuple):
        return generate_expression_code(expression[1])
    elif isinstance(expression, str) and expression.startswith('"') and expression.endswith('"'):
        return expression
    elif isinstance(expression, str) and (expression.isdigit() or (expression.startswith('-') and expression[1:].isdigit())):
        return expression
    elif expression == 'cleberVerdadeiro':
        return "True"
    elif expression == 'cleberFalso':
        return "False"
    elif isinstance(expression, list):
        return generate_expression_code(expression[0])
    elif expression in variables:
        return variables[expression]
    return expression

def execute_statement(statement):
    if statement[0] == 'declaration':
        _, var_type, var_name, var_value = statement
        if var_type == 'cleberBloco':
            variables[var_name] = {}
            for stmt in var_value[1]:
                execute_statement(stmt)
        elif var_value:
            variables[var_name] = generate_expression_code(var_value)
        else:
            variables[var_name] = None
    elif statement[0] == 'assignment':
        _, var_name, var_value = statement
        if '.' in var_name:
            block, member = var_name.split('.')
            if block in variables:
                variables[block][member] = generate_expression_code(var_value)
            else:
                print(f"Erro: Bloco '{block}' não declarado.")
        else:
            variables[var_name] = generate_expression_code(var_value)
    elif statement[0] == 'print':
        _, value = statement
        print(eval(generate_expression_code(value)))
    elif statement[0] == 'if':
        _, condition, if_block, else_block = statement
        if eval(generate_expression_code(condition)):
            execute_block(if_block)
        elif else_block:
            execute_block(else_block)
    elif statement[0] == 'for':
        _, init, condition, update, block = statement
        execute_statement(init)
        while eval(generate_expression_code(condition)):
            execute_block(block)
            execute_statement(update)
    elif statement[0] == 'block':
        _, statements = statement
        execute_block(statements)

def execute_block(block):
    for statement in block[1]:
        execute_statement(statement)

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
        ('print', 'bool2'),
    ]
    execute_program(('program', data))