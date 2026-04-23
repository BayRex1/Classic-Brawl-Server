from Utils.Reader import BSMessageReader
from Packets.Messages.Server.Friend.FriendRequestSentMessage import FriendRequestSentMessage

class AddFriend(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player

    def decode(self):
        self.friend_id = self.read_Vint()
        self.friend_name = self.read_string()

    def process(self):
        print(f"[FRIEND] Friend request from {self.player.name} to {self.friend_name} (ID: {self.friend_id})")
        FriendRequestSentMessage(self.client, self.player, self.friend_name).send()
