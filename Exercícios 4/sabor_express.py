import os
lista = [{'nome':'Burguer King', 'situaçao': True},
         {'nome':'ticket house', 'situaçao': False},
         {'nome':'Sabor da picanha','situaçao':False}
        ]

def titulo():
    print('-' * 20)
    print('sabor_express')
    print('-' * 20)


def texto_personalizado(texto):
    print('-' * len(texto))
    print(texto)
    print('-' * len(texto))

def menu():
    print('-----------------------------')
    input('Aperte ENTER para ir ao menu:')
    main()

def main():
    titulo()
    opcoes()
    escolher_opcao()

def opcoes():
    print('1 - Cadastrar restaurante\n2 - Listar restaurantes\n3 - Ativar\n4 - Sair\n')

def limpa_tela():
    try:
        os.system('cls')
    except:
        pass
def escolher_opcao():
    try:
        opçao = int(input('Digite uma opção: '))
        limpa_tela()

        if opçao == 1:
            texto_personalizado('Cadastro Restaurante')
            nome_restaurante = input('Digite o nome do restaurante:')
            add_dicionario = {'nome':nome_restaurante,'situaçao':False}
            lista.append(add_dicionario)
            print(f'O restaurante foi cadastrado com sucesso!')
            menu()
        elif opçao == 2:
            texto_personalizado('Lista Restaurantes')
            print('Nome'.ljust(20),'| Situação')
            for dicionario in lista:
                print(dicionario['nome'].ljust(20),'| ', 'ativado' if dicionario['situaçao'] == True  else 'desativado')
            menu()
        elif opçao == 3:
            texto_personalizado('Situação')
            restaurante = str(input('digite o nome do restaurante: '))
            for dicionario in lista:
                if restaurante == dicionario['nome']: #encontrar restaurante
                    dicionario['situaçao'] = not dicionario['situação']
                    dicionario['situaçao'] = True
                    mensagem = 'Restaurante Ativado' if dicionario['situaçao']  else  'Restaurante desativado'
                else:
                    mensagem = True
            if mensagem == True:
                mensagem = f'O restaurante {restaurante} não foi encontrado'
            print(mensagem)  
            menu()
        elif opçao > 4:
            print('opção invalida!')
            menu()          
    except:
        print('opção invalida!')
        menu()
if __name__ == '__main__':
    main()            
