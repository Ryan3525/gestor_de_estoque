import math
import csv  # Importação necessária para salvar o arquivo

def salvar_para_csv(estoque, nome_arquivo="relatorio_estoque.csv"):
    """Função para salvar os dados em um arquivo compatível com Excel"""
    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(['Produto', 'Preco_Venda_Bruto', 'Preco_Etiqueta'])
            for produto, valores in estoque.items():
                escritor.writerow([produto, valores['bruto'], valores['etiqueta']])
        print(f"\nArquivo '{nome_arquivo}' gerado com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def calcular_venda(custo):
    """Calcula preços com margem e impostos."""
    valor_venda = custo * 1.65  # Margem de 65%
    return {
        "bruto": round(valor_venda, 2),
        "etiqueta": math.ceil(valor_venda) - 0.01
    }

def realizar_auditoria(estoque):
    """
    Analisa a estrutura de dados e extrai métricas estatísticas
    Calcula a média, o maior preço, soma e porcentagem aplicada
    """
    if not estoque:
        return None

    # Extraindo apenas os valores brutos para análise
    precos = [info['bruto'] for info in estoque.values()]
    
    qtd = len(precos)
    media = sum(precos) / qtd
    maior_preco = max(precos)
    
    # Mostra a variação dos preços em relação à média
    soma_variancia = sum((x - media) ** 2 for x in precos)
    desvio_padrao = math.sqrt(soma_variancia / (qtd - 1)) if qtd > 1 else 0

    return {
        "total_itens": qtd,
        "media": round(media, 2),
        "maior": round(maior_preco, 2),
        "desvio": round(desvio_padrao, 2)
    }

banco_produtos = {}

print("CADASTRO DE PRODUTOS E PREÇOS")
while True:
    nome = input("\nNome do Produto (ou 'fim' para gerar relatório): ").strip().title()
    if nome.lower() == 'fim':
        break
        
    try:
        # Tratamento de exceção para entrada de preço
        preco_input = input(f"Preço de custo de '{nome}': ").replace(',', '.')
        custo = float(preco_input)
        
        if custo <= 0:
            print("Valor inválido. O preço deve ser positivo.")
            continue
            
        # Processamento e Armazenamento (Estrutura de Dados)
        banco_produtos[nome] = calcular_venda(custo)
        print(f"{nome} cadastrado!")

    except ValueError:
        print("Erro: Digite um número válido para o preço.")

# Resultados dos itens
if banco_produtos:
    print("\n" + "="*55)
    print(f"{'PRODUTO':<20} | {'VENDA (R$)':<10} | {'ETIQUETA':<10}")
    print("-" * 55)
    for p, v in banco_produtos.items():
        print(f"{p:<20} | {v['bruto']:>10.2f} | {v['etiqueta']:>10.2f}")
    
    # Insight dos dados passados
    stats = realizar_auditoria(banco_produtos)
    
    print("="*55)
    print("RESUMO ESTATÍSTICO DO ESTOQUE")
    print(f"Total de itens:  {stats['total_itens']}")
    print(f"Média de Preços: R$ {stats['media']}")
    print(f"Produto mais caro: R$ {stats['maior']}")
    print(f"Variação (Desvio): R$ {stats['desvio']}")
    print("="*55)

    # Gerar arquivo CSV para Excel
    salvar_para_csv(banco_produtos)

else:
    print("\nNenhum dado foi inserido para análise.")