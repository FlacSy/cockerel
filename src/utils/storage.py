from typing import Dict
from dsplayer import Player


class PlayerStorage:
    def __init__(self):
        self.players: Dict[int, Player] = {}

    def get_player(self, guild_id: int) -> Player | None:
        if guild_id not in self.players:
            return None
        return self.players[guild_id]
    
    def remove_player(self, guild_id: int) -> None:
        if guild_id in self.players:
            del self.players[guild_id]

    def clear_players(self) -> None:
        self.players.clear()