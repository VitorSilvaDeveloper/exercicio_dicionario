def linha():
    print('-'*40)


dicionario_senhas = {}

linha()
while True:
    print('O que deseja fazer?')
    print('[adicionar] | [remover] | [listar] | [sair] ')
    opcao = str(input())
    opcao_nova = opcao.lower()
    if opcao_nova == 'adicionar':
        linha()
        usuario = input('Digite o novo usuario: ')
        senha = input('Digite a senha nova: ')
        linha()
        dicionario_senhas[usuario] = senha

    elif opcao_nova == 'remover':
        print('Digite o usuario que quer exluir: ')
        excluir_usuario = str(input())
        if excluir_usuario in dicionario_senhas:
            print('Excluindo usuario...')
            print('Atualizando dados...')
            del dicionario_senhas[excluir_usuario]
            print(f'Usuario {excluir_usuario} foi excluido.')
        else:
            print('Usuario não enontrado. ERROR')
    
    elif opcao_nova == 'listar':
        print('Listando pares de valores. Separados por virgula [USUARIO:SENHA]')
        print(dicionario_senhas)
    
    elif opcao_nova == 'sair':
        sair = str(input('Certeza que quer sair? [s/n] '))
        vai_sair = sair.lower()
        if vai_sair == 's':
            print('Finalizando o programa..')
            break
        elif vai_sair == 'n':
            continue
    else:
        print('Comando invalido. ERROR')
