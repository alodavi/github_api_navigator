# github_api_navigator

----GITHUB NAVIGATOR----

To run the program:

1) Make sure that you're using python 3
2) Make sure that you've installed all the needed dependencies listed in requirements.txt
3) In particular you only need to install Flask, a python microframework
4) Just run "python application.py" from the command line
5) Open a browser and do GET request to e.g. http://localhost:5000/navigator?search_term=tetris
5) ENJOY!

Notes:

1) Don't move the template.html file to the current directory or to any other directory. Flask automatically looks for it in the templates directory.
2) Since this app doesn't require any authentication you cannot send too many requests in the same time (as written in the documentation of the Github API)
3) By default Flask uses the port 5000


---- SEE THE APP LIVE ON HEROKU! ----
https://github-api-navigator.herokuapp.com/
