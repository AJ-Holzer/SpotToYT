import os


class Config:
    # Spotify
    SPOTIFY_CLIENT_ID: str = str(os.getenv(key="SPOTIFY_CLIENT_ID"))
    SPOTIFY_CLIENT_SECRET: str = str(os.getenv(key="SPOTIFY_CLIENT_SECRET"))
    SPOTIFY_REDIRECT_URI: str = str(os.getenv(key="SPOTIFY_REDIRECT_URI"))
    SPOTIFY_SCOPE: str = "playlist-read-private"


config = Config()
