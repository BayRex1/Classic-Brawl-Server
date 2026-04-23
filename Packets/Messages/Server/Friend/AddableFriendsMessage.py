from Utils.Writer import Writer

class AddableFriendsMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20104
        self.player = player

    def encode(self):
        self.writeVint(0)
