# ============================== #
#  Copyright (c) AJ-Holzer       #
#  SPDX-License-Identifier: MIT  #
# ============================== #


import spotipy  # type: ignore [import-untyped

from spotipy.oauth2 import SpotifyOAuth  # type: ignore [import-untyped]
from api.spotify.types import Playlist, Song
from config import config
from typing import Any, Optional


def fetch_playlists() -> list[Playlist]:
    # Initialize spotipy
    sp: spotipy.Spotify = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=config.SPOTIFY_CLIENT_ID,
            client_secret=config.SPOTIFY_CLIENT_SECRET,
            redirect_uri=config.SPOTIFY_REDIRECT_URI,
            scope=config.SPOTIFY_SCOPE,
        )
    )

    # Define playlists
    playlists: list[Playlist] = []

    # Get playlists
    spotify_playlists: Optional[dict[str, Any]] = sp.current_user_playlists()

    # Return empty list if no playlists found
    if spotify_playlists is None:
        return []

    for playlist in spotify_playlists["items"]:
        print(f"Processing playlist '{playlist['name']}' from Spotify...")

        # Get playlist data
        spotify_playlist_data: Optional[dict[str, Any]] = sp.playlist_items(  # type: ignore
            playlist["id"]
        )

        # Skip if no playlist data
        if spotify_playlist_data is None:
            continue

        # Get songs
        songs: list[Song] = [
            Song(name=item["track"]["name"]) for item in spotify_playlist_data["items"]
        ]

        playlists.append(Playlist(name=playlist["name"], songs=songs))

    return []
