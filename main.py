from datetime import datetime
import unidecode

nome = input("Nome: ")
print("firstbps (1)")
print("firstdecision (2)")
choice = int(input())
nome = nome.casefold()
nome = unidecode.unidecode(nome)
primeiro_espaco = nome.index(' ')

primeiro_nome = nome[0:primeiro_espaco]
ultimo_espaco = nome.rfind(' ')
sobrenome = nome[ultimo_espaco + 1::]

user_name = f"{primeiro_nome}.{sobrenome}"
user_email_firstbps = f"{user_name}@firstbps.com.br"
user_email_firstdecision = f"{user_name}@firstdecision.com.br"
dia = datetime.today().strftime('%d')
ano = datetime.today().strftime('%Y')
fd = 'i' if sobrenome[0] == 'i' else sobrenome[0].capitalize()
ld = 'L' if primeiro_nome[0] == 'l' else primeiro_nome[0].casefold()
senha = f"{fd}{dia}{ld}@{ano}"

if choice == 1:
    contrato = input("Projeto: ")

    print()
    print()

    print(nome.title())
    print("===================================")
    print("Seu dominio de rede firstdecision.local possui um novo usuário.")
    print("Nome: ", nome.title())
    print("usuário: ", user_name)
    print("Senha: ", senha)
    print()
    print("Seu dominio de email firstbps.com.br possui um novo usuário.")
    print("Nome: ", nome.title())
    print("usuário: ", user_email_firstbps)
    print("Senha: ", senha)

    print()
    print()

    print("Projeto: ", contrato)

if choice == 2:
    print()
    print()

    print(nome.title())
    print("===================================")
    print("Seu dominio de rede firstdecision.local possui um novo usuário.")
    print("Nome: ", nome.title())
    print("usuário: ", user_name)
    print("Senha: ", senha)
    print()
    print("Seu dominio de email firstdecision.com.br possui um novo usuário.")
    print("Nome: ", nome.title())
    print("usuário: ", user_email_firstdecision)
    print("Senha: ", senha)

    print()
    print()

