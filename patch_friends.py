import re

file_path = 'Logic/Player.py'

with open(file_path, 'r') as f:
    content = f.read()

# Находим класс Players и добавляем атрибуты
if 'friends_list' not in content:
    # Добавляем после строки с Brawler_level
    content = content.replace(
        '    Brawler_level = {',
        '    # === ДРУЗЬЯ ===\n    friends_list = []\n    incoming_requests = []\n    outgoing_requests = []\n\n    Brawler_level = {'
    )
    with open(file_path, 'w') as f:
        f.write(content)
    print("✅ Поля друзей добавлены")
else:
    print("⚠️ Поля уже есть")
