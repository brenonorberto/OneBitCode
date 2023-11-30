teams = {}
done = False

# função para listar times


def print_temas():
    print("Times listados:")
    for i, team in enumerate(teams.values()):
        print(f"{i+1} - {team['name']} ({len(team['players'])} jogadores)")


while not done:
    # Opções no programa
    print("O que você deseja fazer?")
    print("1 - Adicionar um time")
    print("2 - Remover um time")
    print("3 - Listar times")
    print("4 - Adicionar jogador em um time")
    print("5 - Remover jogador de um time")
    print("6 - Listar jogadores de um time")
    print("7 - Sair")

    choice = input(">")
    if choice == '1':
        team_name = input("Digite o nome do time\n ")
        teams[team_name] = {
            "name": team_name,
            "players": []
        }
        print("Time adicionado com sucesso!\n")
    elif choice == '2':
        print_temas()
        team_num = int(input("Qual número do time que deseja remover?\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            del teams[team_name]
            print("Time removido com sucesso!\n")
        else:
            print("Número do time inválido!\n")
    elif choice == '3':
        print_temas()

    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        pass
    elif choice == '7':
        done = True
    else:
        print("Opcão inválida. Tente novamente.")
