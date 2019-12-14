from games.secret_santa.SecretSanta import SecretSanta


def main():
    # Main menu
    game_type = input("\nWould you like to play:\n1. Secret Santa\n\n")
    while (game_type != '1'):
        print("That response was invalid. Please choose from the options")
        game_type = input("\nWould you like to play:\n1. Secret Santa\n\n")
    game_type = int(game_type)

    # Menu Logic
    if (game_type == 1):
        game = SecretSanta()

    game.start()


if __name__ == "__main__":
    main()
    