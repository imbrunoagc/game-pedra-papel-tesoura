import random

# Pontuação do jogador
user_points = 0

# Pontuação da máquina
computer_points = 0

# Opções da máquina
options = ["r", "t", "p"]

# Enquanto a condição for verdadeira, executar o loop-While.
while True:
    user_choice = input("Escolha R(Pedra - Rocha)/T(Tesoura)/P(Papel) ou Q para sair. ").lower()
    
    # Se o usuário inserir q ou Q - Saida do jogo
    if user_choice == "q":
        break
    
    if user_choice not in options:
        print("Erro: valor informado não está dentro da lista de opções. Favor execute novamente e informe uma opção válida!")
        continue
    # 0=Pedra, 1=Tesoura, 2=Papel
    computer_choice = random.randint(0, 2)
    computer_option = options[computer_choice]
    
    print(" O Computador escolheu " + computer_option)
    
    if user_choice == computer_option:
        print("Empate!")
    elif user_choice == "r" and computer_option == "t":
        print("Você ganhou!")
        user_points = user_points + 1
        
    elif user_choice == "p" and computer_option == "r":
        print("Você ganhou!")
        user_points = user_points + 1
        
    elif user_choice == "t" and computer_option == "p":
        print("Você ganhou!")
        user_points = user_points + 1
    
    else:
        "Você perdeu"
        computer_points = computer_points + 1
    
print("Sua pontuação: " + str(user_points))
print("Pontuação do computador: " + str(computer_points))

if computer_points > user_points:
    print("Derrota!!!")
elif computer_points == user_points:
    print("Empate!!!")
else:
    print("Vitória!!!")
