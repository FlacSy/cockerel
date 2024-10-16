from typing import Dict
from dsplayer import Player
from disnake.ext.commands import Bot

class PlayerStorage:
    def __init__(self):
        self.players: Dict[int, Player] = {}
        self.player_message_id: int | None = None
        self.bot: Bot | None = None
        
    def get_player(self, guild_id: int) -> Player | None:
        if guild_id not in self.players:
            return None
        return self.players[guild_id]
    
    def remove_player(self, guild_id: int) -> None:
        if guild_id in self.players:
            del self.players[guild_id]

    def clear_players(self) -> None:
        self.players.clear()

    def set_player_message_id(self, message_id: int) -> None:
        self.player_message_id = message_id

    def get_player_message_id(self) -> int | None:
        return self.player_message_id
    
    def clear_player_message_id(self) -> None:
        self.player_message_id = None

    def set_bot(self, bot) -> None:
        self.bot = bot

    def get_bot(self) -> Bot | None:
        return self.bot
    
player_storage = PlayerStorage()