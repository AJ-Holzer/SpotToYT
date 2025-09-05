# SpotToYT

Converts all public Spotify playlists to YT-Music playlists

## Installation

1. Run `pip install -r requirements.txt` in terminal
2. Run `playwright install` in terminal to install playwright binaries _(needed for Chromium/Firefox/WebKit)_

   Optional, but if you want to install a specific browser:

   ```bash
   playwright install chromium
   playwright install firefox
   playwright install webkit
   ```

3. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)

4. Click **Create App** -> give it a name (e.g. "Playlist Transfer")

5. Add a Redirect URI:

   - Example: `http://localhost:8888/callback`
   - This is where Spotify will send the user after login

6. Save your **Client ID** and **Client Secret** in the `.env` file.
   There is an example `.env.example` file provided

7. Now run the `main.py` file. Done!
