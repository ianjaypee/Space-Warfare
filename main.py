from game import Game


class SpaceWarfare(Game):
    def __init__(self):
        super(SpaceWarfare, self).__init__()


def main():
    game = SpaceWarfare()
    game.run()


if __name__ == '__main__': 
    main()  