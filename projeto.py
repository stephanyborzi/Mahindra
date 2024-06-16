import random

def ValidUser():
    while True:
        indice = -1
        input_usuario_login = input("Usuario: ")
        input_senha_login = input("Senha: ")
        for i in range(len(usuarios)):
            if usuarios[i] == input_usuario_login:
                indice = i
                break
        if indice == -1:
            print("Não te encontramos cadastrado")
            input_cadastro = input("Você gostaria de se cadastrar na nossa plataforma de maneira gratuita? (S/N) ")
            if input_cadastro.upper() == 'S':
                input_usuario_cadastro = input('Crie seu usuário. Digite um nome de usuário válido: ')
                input_senha_cadastro = input('Crie uma senha: ')
                usuarios.append(input_usuario_cadastro)
                senhas.append(input_senha_cadastro)
                print("Cadastro realizado com sucesso! Você ganhou 100 pontos para usar na nossa plataforma. Por favor, faça login.")
            else:
                print('Que pena, talvez uma outra hora!')
                return None  
        elif senhas[indice] != input_senha_login:
            print("Senha inválida")
        else:
            return indice

def modalidades_apostas():
    while True:
        input_escolha_modalidade = input('Escolha a modalidade na qual você quer apostar: ')
        if input_escolha_modalidade not in modalidades:
            print("Não há nenhuma modalidade desse tipo cadastrada. Por favor, escolha outra:")
        else:
            print(f"Você escolheu a modalidade: {input_escolha_modalidade}")
            break

print("-=" * 20)
print('Seja bem-vindo(a) à nossa plataforma')
print("-=" * 20)
usuarios = ['user1', 'user2', 'user3']
senhas = ['1234', '4321', '6789']
pontos = 0
userValido = ValidUser()
if userValido is not None:
    print(f"Bem-vindo, {usuarios[userValido]}!")
    pontos += 100
    recomendar = input('Gostaria de recomendar nossa plataforma para um amigo e ganhar mais 200 pontos para usar nas suas apostas? (S/N) ')
    if recomendar.upper() == 'S':
        pontos += 200
        print('Muito obrigado por nos recomendar para um amigo!')
    else:
        print('Que pena, talvez uma outra hora!')
    print(f"Você tem um total de {pontos} pontos.")

    modalidades = [
        'Vencedor da prova', 'Vencedor Top 3', 'Volta mais rápida', 'Head to head', 
        'Time vencedor da temporada', 'Batidas', 'Desistência', 'Pit Stop', 
        'Troca de liderança', 'Piloto mais arrojado', 'Voltas dadas pelo líder nos últimos colocados'
    ]

    print('Essas são nossas modalidades de aposta:')
    for modalidade in modalidades:
        print(f"  - {modalidade}")

    modalidades_apostas()

    while True:
        while True:
            try:
                qtd_aposta = int(input('Quanto você quer apostar?: '))
                if qtd_aposta > pontos:
                    print(f'Você não tem pontos suficientes para fazer essa aposta. Escolha um valor compatível com seu saldo ({pontos} pontos).')
                else:
                    break
            except ValueError:
                print("Por favor, insira um número válido.")
        
        carros = ['carro1', 'carro2', 'carro3', 'carro4']
        while True:
            escolha_carro = input('Em qual carro você quer apostar? (carro1, carro2, carro3, carro4): ')
            if escolha_carro in carros:
                break
            else:
                print('Opção inválida. Escolha entre carro1, carro2, carro3 ou carro4.')

        vencedor = random.choice(carros)

        print(f"O vencedor é: {vencedor}")
        if escolha_carro == vencedor:
            pontos += qtd_aposta
            print('Você ganhou a aposta!')
        else:
            pontos -= qtd_aposta
            print('Você perdeu a aposta.')

        print(f"Agora você tem um total de {pontos} pontos.")

        if pontos <= 0:
            print('Você não tem mais pontos para apostar')
            break

        apostar_novamente = input('Gostaria de apostar novamente? (S/N): ').upper()
        if apostar_novamente != "S":
            break

    print('Muito obrigado por ter jogado com a gente!')
else:
    print('Obrigado por visitar nossa plataforma. Até a próxima!')
