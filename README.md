# SpotToYT

Converts all public Spotify playlists to YT-Music playlists

> 🚧 Active Development – Regular updates underway.

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

   - Example: `http://127.0.0.1:8888/callback`
   - This is where Spotify will send the user after login

6. Select `Web API`

7. Go to [Google Cloud Credentials](https://console.cloud.google.com/apis/credentials)
8. Search for `YouTube Data API v3` in the search bar at the top
9. Click `Enable`
10. Click on `Create credentials`
11. Click on `Create OAuth Client ID`
12. You may need to configure a consent screen:

    1. App Information
       1. Fill in the app name (e.g. "SpotToYT")
       2. Set an user support email (e.g. Your email)
    2. Audience
       1. I chose `External` as my Audience
    3. Contact Information
       1. Now enter your email address
    4. Finish
       1. Now agree to the _Google API services user data policy_
    5. Click on **Create**

13. Click on `Create OAuth client`
14. Now select your application type
15. Click `Create`
16. Copy the **client ID** to the console
17. Copy the **client secret** to the console

18. Save your **Client ID** and **Client Secret** for Spotify and YT-Music in the `.env` file.
    There is an example `.env.example` file provided

19. Now run the `main.py` file. Done!
