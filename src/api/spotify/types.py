# ============================== #
#  Copyright (c) AJ-Holzer       #
#  SPDX-License-Identifier: MIT  #
# ============================== #


from dataclasses import dataclass


@dataclass
class Song:
    name: str


@dataclass
class Playlist:
    name: str
    songs: list[Song]
