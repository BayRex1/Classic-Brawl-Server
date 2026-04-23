import random

class CrowUlti:
    @staticmethod
    def modify_ulti(player):
        """Изменяет ульту Ворона"""
        # Увеличиваем длительность ульты с 1 до 5 секунд
        player.ulti_duration = 5
        
        # Урон при приземлении
        player.ulti_landing_damage = 5000
        
        print(f"[CROW] {player.name} активировал ульту! Длительность: 5 сек, урон: 5000")
    
    @staticmethod
    def apply_landing_damage(player, enemy):
        """Наносит урон врагу при приземлении"""
        if hasattr(player, 'ulti_landing_damage'):
            damage = player.ulti_landing_damage
            # Здесь должна быть логика нанесения урона врагу
            print(f"[CROW] {player.name} нанёс {damage} урона перьями!")
            return damage
        return 0
