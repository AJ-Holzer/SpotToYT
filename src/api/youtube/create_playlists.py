# ============================== #
#  Copyright (c) AJ-Holzer       #
#  SPDX-License-Identifier: MIT  #
# ============================== #


from ytmusicapi import YTMusic
from ytmusicapi.type_alias import JsonDict
from api.spotify.types import Playlist
from api.youtube.types import YTHeader
from api.youtube.add_tracks import add_tracks
from typing import cast


def create_playlists(playlists: list[Playlist], yt_header: YTHeader) -> None:
    ytmusic: YTMusic = YTMusic(auth=cast(JsonDict, yt_header))

    # Create playlists
    for playlist in playlists:
        # Create playlist and get playlist id
        playlist_id: str | JsonDict = ytmusic.create_playlist(
            title=playlist.name,
            description="",
        )

        # Add tracks
        add_tracks(ytmusic=ytmusic, playlist_id=str(playlist_id), playlist=playlist)
