from games.secret_santa.SecretSanta import SecretSanta
from games.white_elephant.WhiteElephant import WhiteElephant


def main():
    # Main menu
    game_type = input("\nWould you like to play:\n1. Secret Santa\n2. White Elephant\n\n")
    while (game_type != '1') and (game_type != '2'):
        print("That response was invalid. Please choose from the options")
        game_type = input("\nWould you like to play:\n1. Secret Santa\n2. White Elephant\n\n")
    game_type = int(game_type)

    # Menu Logic
    if (game_type == 1):
        game = SecretSanta()
    elif (game_type == 2):
        game = WhiteElephant()

    game.start()


if __name__ == "__main__":
    main()
