# ============================== #
#  Copyright (c) AJ-Holzer       #
#  SPDX-License-Identifier: MIT  #
# ============================== #


from dataclasses import dataclass


@dataclass
class Artist:
    name: str
    id: str


@dataclass
class Track:
    name: str
    id: str
    artist: Artist
    duration: int


@dataclass
class Playlist:
    name: str
    id: str
    description: str
    tracks: list[Track]
