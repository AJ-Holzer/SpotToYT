# ============================== #
#  Copyright (c) AJ-Holzer       #
#  SPDX-License-Identifier: MIT  #
# ============================== #


from ytmusicapi import YTMusic, OAuthCredentials
from config import config
from api.classes import Playlist, Track
from typing import Optional, cast
from api.youtube.types import SearchQueryResults


class YTMService:
    def __init__(self) -> None:
        self._ytmusic: YTMusic = YTMusic(
            auth=config.YTM_OAUTH_FILE_PATH,
            oauth_credentials=OAuthCredentials(
                client_id=config.YTM_CLIENT_ID,
                client_secret=config.YTM_CLIENT_SECRET,
            ),
        )

    def create_playlist(self, name: str, description: str) -> Optional[Playlist]:
        try:
            playlist_id: str = str(
                self._ytmusic.create_playlist(title=name, description=description)
            )
            return Playlist(
                name=name, id=playlist_id, description=description, tracks=[]
            )
        except Exception as e:
            print(f"Exception has occurred while creating YouTubeMusic playlist: {e}")
            return None

    def search_track(self, query: Track) -> Optional[str]:
        try:
            search_query: str = f"{query.name} by {query.artist.name}"
            api_search_results: SearchQueryResults = cast(
                SearchQueryResults,
                self._ytmusic.search(query=search_query, filter="songs"),
            )

            return (
                None
                if len(api_search_results) == 0
                else api_search_results[0]["videoId"]
            )
        except Exception as e:
            print(
                f"Exception has occurred while searching for the track '{query.name}' by '{query.artist.name}': {e}"
            )
            return None

    def delete_playlist(self, playlist_id: str) -> None:
        try:
            self._ytmusic.delete_playlist(playlistId=playlist_id)
        except Exception as e:
            print(
                f"Exception has occurred while deleting YouTubeMusic playlist with id '{playlist_id}': {e}"
            )

    def add_songs_to_playlist(self, tracks: list[Track], playlist: Playlist) -> None:
        try:
            track_ids: list[str] = []

            # Get video ids
            for track in tracks:
                if track_id := self.search_track(query=track):
                    track_ids.append(track_id)

            self._ytmusic.add_playlist_items(playlistId=playlist.id, videoIds=track_ids)
        except Exception as e:
            print(f"Exception has occurred: {e}")
