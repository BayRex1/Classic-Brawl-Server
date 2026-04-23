import random

class DynamikeClone:
    @staticmethod
    def create_clone(player):
        """Создаёт клона Dynamike"""
        clone = {
            'id': random.randint(10000000, 99999999),
            'name': f'Dynamike Clone',
            'brawler_id': 11,  # ID Dynamike
            'hp': 3000,
            'damage': 800,
            'owner_id': player.low_id
        }
        print(f"[CLONE] Dynamike призвал клона! ХП: 3000, Урон: 800")
        return clone
