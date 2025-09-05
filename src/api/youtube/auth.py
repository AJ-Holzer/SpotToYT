# ============================== #
#  Copyright (c) AJ-Holzer       #
#  SPDX-License-Identifier: MIT  #
# ============================== #


import json

from typing import Any
from playwright.sync_api import sync_playwright


def get_ytmusic_headers() -> dict[str, Any]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # open a real browser
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://music.youtube.com")

        print("👉 Please log in to YouTube Music in the browser window.")
        page.wait_for_url("https://music.youtube.com/*", timeout=120_000)

        cookies = context.cookies()
        browser.close()

        # Save headers.json
        headers = {"cookie": "; ".join([f"{c['name']}={c['value']}" for c in cookies])}

        with open("yt_headers_auth.json", "w") as f:
            json.dump(headers, f, indent=2)

        return headers
