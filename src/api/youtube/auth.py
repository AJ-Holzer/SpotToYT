# ============================== #
#  Copyright (c) AJ-Holzer       #
#  SPDX-License-Identifier: MIT  #
# ============================== #


import json

from playwright.sync_api import sync_playwright, Page, BrowserContext, Browser, Cookie
from api.youtube.types import YTHeader


def get_ytmusic_headers() -> YTHeader:
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(headless=False)  # open a real browser
        context: BrowserContext = browser.new_context()
        page: Page = context.new_page()
        page.goto("https://music.youtube.com")

        print("👉 Please log in to YouTube Music in the browser window.")
        page.wait_for_url(url="https://music.youtube.com/*", timeout=120_000)

        cookies: list[Cookie] = context.cookies()
        browser.close()

        # Save headers.json
        headers: YTHeader = {
            "cookie": "; ".join([f"{c['name']}={c['value']}" for c in cookies])  # type: ignore
        }

        with open("yt_header_auth.json", "w") as f:
            json.dump(headers, f, indent=2)

        return headers
