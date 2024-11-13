import bcrypt
#instalacao pip install bcrypt no powershell (https://www.youtube.com/watch?v=hNa05wr0DSA)
import getpass
#deixar a senha nao visivel quando ta digitando


usersA = []
users = []
pets = []
agenda = []
import time

def hashSenha(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

while True:
    login = False
#AREA DE LOGIN
    if len(usersA) == 0:
        print(
            "Não há usuarios registrados com esta informaçoes. \nCadastre um novo usuario: ")
        nomeUser = input('Nome para Login: ')
        nomeUser = nomeUser.upper()

        senha = getpass.getpass("Senha: ")
        hashsenha = hashSenha(senha)

        usersA.append([nomeUser, senha, 'A'])
        login = True
        print("Usuario cadastrado com sucesso!")

    else:
        nomeUser = input('Digite o nome do usuario: ')
        senha = input('Digite a sua senha: ')

        for i in range(len(usersA)):
            if nomeUser == usersA[i][0] and senha == usersA[i][1]:
                print("Usuario autenticado.")
                login = True
                break

#MENU PRINCIPAL

    if login:
        while True:
            print('- - - - - Bem-vindo! - - - - - ')
            print(''' 
                1 - Área do Usuário
                2 - Área do Animal
                3 - Área de Serviços
                4 - Área de Agendamento
                5 - Sair
                ''')
#Fim
            opcao = input(
                "Para entrar na área desejada, digite o numero correspondente: ")
#area do user
            if opcao == '1':
                print("- - - - Área do Usuário - - - - ")
                print('''
                       1 - Cadastro de Usuario (APENAS ADM)
                       2 - Atualizar dados
                       3 - Apagar Dados (APENAS ADM)
                       4 - Voltar''')

                opcaouser = input("Escolha uma das opçoes a cima: ")

                if opcaouser == '1':

                    if any(user[2] == 'A' for user in usersA):

                        CadastroNome = input('Digite o seu nome: ')
                        cel = input('Digite o seu numero de telefone/celular: ')
                        email = input('Digite seu email: ')  
                        cep = input('Digite seu cep: ')
                        Sexo = input('Digite seu sexo: ')

                        while True:
                            #verificaçao cpf
                            cpf = input('Digite seu cpf(xxx.xxx.xxx-xx): ')
                            tam = 14
                            f = True
                            if(len(cpf)!= tam):
                                f = False
                            elif((cpf[3] !=".") or (cpf[7] !=".") or (cpf [-3] != "-")):
                                f = False
                            else:

                                for i in range (tam):
                                    if((i !=3) and (i !=7) and (i !=11)):
                                        c = cpf[i]
                                        if(not c.isdigit()):
                                            f = False
                            if (f):
                                print("cpf valido!")
                                break
                            else:
                                print('cpf invalido')

                            #video do caba caso eu esqueça de algo(https://www.youtube.com/watch?v=s7m1aVgNULA)



                        users.append(
                            [CadastroNome, cel, email, cep, Sexo, cpf])

                        print('Novo usuario cadastrado com sucesso!')
                    else:
                        print('apenas ADMs podem fazer isso')

                elif opcaouser == '2':

                    Atualizarnome = input(
                            'digite o nome de usuario que deseja alterar: ')

                    for user in users:
                        if user[0] == Atualizarnome:
                            print('- - - - altera os dados do usuario - - - -')
                            user[1] = input('Novo numero telefone/celular: ')
                            user[2] = input('Novo Email: ')
                            user[3] = input('novo cep: ')
                            user[4] = input('Novo sexo: ')
                            user[5] = input('Novo cpf: ')

                            print('Dados atualizados!')

                            break
                    else:
                            print('usuario nao encontrado')

                elif opcaouser == '3':

                    if any(user[2] == 'A' for user in usersA):
                        apagar = input('Digite o nome de usuario que deseja excluir: ')
                        
                        for user in users:
                            if user[0] == apagar:
                                users.remove(user)
                                print('excluido com sucesso')

                                break
                        else:
                            print('\nUSUARIO NAO ENCONTRADO!\n')
                    else:
                        print('Apenas ADMs podem fazer isso')


                elif opcao == '4':
                    print('Voltando para o menu principal')
                    break
                else:
                    ('Nao existe essa opção mano')

#area animal

            if opcao == '2':
                print("\n- - - - Área do Animal - - - - \n")
                print('''
                       1 - Cadastro do Animal(APENAS ADM)
                       2 - Atualizar dados do Animal
                       3 - Apagar Dados do Animal (APENAS ADM)
                       5 - Voltar''')
                
                opcaoAnimal = input("Escolha uma das opçoes a cima: ")
                
                if opcaoAnimal == '1':

                    if any(user[2] == 'A' for user in usersA):

                            IDpet = input('Digite o ID do Animal: ')
                            nomePet = input('Digite o nome do Animal: ')
                            categoria = input('Digite a categoria do Animal: ')
                            raça = input('Digite a raça do Animal: ')
                            nascimento = input('Digite a data de nascimento do Animal: ')

                            while True:
                                cpfDono = input('Digite o CPF do Dono do animal: ')
                                tam = 14
                                f = True
                                if(len(cpf)!= tam):
                                    f = False
                                elif((cpf[3] !=".") or (cpf[7] !=".") or (cpf [-3] != "-")):
                                    f = False
                                else:

                                    for i in range (tam):
                                        if((i !=3) and (i !=7) and (i !=11)):
                                            c = cpf[i]
                                            if(not c.isdigit()):
                                                f = False
                                if (f):
                                    print("cpf valido!")
                                    break
                                else:
                                    print('cpf invalido')


                            pets.append([IDpet, nomePet, categoria, raça, nascimento, cpfDono])
                            
                            print('\nAnimal cadastrado com sucesso!\n')

                    else:
                            print('\nApenas ADMs têm permissão para esta ação\n')

                elif opcaoAnimal == '2':

                    atualizarPet = input('Digite o ID do animal que deseja alterar: ')
                        
                    for pet in pets:
                        if pet[0] == atualizarPet:
                            print('- - - - Altere os dados do animal - - - -')
                            pet[1] = input('Novo Nome do animal: ')
                            pet[2] = input('Nova Categoria do animal: ')
                            pet[3] = input('Nova Raça do animal: ')
                            pet[4] = input('Nova Data de Nascimento do animal: ')
                            pet[5] = input('Novo CPF do Dono: ')

                            print('Dados do animal atualizados com sucesso!')
                            break
                        else:
                            print('Animal não encontrado.')

                elif opcaoAnimal == '3':
                    if any(user[2] == 'A' for user in usersA):
                            
                        excluirPet = input('Digite o ID do pet que deseja excluir: ')
                        for pet in pets:
                            if pet[0] == excluirPet:
                                pets.remove(pet)

                                print('Animal excluido com sucesso!')
                                break
                            else:
                                print('animal nao encontrado')
                    else:
                        print('apenas adms tem permissao para esta ação')

                
                elif opcao == '4':
                    print('Voltando para o menu principal...')
                    break  
                else:
                    print('Opção inválida.')


            if opcao == '3':
                print("- - - - Área de Serviços - - - - ")
                print('\n- - - - - - - - Aqui é aonde você encotrará nossos preços e descrição dos serviços! - - - - - - - -')
                print('''
                     1 - Apenas banho
                     2 - Apenas tosa
                     3 - Banho e tosa''')
                
                servicos = input('escolha uma das opçoes para ver mais informações')    
                if servicos == '1':
                    print('Apenas o banho! Garantimos que seu pet irá ficar mais cheiroso do que nunca por apenas \n--------------- \n30R$ para porte pequeno \n60R$ para porte medio \n90R$ para grande porte \n---------------')
                    time.sleep(5)
                    print('\n--------------------------- Caso queira marcar vá a area de agendamento! ---------------------------\n')
                    time.sleep(3)

                if servicos == '2':
                    print('Apenas Tosa! \n--------------- \n35R$ Tosa simples \n50$ Tosa higienica \n65R$ Tosa completa \n--------------- ')
                    time.sleep(5)
                    print('\n--------------------------- Caso queira marcar vá a area de agendamento! ---------------------------\n')
                    time.sleep(3)

                if servicos == '3':
                    print('\n--------------- \n50R$ Banho e tosa simples \n 75R$ Banho e tosa completa \n--------------- \n(+25 DE ACORDO COM O PORTE) \n---------------')
                    time.sleep(5)
                    print('\n--------------------------- Caso queira marcar vá a area de agendamento! ---------------------------\n')
                    time.sleep(3)

            if opcao == '4':
                print("- - - - Área de agendamento - - - - ")
                print(''' 
                      1 - Agendar serviços
                      2 - Ver agendamentos
                      3 - Desmarcar agendamentos
                      4 - Voltar\n ''')
                
                opcaoagendamento = input("Digite a opção desejada: ")
                if opcaoagendamento == '1':
                    print('Marcar agendamento')
                    Data = input('Data Desejada: ')
                    Hora = input('Horario de preferencia: ')
                    Porte = input('Porte do animal: ')
                    servico2 = input('serviço desejado: ')

                    agenda.append({'Data':Data, 'Hora':Hora, 'Porte':Porte, 'Serviço':servico2})

                    print('Agendamento marcado')
                
                elif opcaoagendamento =='2':
                    print('\n- - - - - - Serviços marcadas - - - - - -\n')
                    
                    if len(agenda) == 0:
                            print('Nenhum serviço marcado')
                    else:

                        for i, ServAgenda in enumerate(agenda, 1):
                            time.sleep(2)
                            print(f'Serviço {i}:')
                            print(f'Data: {ServAgenda['Data']}')
                            print(f'Hora: {ServAgenda['Hora']}')
                            print(f'Porte: {ServAgenda['Porte']}')
                            print(f'Serviço: {ServAgenda['Serviço']}\n')

                elif opcaoagendamento =='3':
                    apagar = input('Digite o numero do serviço que deseja excluir: ')
                    xesque = int(apagar) - 1
                    if 0 <= xesque < len(agenda):
                        agenda.pop(xesque)
                        print('Agendamento desmarcado')

                    else:
                        print('Numero invalido')


            if opcao == '5':
                print("- - - - Volte sempre! - - - - ")
                exit()
            
