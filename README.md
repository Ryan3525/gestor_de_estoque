# gestor_de_estoque
Gestor de Estoque e Auditoria de Dados

Este projeto é uma ferramenta em Python desenvolvida para automatizar o fluxo de entrada, precificação e análise estatística de produtos em um inventário. Ele resolve o problema comum de converter custos brutos em preços de venda otimizados, garantindo a persistência dos dados para análise externa.

## Funcionalidades

- **Fluxo de Dados Interativo:** Cadastro de produtos e preços diretamente pelo terminal, com tratamento de strings (limpeza de espaços e conversão de vírgulas).
- **Cálculo de Precificação:** - Aplicação automática de margem de lucro e impostos.
  - Geração de "Preço de Etiqueta" (Psicológico) utilizando arredondamento para cima (`math.ceil`).
- **Auditoria Estatística:**
  - Cálculo de média aritmética dos preços.
  - Identificação do produto de maior valor.
  - Cálculo de **Desvio Padrão** para medir a variabilidade do estoque.
- **Exportação de Dados:** Geração automática de um arquivo `.csv` para abertura em Excel ou Google Sheets.

##  Tecnologias e Conceitos

- **Linguagem:** Python
- **Bibliotecas Nativas:** - `math`: Operações matemáticas avançadas (raiz quadrada e arredondamentos).
  - `csv`: Persistência de dados em arquivos estruturados.
- **Tratamento de Exceções:** Uso de blocos `try...except` para evitar interrupções por erros de digitação (letras em campos numéricos ou valores negativos).
- **Estruturas de Dados:** Utilização de dicionários aninhados para organizar as propriedades de cada produto.

## Como Utilizar

1. **Clonar o repositório:**
   
   git clone [https://github.com/Ryan3525/gestor_de_estoque.git](https://github.com/Ryan3525/gestor_de_estoque.git)

2. **Executar o script:**

   python calculo_precificacao.py

3. **Interagir com o sistema:**

   Insira os nomes e preços conforme solicitado. Digite fim para encerrar e gerar o relatório e o arquivo CSV.


##  Estrutura do Arquivo Gerado
O arquivo relatorio_estoque.csv será criado na mesma pasta do script com as seguintes colunas:

- Produto: Nome formatado do item.

- Preco_Venda_Bruto: Valor calculado com margem.

- Preco_Etiqueta: Valor final sugerido para venda.
