# ============================== #
#  Copyright (c) AJ-Holzer       #
#  SPDX-License-Identifier: MIT  #
# ============================== #


from api.youtube.auth import get_ytmusic_headers
from typing import Any

# from api.spotify.fetch import fetch_playlists
# from api.spotify.types import Playlist, Song


def main() -> None:
    # Login to YT-Music
    yt_headers: dict[str, Any] = get_ytmusic_headers()

    # playlists: list[Playlist] = fetch_playlists()
    # print(playlists)


if __name__ == "__main__":
    main()
