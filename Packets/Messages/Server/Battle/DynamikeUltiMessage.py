from Utils.Writer import Writer
from Logic.DynamikeClone import DynamikeClone

class DynamikeUltiMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        clone = DynamikeClone.create_clone(self.player)
        
        self.writeVint(1)  # количество клонов
        self.writeVint(clone['id'])
        self.writeVint(clone['brawler_id'])
        self.writeVint(clone['hp'])
        self.writeVint(0)  # x позиция
        self.writeVint(0)  # y позиция
        self.writeVint(clone['damage'])
        self.writeVint(self.player.low_id)  # owner id
