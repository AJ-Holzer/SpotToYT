# ============================== #
#  Copyright (c) AJ-Holzer       #
#  SPDX-License-Identifier: MIT  #
# ============================== #


# trunk-ignore(bandit/B404)
import subprocess


def authenticate() -> None:
    # trunk-ignore(bandit/B603)
    # trunk-ignore(bandit/B607)
    subprocess.run("ytmusicapi oauth")
