## Guia de Clonagem e Execução do Compilador Cleber

### 1. Clonando o Projeto

Para clonar o projeto, você precisa ter o `Git` instalado. Use o seguinte comando:

```bash
git clone https://github.com/gabrielsantos969/CompiladorCleber.git
```

### 2. Criando um Ambiente Virtual (Recomendado)

É altamente recomendado criar um ambiente virtual para isolar as dependências do seu projeto. Isso evita conflitos com outras bibliotecas instaladas em seu sistema.

Para criar um ambiente virtual com `venv`, use o seguinte comando dentro da pasta do projeto:

```bash
python -m venv env
```

Ative o ambiente virtual:

```bash
source env/bin/activate  # Linux/macOS
env\Scripts\activate  # Windows
```

### 3. Instalando as Dependências

Após ativar o ambiente virtual, instale as dependências do projeto com o comando:

```bash
pip install -r requirements.txt
```

### 4. Executando o Projeto

Para executar o projeto, use o seguinte comando:

```bash
python main.py
```

### 5. Desativando o Ambiente Virtual

Após finalizar o trabalho, desative o ambiente virtual:

```bash
deactivate
```

### Dicas Adicionais:

* **Ply:** A biblioteca `ply` é usada para análise léxica e sintática. Certifique-se de ter a biblioteca instalada corretamente.
* **Documentação:** Consulte a documentação oficial do `ply` para obter mais informações sobre sua utilização: [https://www.dabeaz.com/ply/](https://www.dabeaz.com/ply/)
* **Depuração:** Use um depurador Python para encontrar e corrigir erros no seu código.

Espero que este guia te ajude a clonar, configurar e executar o nosso compilador! Se tiver mais alguma dúvida, não hesite em criar uma [Issue.md](../Duvidas/ISSUE.md). 😊
