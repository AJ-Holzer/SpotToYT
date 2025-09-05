# ============================== #
#  Copyright (c) AJ-Holzer       #
#  SPDX-License-Identifier: MIT  #
# ============================== #


from ytmusicapi import YTMusic
from ytmusicapi.type_alias import JsonList
from api.spotify.types import Playlist


def add_tracks(
    ytmusic: YTMusic,
    playlist_id: str,
    playlist: Playlist,
) -> None:
    for song in playlist.songs:
        search_results: JsonList = ytmusic.search(query=song.name, filter="songs")

        # Add first song if songs found
        if search_results:
            ytmusic.add_playlist_items(
                playlistId=playlist_id,
                videoIds=[search_results[0]["videoId"]],
            )
