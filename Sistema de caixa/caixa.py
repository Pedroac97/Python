from time import sleep  # sleep: pausa dramaticas
print('{:=^42}'.format(' GEEK TEMPLE '))
on = 1
contSoma= preçoFim = 0
listaProdutos = []
while on != 2:

    #inicia ou finalisa o programa
    on = int(input('''        ╔═══════════════════════════════╗
        ║[1]Abrir o caixa para pagamento║
        ║[2] Finalizar Programa         ║
        ╚═══════════════════════════════╝
Oque deseja? '''))
    if on == 1:
        while True:

            #fala qual é o produto vendido e o valor
            produto = str(input('Qual Produto? ')).title().strip()
            preço = desconto = float(input('Qual valor do produto?(valores com virgula use ".") R$'))
            listaProdutos.append(produto)
            listaProdutos.append(preço)
            while True:
                preçoFim += preço
                onn = str(input('Quer Somar mais Algum numero? [S/N]')).upper().strip()[0]
                if onn in 'Ss':
                    contSoma += 1
                    break
                elif onn in 'Nn':
                    print(f'\033[;32m Valor: R${preçoFim} \033[m')
                    break
            if onn in 'Nn':
                break

            #escolhe a forma de pagamento
        pagamento = int(input('''        ╔══════ FORMAS DE PAGAMENTO ══════╗
        ║[1] Avista Dinheiro/Cheque(-10%) ║
        ║[2] Avista no cartão(-5%)        ║ 
        ║[3] 2x no cartão                 ║
        ║[4] 3x ou mais no cartão(+20%)   ║
        ╚═════════════════════════════════╝
Qual opção de pagamento? '''))
        while True:
            if pagamento == 1:
                #Pagamento em Dinheiro

                desconto -= preçoFim * 0.10
                print('Produto ganha desconto de 10% e vai de R${}, para R${}'.format(preçoFim, desconto))
                valor = float(input('Valor recebido: '))
                while valor < desconto:
                    valor = float(input('\033[1;;41m Valor Abaixo!!!\033[m Valor recebido: '))
                troco = valor - desconto
                print(f'Troco R${troco}')
                ced = 100
                total = 0
                while True:
                    if troco >= ced:
                        troco -= ced
                        total += 1
                    else:
                        # sistema de Troco para o cliente
                        if total != 0:
                            if ced >= 2:
                                print(f'{total} notas de R${ced}')
                            elif ced <= 1:
                                print(f'{total} moedas de {ced} \033[1;31m!!!Estamos sem moedas!!!\033[m')
                        total = 0
                        if ced == 100:
                            ced = 50
                        elif ced == 50:
                            ced = 20
                        elif ced == 20:
                            ced = 10
                        elif ced == 10:
                            ced = 5
                        elif ced == 5:
                            ced = 2
                        elif ced == 2:
                            ced = 1
                        elif ced == 1:
                            ced = 0.5
                        elif ced == 0.5:
                            ced = 0.25
                        elif ced == 0.25:
                            ced = 0.1
                        elif ced == 0.1:
                            break
                        if troco == 0:
                            break
                print('Imprimindo Comprovante')
                sleep(3)
                print('~~' * 25)
                print('-' * 40)
                print(f'{"LISTAGEM DE PRODUTOS":^40}')
                print('-' * 40)
                for pos in range(0, len(listaProdutos)):
                    if pos % 2 == 0:
                        print(f'{listaProdutos[pos]:.<30}', end='')
                    else:
                        print(f'R${listaProdutos[pos]:>7.2f}')
                print('-' * 40)
                print(f'{"VOLTE SEMPRE":^40}')
                print('-' * 40)
                print('~~' * 25)
                sleep(3)
                preçoFim = 0
                listaProdutos = []
                break
            elif pagamento == 2:
                #Pagamento em avista no cartão
                desconto -= preçoFim * 0.05
                print('Produto ganha desconto de 5% e vai de R${}, para R${}'.format(preçoFim, desconto))
                print('Volte sempre')
                sleep(3)
                print('~~' * 25)
                preçoFim = 0
                listaProdutos = []
                break
            elif pagamento == 3:
                #Pagamneto em 2x
                print('Preço R${}'.format(preçoFim))
                print('Imprimindo Comprovante')
                sleep(3)
                print('~~' * 25)
                print('-' * 40)
                print(f'{"LISTAGEM DE PRODUTOS":^40}')
                print('-' * 40)
                for pos in range(0, len(listaProdutos)):
                    if pos % 2 == 0:
                        print(f'{listaProdutos[pos]:.<30}', end='')
                    else:
                        print(f'R${listaProdutos[pos]:>7.2f}')
                print('-' * 40)
                print(f'{"VOLTE SEMPRE":^40}')
                print('-' * 40)
                print('~~' * 25)
                sleep(3)
                preçoFim = 0
                listaProdutos = []
                break
            elif pagamento == 4:
                #Pagamneto em 3x ou mais
                juros = preçoFim * 0.20
                print('Produto fica 20% de juros. De R${} para R${}'.format(preçoFim, (preçoFim + juros)))
                print('Volte sempre')
                sleep(3)
                print('~~' * 25)
                preçoFim = 0
                listaProdutos = []
                break
            elif pagamento > 4 or 0 >= pagamento:
                #lupera para recoção de erros na ecolha do pagamento
                erro = str(input('\033[1;31mOpção invalida!!!\033[m Quer tentar novamente[S/N]: ')).upper().strip()[0]
                if erro in "Ss":
                    pagamento = int(input('''        ╔══════ FORMAS DE PAGAMENTO ══════╗
        ║[1] Avista Dinheiro/Cheque(-10%) ║
        ║[2] Avista no cartão(-5%)        ║ 
        ║[3] 2x no cartão                 ║
        ║[4] 3x ou mais no cartão(+20%)   ║
        ╚═════════════════════════════════╝
Qual opção de pagamento? '''))
                else:
                    break
    elif on != 2:
        erro = str(input('\033[1;31mOpção invalida!!!\033[m Quer tentar novamente[S/N]: ')).upper().strip()[0]
        if erro in "Nn":
            break
    else:
        break
print('Programa finalizado!!!')