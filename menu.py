import operacoes
import this

def menu():
    print('\n\nEscolha uma das opções abaixo: \n\n' +
            '1. Cadastrar\n'                        +
            '2. Consultar\n'                        +
            '3. Atualizar nome\n'                   +
            '4. Atualizar endereco\n'               +
            '5. Atualizar telefone\n'               +
            '6. Atualizar data atual\n'             +
            '7. Excluir\n'                          +
            '0. Sair')
    this.opcao = int(input())

def operacao():
    menu()
    if this.opcao == 1:
        print('Digite o nome: ')
        nome = input()
        print('Digite o endereço: ')
        endereco = input()
        print('Digite o telefone: ')
        telefone = input()
        print('Digite a data atual: ')
        dataAtual = input()
        #Utilizar o método cadastrar
        operacoes.inserir(nome, endereco, telefone, dataAtual)
    elif this.opcao == 2:
        operacoes.selecionar()
    elif this.opcao == 3:
        print('Informe o código: ')
        codigo = input()
        print('Informe o novo nome: ')
        nome = input()
        #Uso do método
        operacoes.atualizarNome(codigo, nome)
    elif this.opcao == 4:
        print('Informe o código: ')
        codigo = input()
        print('Informe o novo endereço: ')
        endereco = input()
        #Uso do método
        operacoes.atualizarEndereco(codigo, endereco)
    elif this.opcao == 5:
        print('Informe o código: ')
        codigo = input()
        print('Informe o novo telefone: ')
        telefone = input()
        #Uso do método
        operacoes.atualizarTelefone(codigo, telefone)
    elif this.opcao == 6:
        print('Informe o código: ')
        codigo = input()
        print('Informe a nova data: ')
        dataAtual = input()
        #Uso do método
        operacoes.atualizarData(codigo, dataAtual)
    elif this.opcao == 7:
        print('Informe o código: ')
        codigo = input()
        operacoes.excluir(codigo)
    elif this.opcao == 0:
        print('Obrigado!')
