from dsplayer import event
from src.utils.storage import player_storage

@event('on_disconnect')
async def on_disconnect(event_data: dict):
    print(player_storage.get_bot())
    text_id: int = event_data['text_id']
    bot = player_storage.get_bot()
    if bot is None:
        return
    channel = bot.get_channel(text_id)
    if channel is None:
        return
    await channel.send("Disconnected from the voice channel.")