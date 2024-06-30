import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21658697"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "de14ead808f57b3825f74a8be57868c5")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sharmaharry34105:sahilkhan8000@cluster9.bmsgwvp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster9")
