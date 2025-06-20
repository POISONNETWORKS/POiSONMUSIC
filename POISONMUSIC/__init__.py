from POISONMUSIC.core.bot import POISON
from POISONMUSIC.core.dir import dirr
from POISONMUSIC.core.git import git
from POISONMUSIC.core.userbot import Userbot
from POISONMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = POISON()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
