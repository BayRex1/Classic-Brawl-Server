from tinydb import TinyDB, Query
import re

file_path = 'Database/DatabaseManager.py'

with open(file_path, 'r') as f:
    content = f.read()

# Добавляем метод updateClubTrophies в класс DataBase
if 'def updateClubTrophies' not in content:
    print("Добавляем метод updateClubTrophies...")
    update_method = '''

    def updateClubTrophies(self):
        """Обновляет общее количество трофеев клуба"""
        if self.player.club_low_id == 0:
            return
        
        from tinydb import TinyDB, Query
        club_db = TinyDB('Database/Club/club.db')
        player_db = TinyDB('Database/Player/data.db')
        query = Query()
        
        club = club_db.search(query.clubID == self.player.club_low_id)
        if not club:
            return
        
        club_info = club[0]['info']
        total_trophies = 0
        
        for member_id in club_info.get('members', {}):
            if member_id != 'totalmembers':
                for player in player_db.all():
                    if str(player['info'].get('lowID', 0)) == str(member_id):
                        total_trophies += player['info'].get('trophies', 0)
                        break
        
        club_info['trophies'] = total_trophies
        club_db.update(club[0], query.clubID == self.player.club_low_id)
        print(f"[CLUB] Трофеи клуба обновлены: {total_trophies}")
'''
    content += update_method

with open(file_path, 'w') as f:
    f.write(content)

print("✅ DatabaseManager.py обновлён")
