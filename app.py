import os
import pandas as pd
import plotly.express as px

caminho = 'D:\Documentos\Programação\Curso básico de python\Vendas'

lista_arquivos = os.listdir(caminho)
tabela_total = pd.DataFrame()

for arquivo in lista_arquivos:
    if 'venda' in arquivo.lower():
        tabela = pd.read_csv(f'{caminho}\{arquivo}')
        tabela_total = tabela_total.append(tabela)

# Produto que mais vendeu
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida', 'Preco Unitario']].sort_values(by='Quantidade Vendida', ascending=False)

print(tabela_produtos)

# Produto que mais faturou
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)

print(tabela_faturamento)


# Loja que mais faturou
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tabela_lojas)

# grafico de faturamento de lojas
grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()