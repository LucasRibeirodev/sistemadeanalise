import pandas as pd

# Passo a Passo de solução
# abrir os 6 arquivos de excel

lista_meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
tabela_vendas = pd.read_excel ('janeiro.xlsx')

print(tabela_vendas)

# para cada arquivo:
# vertificar se algum valor na coluna vendas daquele arquivo é maior que 55 mil
# sefor maior que 55 mil enviar sms, sm contendo nome, o mes, e as vnedas do vendedor
# se for menor que 55 mil não fazer nada