opcao = 0
manifestos = []
tipos = ['Sugestão', 'Reclamação', 'Elogio']
print('{:^30}'.format('OUVIDORIA ABC'))  # Colocar no meio
while opcao != 7:
    print('=' * 35)
    print('1) Listar todas as manifestações.')
    print('2) Listar todas as sugestões.')
    print('3) Listar todas as reclamações.')
    print('4) Listar todas os elogios.')
    print('5) Enviar nova manifestação.')
    print('6) Pesquisar por ID.')
    print('7) Sair')
    print('=' * 35)
    opcao = int(input('Digite a opção que você deseja: '))
    print()
    if opcao < 1 or opcao > 7:  # Menor que 1 ou maiores que 7 ==> Opção inválida.
        print('Opção inválida!')

    elif opcao == 1:  # Mostrar todas as manifestações disponíveis.
        print('Manifestações:')
        if manifestos == []:  # Se manifestor for igual [] imprime o print.
            print('Nenhuma manifestação encontrada!')
        for i in manifestos:
            maniqueb = i.replace('#', ' - ')
            print('CÓDIGO', maniqueb)

    elif opcao == 2:  # Mostrar sugestões as disponiveís.
        print('Sugestões:')
        for i in manifestos:
            maniqueb2 = i.split('#')
            if tipos[0] == maniqueb2[
                    2]:  # Se os tipos[0] for igua a maniqueb2(manifestos quebrado) imprime as sugestões.
                maniqueb2.pop(2)
                print('CÓDIGO', end='')
                for i in maniqueb2:
                    print(' -', i, end='')
            print()

    elif opcao == 3:  # Mostrar todas as reclamações.
        print('Reclamações:')
        for i in manifestos:
            maniqueb3 = i.split('#')
            if tipos[1] == maniqueb3[
                    2]:  # Se os tipos[1] for igua a maniqueb3(manifestos quebrado) imprime as reclamações.
                maniqueb3.pop(2)
                print('CÓDIGO', end='')
                for i in maniqueb3:
                    print(' -', i, end='')
            print()

    elif opcao == 4:  # Mostrar todos os elogios.
        print('Elogios:')
        for i in manifestos:
            maniqueb4 = i.split('#')
            # Se os tipos[2] for igua a maniqueb4(manifestos quebrado) imprime os elogios.
            if tipos[2] == maniqueb4[2]:
                maniqueb4.pop(2)
                print('CÓDIGO', end='')
                for i in maniqueb4:
                    print(' -', i, end='')
            print()

    elif opcao == 5:  # Enviar nova manifestação conforme seu tipo.
        tipo = 0
        prot = str(len(manifestos) + 1)
        nome = str(input('Requisitante: '))
        while tipo < 1 or tipo > 3:
            print('1) Sugestão')
            print('2) Reclamação')
            print('3) Elogio ')
            tipo = int(input('Digite o tipo de manifestação: '))
            if tipo < 1 or tipo > 3:  # Menor que 1 ou maiores que 3 ==> Opção inválida.
                print('Opção inválida!')
        descricao = str(input('Digite seu manifesto: '))
        manifestostotal = prot + '#' + nome + \
            '#' + tipos[tipo - 1] + '#' + descricao
        manifestos.append(manifestostotal)  # Adicionar dentro de manifestos.
        print(f"O numero do seu protocolo é {prot}")

    elif opcao == 6:  # Pesquisar manifetações por número(ID).
        numeroprot = -1
        tamanhoproto = len(manifestos)
        while numeroprot <= 0 or numeroprot > tamanhoproto:
            # Pesquisar manifestação por número.
            numeroprot = int(input('Informe o número do protocolo: '))
            # Menor ou igual 0, ou maior que o tamanho do protocolo imprime o print.
            if numeroprot <= 0 or numeroprot > tamanhoproto:
                print('Número do protolo inválido, consulte-o novamente!')
                break
        for i in manifestos:
            maniqueb5 = i.split('#')  # Manifestos quebrado.
            # Se maniqueb5[0] for igual ao numeroprot imprime a manifestação.
            if int(maniqueb5[0]) == numeroprot:
                print('CÓDIGO', end='')
                for i in maniqueb5:
                    print(' -', i, end='')
            print()

print('Encerrando... Até mais')
