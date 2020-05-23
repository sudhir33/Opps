class Telephone:
    def __init__(self):
        print("calls")

class Moblie(Telephone):
    def __init__(self):
        super().__init__()
        print("messages")

class Smart(Moblie):
    def __init__(self):
        super().__init__()
        print("games and movies")
        
s1=Smart()
