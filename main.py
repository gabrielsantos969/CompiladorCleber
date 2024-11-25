import lexer
import parser
from executor import execute_program

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

data = read_file('index.cleber')

lexer.test_lexer(data)

ast = parser.parser.parse(data)
execute_program(ast)

parser.write_symbol_table_to_file('symbol_table.txt')