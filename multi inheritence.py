class Land_line:
    def __init__(self):
        print("calls")


class Moblie(Land_line):
    def __init__(self):
        super().__init__()
        print("Messages and basic games")


class Smart(Moblie):
    def __init__(self):
        super().__init__()
        print("movies, advanced games")


s1=Smart()
