import pandas as pd
from twilio.rest import Client

account_sid = "ACcb7ed67b5b59b33b9614ca205d6bec89"
# Your Auth Token from twilio.com/console
auth_token  = "56b041810efc14bb77b14aa5d34afb75"


# Passo a Passo de solução
# abrir os 6 arquivos de excel

lista_meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel (f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc [tabela_vendas ['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc [tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'No mês de {mes} o Vendedor {vendedor} atingiu a meta com o valor de {vendas}')
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to="+5541998239095",
            from_="+19897472553",
            body=f'No mês de {mes} o Vendedor {vendedor} atingiu a meta com o valor de {vendas}')

        print(message.sid)



# para cada arquivo:
# vertificar se algum valor na coluna vendas daquele arquivo é maior que 55 mil


# sefor maior que 55 mil enviar sms, sm contendo nome, o mes, e as vnedas do vendedor
# se for menor que 55 mil não fazer nada