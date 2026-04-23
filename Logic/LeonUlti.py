class LeonUlti:
    @staticmethod
    def make_ghost(player):
        """Делает Лиона призраком: проходит по воде и сквозь стены"""
        player.is_ghost = True
        player.ghost_timer = 6  # 6 секунд невидимости
        
        # Отправляем эффект призрака
        print(f"[LEON] {player.name} стал призраком! Может проходить по воде и сквозь стены")
        
    @staticmethod
    def remove_ghost(player):
        """Убирает эффект призрака"""
        player.is_ghost = False
        print(f"[LEON] {player.name} вернулся в нормальное состояние")
