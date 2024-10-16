import os
import logging
import disnake
import importlib
from disnake.ext import commands
from dotenv import load_dotenv
from src.utils.storage import player_storage
from dsplayer import PluginLoader

plugin_loader = PluginLoader()
plugin_loader.debug_mode = True

def main():
    """
    Main function to run the bot
    :return: None
    :rtype: NoneType
    """
    logging.basicConfig(level=logging.INFO)

    load_dotenv()

    TOKEN = os.environ.get("DS_TOKEN")
    
    intents = disnake.Intents.all()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    logging.info("Bot is starting...")

    for filename in os.listdir("./src/cogs/"):
        if filename.endswith(".py") and filename != '__init__.py':
            try:
                bot.load_extension(f"src.cogs.{filename[:-3]}")
                logging.info(f"Loaded extension {filename}")
            except Exception as e:
                logging.error(f"Failed to load extension {filename}: {e}")

    for filename in os.listdir("./src/events/"):
        if filename.endswith(".py") and filename != '__init__.py':
            try:
                importlib.import_module(f"src.events.{filename[:-3]}")
                logging.info(f"Loaded event {filename}")
            except Exception as e:
                logging.error(f"Failed to load extension {filename}: {e}")

    logging.info("Bot is running...")
    
    @bot.event
    async def on_ready():
        logging.info(f"Bot is ready. Logged in as {bot.user}")
        player_storage.set_bot(bot)
        
    logging.info("Bot is running...")
    bot.run(TOKEN)

if __name__ == "__main__":
    main()