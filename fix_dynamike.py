import re

file_path = 'GameAssets/csv_logic/characters.csv'

with open(file_path, 'r') as f:
    content = f.read()

# Ищем строку Dynamike
lines = content.split('\n')
new_lines = []
found = False

for line in lines:
    if 'TntDude' in line and 'dynamike' in line:
        found = True
        parts = line.split(',')
        # Колонки: 0=Name, 7=Speed, 8=Health, 13=Damage
        print(f"Найдена строка: {line[:100]}...")
        print(f"Было: Health={parts[8] if len(parts)>8 else '?'}, Damage={parts[13] if len(parts)>13 else '?'}")
        
        # Меняем здоровье на 5000
        if len(parts) > 8:
            parts[8] = '5000'
        # Меняем урон на 2000
        if len(parts) > 13:
            parts[13] = '2000'
        # Меняем урон супера на 3000
        if len(parts) > 14:
            parts[14] = '3000'
        
        line = ','.join(parts)
        print(f"Стало: Health={parts[8] if len(parts)>8 else '?'}, Damage={parts[13] if len(parts)>13 else '?'}")
    new_lines.append(line)

if not found:
    print("❌ Строка с Dynamike не найдена!")

with open(file_path, 'w') as f:
    f.write('\n'.join(new_lines))

print("✅ Готово!")
