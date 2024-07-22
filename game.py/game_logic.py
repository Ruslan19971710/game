from settings import  *   # Импорт настроек из файла settings.py

class GameLogic:
    def __init__(self):
        self.players = []  # Список игроков
        self.judge = None  # Судья

    def add_player(self, player):
        self.players.append(player)

    def start_game(self):
        # Здесь начинается игра
        pass

    def handle_message(self, message):
        # Обработка сообщения от игрока
        pass

# Создание экземпляра класса GameLogic
game_logic = GameLogic()
