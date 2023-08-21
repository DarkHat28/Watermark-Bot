import os


class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", None)
	STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	UPDATES_CHANNEL = int(os.environ.get("UPDATES_CHANNEL"))
	DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
	PRESET = os.environ.get("PRESET", "ultrafast")
	OWNER_ID = int(os.environ.get("OWNER_ID"))
	CAPTION = "@Anime_Unfold"
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DATABASE_URL = os.environ.get("DATABASE_URL")
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", False))
	USAGE_WATERMARK_ADDER = """
Hi, I am Unfold Videos Watermark Adder Bot!

**How to Added Watermark to a Video?**
**Usage:** First Send a JPG Image/Logo, then send any Video. Better add watermark to a MP4 or MKV Video.

__Note: I can only process one video at a time. If you have any issues with Adding Watermark to a Video, then please Contact [OWNER](https://t.me/Saitama_AU).__

"""
	PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
"
