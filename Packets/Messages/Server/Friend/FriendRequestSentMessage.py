from Utils.Writer import Writer

class FriendRequestSentMessage(Writer):
    def __init__(self, client, player, friend_name):
        super().__init__(client)
        self.id = 20103
        self.player = player
        self.friend_name = friend_name

    def encode(self):
        self.writeVint(0)
        self.writeVint(0)
        self.writeString(self.friend_name)
