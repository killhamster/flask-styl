# flask-styl
A fork of the implementation of the [STYL](https://github.com/Atienon/styl-recommendations) script with Flask.

Enter the title of one song and get a list of ten recommendations based on that one song.

Setup:

You need to create a .env file with your SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET from Spotify. An extra SECRET_KEY is required so a CRSF token can be generated for the form.
