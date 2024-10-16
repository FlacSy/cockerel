import disnake
from disnake.ext import commands
from dsplayer import Player

from main import player_storage, plugin_loader

class PlayCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(description="Play a song")
    async def play(self, inter: disnake.ApplicationCommandInteraction, song: str):
        await inter.response.defer()
        player = player_storage.get_player(inter.guild.id)
        
        if player is None:
            if inter.user.voice is None:
                await inter.followup.send("You need to be in a voice channel to play music.")
                return
            
            player = Player(
                voice_id=inter.user.voice.channel.id,
                text_id=inter.channel.id,
                inter=inter,
                plugin_loader=plugin_loader,
                FFMPEG_OPTIONS={
                    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                    'options': '-vn'},
            )
            player_storage.players[inter.guild.id] = player
        try:
            try:
                await player.connect()
            except:
                pass 
            track = await player.play(song)
            if track is None:
                await inter.followup.send("Could not find the track.")
                return
            
            await inter.followup.send(f"Now playing: {track['title']}")
        except Exception as e:
            await inter.followup.send(f"An error occurred while trying to play the track: {str(e)}")

def setup(bot):
    bot.add_cog(PlayCommand(bot))
