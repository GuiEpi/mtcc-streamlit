from logging.handlers import RotatingFileHandler
from collections import OrderedDict
import configparser
import logging


CONFIG_PATH = "./config.ini"
CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_PATH)

MTCC_LINK = "https://github.com/GuiEpi/mtcc"

# nfo
NFO_NAME = "mtcc Nfo Builder"
NFO_VERSION = "1.0.0"
NFO_RIPPER = CONFIG.get("nfo", "ripper")
NFO_UPLOADER = CONFIG.get("nfo", "uploader")

# pres
BANNERS_PATH = "./banners"

PRES_YGG_LINK = CONFIG.get("pres", "ygg_link")
PRES_YGG_TAG = CONFIG.get("pres", "ygg_tag")
PRES_DEFAULT_BANNER = CONFIG.get("pres", "default_banners")
PRES_BANNERS_LINK = "https://raw.githubusercontent.com/GuiEpi/mtcc/master/banners"
PRES_BANNERS_FILES_NAME = (
    "informations.png",
    "track_details.png",
    "technical_details.png",
    "download.png",
    "my_torrents.png",
    "mtcc_pres.png",
)

PRES_BANNERS = {
    "play_banners_purple": f"{PRES_BANNERS_LINK}/play_banners_purple",
    "play_banners_orange": f"{PRES_BANNERS_LINK}/play_banners_orange",
    "kk_banners_blue": f"{PRES_BANNERS_LINK}/kk_banners_blue",
    "kk_banners_orange": f"{PRES_BANNERS_LINK}/kk_banners_orange",
}

PRES_BANNERS = OrderedDict(
    [
        ("play_banners_purple", f"{PRES_BANNERS_LINK}/play_banners_purple"),
        ("play_banners_orange", f"{PRES_BANNERS_LINK}/play_banners_orange"),
        ("kk_banners_blue", f"{PRES_BANNERS_LINK}/kk_banners_blue"),
        ("kk_banners_orange", f"{PRES_BANNERS_LINK}/kk_banners_orange"),
    ]
)
if PRES_DEFAULT_BANNER in PRES_BANNERS:
    PRES_BANNERS.move_to_end(PRES_DEFAULT_BANNER, last=False)

# logging
formatter = logging.Formatter(
    "%(asctime)s %(module)9s:%(lineno)-4s %(levelname)-9s %(message)s"
)
logbytes = 512000
logbackups = 3

def setup_logger(name: str, level=logging.INFO):
    handler = logging.StreamHandler()
    handler = RotatingFileHandler(f"mtcc.log", "a", logbytes, logbackups)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
