# ============================== #
#  Copyright (c) AJ-Holzer       #
#  SPDX-License-Identifier: MIT  #
# ============================== #


from api.youtube.auth import get_ytmusic_headers
from api.youtube.create_playlists import create_playlists
from api.spotify.types import Playlist
from api.youtube.types import YTHeader


from api.spotify.fetch import fetch_playlists
# from api.spotify.types import Playlist, Song


def main() -> None:
    # Login to YT-Music
    yt_header: YTHeader = get_ytmusic_headers()

    # Fetch Spotify playlists
    playlists: list[Playlist] = fetch_playlists()

    # Create playlists
    create_playlists(playlists=playlists, yt_header=yt_header)


if __name__ == "__main__":
    main()
