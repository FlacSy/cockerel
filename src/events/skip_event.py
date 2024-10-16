from dsplayer import event
from src.utils.storage import player_storage

@event('on_skip')
async def on_skip(event_data: dict):
    text_id: int = event_data['text_id']
    bot = player_storage.get_bot()
    if bot is None:
        return
    channel = bot.get_channel(text_id)
    if channel is None:
        return
    await channel.send("Skipping the current track.")