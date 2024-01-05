import os
from dotenv import load_dotenv
from logging.config import dictConfig


load_dotenv()


DISCORD_API_SECRET= os.getenv("DISCORD_API_TOKEN")
