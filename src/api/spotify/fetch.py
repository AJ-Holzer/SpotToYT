# ============================== #
#  Copyright (c) AJ-Holzer       #
#  SPDX-License-Identifier: MIT  #
# ============================== #


from api.spotify.types import Playlist, Song


def fetch_playlists() -> list[Playlist]:
    return [
        Playlist(
            name="TestName",
            songs=[
                Song(name="song 01"),
                Song(name="song 02"),
            ],
        )
    ]
