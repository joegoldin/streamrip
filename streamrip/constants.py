import os
from pathlib import Path

import click
import mutagen.id3 as id3

APPNAME = "streamrip"

CACHE_DIR = click.get_app_dir(APPNAME)
CONFIG_DIR = click.get_app_dir(APPNAME)
CONFIG_PATH = os.path.join(CONFIG_DIR, "config.yaml")
LOG_DIR = click.get_app_dir(APPNAME)
DB_PATH = os.path.join(LOG_DIR, "downloads.db")

DOWNLOADS_DIR = os.path.join(Path.home(), "StreamripDownloads")

AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"

TIDAL_COVER_URL = "https://resources.tidal.com/images/{uuid}/{width}x{height}.jpg"

EXT = {
    0: ".mp3",
    1: ".mp3",
    2: ".flac",
    3: ".flac",
    4: ".flac",
}

QUALITY_DESC = {
    0: "128kbps",
    1: "320kbps",
    2: "16bit/44.1kHz",
    3: "24bit/96kHz",
    4: "24bit/192kHz",
}


QOBUZ_FEATURED_KEYS = (
    "most-streamed",
    "recent-releases",
    "best-sellers",
    "press-awards",
    "ideal-discography",
    "editor-picks",
    "most-featured",
    "qobuzissims",
    "new-releases",
    "new-releases-full",
    "harmonia-mundi",
    "universal-classic",
    "universal-jazz",
    "universal-jeunesse",
    "universal-chanson",
)

__MP4_KEYS = (
    "\xa9nam",
    "\xa9ART",
    "\xa9alb",
    r"aART",
    "\xa9day",
    "\xa9day",
    "\xa9cmt",
    "desc",
    "purd",
    "\xa9grp",
    "\xa9gen",
    "\xa9lyr",
    "\xa9too",
    "cprt",
    "cpil",
    "covr",
    "trkn",
    "disk",
    None,
    None,
)

__MP3_KEYS = (
    id3.TIT2,
    id3.TPE1,
    id3.TALB,
    id3.TPE2,
    id3.TCOM,
    id3.TYER,
    id3.COMM,
    id3.TT1,
    id3.TT1,
    id3.GP1,
    id3.TCON,
    id3.USLT,
    id3.TEN,
    id3.TCOP,
    id3.TCMP,
    None,
    id3.TRCK,
    id3.TPOS,
    None,
    None,
)

__METADATA_TYPES = (
    "title",
    "artist",
    "album",
    "albumartist",
    "composer",
    "year",
    "comment",
    "description",
    "purchase_date",
    "grouping",
    "genre",
    "lyrics",
    "encoder",
    "copyright",
    "compilation",
    "cover",
    "tracknumber",
    "discnumber",
    "tracktotal",
    "disctotal",
)


FLAC_KEY = {v: v.upper() for v in __METADATA_TYPES}
MP4_KEY = dict(zip(__METADATA_TYPES, __MP4_KEYS))
MP3_KEY = dict(zip(__METADATA_TYPES, __MP3_KEYS))

COPYRIGHT = "\u2117"
PHON_COPYRIGHT = "\u00a9"
FLAC_MAX_BLOCKSIZE = 16777215  # 16.7 MB

# TODO: give these more descriptive names
TRACK_KEYS = ("tracknumber", "artist", "albumartist", "composer", "title")
ALBUM_KEYS = ("albumartist", "title", "year", "bit_depth", "sampling_rate", "container")
# TODO: rename these to DEFAULT_FOLDER_FORMAT etc
FOLDER_FORMAT = (
    "{albumartist} - {title} ({year}) [{container}] [{bit_depth}B-{sampling_rate}kHz]"
)
TRACK_FORMAT = "{tracknumber}. {artist} - {title}"

URL_REGEX = (
    r"https:\/\/(?:www|open|play|listen)?\.?(qobuz|tidal|deezer)\.com(?:(?:\/(track|playlist|album|"
    r"artist|label))|(?:\/[-\w]+?))+\/([-\w]+)"
)
SOUNDCLOUD_URL_REGEX = r"https://soundcloud.com/[-\w:/]+"
SOUNDCLOUD_CLIENT_ID = "a3e059563d7fd3372b49b37f00a00bcf"


TIDAL_MAX_Q = 7
DEEZER_MAX_Q = 6
AVAILABLE_QUALITY_IDS = (0, 1, 2, 3, 4)
MEDIA_TYPES = ("track", "album", "artist", "label", "playlist")
