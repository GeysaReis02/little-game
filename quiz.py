print("Technology quiz: Seja Bem-Vindo!")
answer_user = input("Vamos começar? (S/N) ")
print(answer_user)

if answer_user != "S":
    quit()

score = 0

print("Então, vamos começar...")

print("Em computação, o que significa a sigla 'GPU'? \n (A)Unidade de Processamento Geral (General Processing Unit) \n (B)Utilitário de Performance de Jogo (Game Performance Utility) \n (C)Unidade de Processamento Gráfico (Graphics Processing Unit) \n (D)Usuário de Poder Global (Global Power User) \n")
answer_01 = input("Resposta: ")

if answer_01 == "C":
    print("Correto!")
    score = score + 1
else: 
    print("Incorreto!")

print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A)Ubisoft \n (B)Activision \n (C)Rockstar Games \n (D)EA \n")
answer_02 = input("Resposta: ")

if answer_02 == "C":
    print("Correto!")
    score = score + 1
else: 
    print("Incorreto!")


print("Qual sistema operacional é utilizado na linha de iPhones da Apple? \n (A)Android \n (B)iOS \n (C)Windows Mobile \n (D)macOS \n")
answer_03 = input("Resposta: ")

if answer_03 == "B":
    print("Correto!")
    score = score + 1
else: 
    print("Incorreto!")


print("Qual jogo aclamado ganhou o prêmio principal de Jogo do Ano (Game of the Year) no The Game Awards 2023? \n (A) The Legend of Zelda: Tears of the Kingdom \n (B)Alan Wake 2 \n (C)Marvel's Spider-Man 2 \n (D)Baldur's Gate 3 \n")
answer_04 = input("Resposta: ")

if answer_04 == "D":
    print("Correto!")
    score = score + 1
else: 
    print("Incorreto!")

print(f"O quiz acabou...Sua pontuação foi: {score}/4")


