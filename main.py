import pandas as pd

# Passo a passo de solução

# Abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'Nomes {mes} foi batido a meta por o Vendedor: {vendedor}, Vendas: {vendas}')


# Para cada arquivo:

# Verificar se algum valor naquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> enviar um SMS com o mês e as vendas do vendedor

# caso não seja maior , não fazer nada