import os
from dotenv import load_dotenv
from logging.config import dictConfig


load_dotenv()


DISCORD_API_SECRET= os.getenv("DISCORD_API_TOKEN")
#put your discord api token in a .env file
