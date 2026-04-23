#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${GREEN}🚀 УСТАНОВКА ПАКЕТОВ ДЛЯ CLASSIC-BRAWL${NC}"
echo ""

echo -e "${YELLOW}[1/5] Обновление пакетов...${NC}"
pkg update -y && pkg upgrade -y

echo -e "${YELLOW}[2/5] Установка Python и Git...${NC}"
pkg install python git -y

echo -e "${YELLOW}[3/5] Установка TinyDB...${NC}"
pip install tinydb

echo -e "${YELLOW}[4/5] Установка Rust (Cargo)...${NC}"
pkg install rust -y

echo -e "${YELLOW}[5/5] Установка Bore...${NC}"
cargo install bore-cli

echo ""
echo -e "${GREEN}✅ Все пакеты установлены!${NC}"
echo ""
echo -e "${YELLOW}👉 Запуск сервера:${NC}"
echo "   cd ~/Classic-Brawl && python main.py"
echo ""
echo -e "${YELLOW}👉 Запуск Bore туннеля:${NC}"
echo "   ~/.cargo/bin/bore local 9339 --to bore.pub"
