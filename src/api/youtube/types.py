# ============================== #
#  Copyright (c) AJ-Holzer       #
#  SPDX-License-Identifier: MIT  #
# ============================== #


from typing import TypedDict


class SearchQueryResult(TypedDict):
    videoId: str


SearchQueryResults = list[SearchQueryResult]
