import lexer
import parser
from executor import execute_program
def write_intermed_output(file_path, dataOutput):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("Código intermediário Léxico:\n")
        file.write(dataOutput)
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

data = read_file('index.cleber')

lexer.test_lexer(data)

ast = parser.parser.parse(data)

execute_program(ast)

write_intermed_output('codigo_intermediario_gerado.txt',  data)
      
parser.write_symbol_table_to_file('symbol_table.txt')