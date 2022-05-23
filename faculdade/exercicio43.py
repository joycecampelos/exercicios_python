'''
EXERCÍCIO 43 - O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
…
50 - R$ 9.00
'''

preço = float(input('Preço do pão : R$ '))
print('Panificadora Pão de Ontem - Tabela de preços')
for c in range(1, 51):
    print(f'{c:2} - R$ {preço * c:.2f}')