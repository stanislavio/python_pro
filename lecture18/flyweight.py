class Player:
    def __init__(self, name, team_color):
        self.name = name
        self.team_color = team_color


class PlayerFactory:
    players = {}

    def get_player(self, name, team_color):
        if (name, team_color) not in self.players:
            self.players[(name, team_color)] = Player(name, team_color)
        return self.players[(name, team_color)]


factory = PlayerFactory()

player1 = factory.get_player("John", "Red")
player2 = factory.get_player("Jane", "Blue")
player3 = factory.get_player("John", "Red")  # Використовується існуючий об'єкт

print(player1 is player2)  # Виведе: False
print(player1 is player3)  # Виведе: True
