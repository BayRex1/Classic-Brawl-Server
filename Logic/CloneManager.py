import random

class CloneManager:
    @staticmethod
    def create_clone(player, map_id, x, y):
        """Создаёт клона Dynamike"""
        clone = {
            'id': random.randint(1000000, 9999999),
            'name': f'Clone of {player.name}',
            'brawler_id': player.brawler_id,
            'hp': 1000,
            'damage': 500,
            'x': x,
            'y': y,
            'map_id': map_id,
            'owner_id': player.low_id
        }
        print(f"[CLONE] Создан клон для {player.name}")
        return clone
