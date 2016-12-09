'''
MIT License

Copyright (c) 2016  Aloisia Davì

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''


from flask import Flask, render_template, request
from urllib.request import urlopen
from urllib.error import HTTPError
import json

app=Flask('__name__')

'''
Routing to the homepage
'''

@app.route('/')
def home():
    return "<h1>Search terms throug the Github API.</h1><br><h2>Please follow the following instructions:</h2><h3>Do GET request to e.g. http://localhost:5000/navigator?search_term=python</h3>"

'''
Routing to the navigator. It gets a search term as parameter and returns the list of the results (only 5) in descendent order.
'''

@app.route('/navigator')
def navigator():
    try:
        search_term = request.args.get('search_term')
        data = find_data(search_term)
        last_commits = commits_list_generator(data["items"])
        return render_template("template.html", search_term = search_term, data_list = data["items"], last_commits = last_commits)
    except:
        return "Service temporarily unavailable. Please try again later."

'''
find_data takes a string as input and returns a dictionary. It queries directly the Github API and returns
the results in the form of a json string, converted to a dictionary
'''
def find_data(string):
    query = "https://api.github.com/search/repositories?q=" + string + "&sort=updated&order=desc&per_page=5"
    data = urlopen(query).read().decode()
    data = json.loads(data)
    return data

'''
It takes the latest commits from every repository and append it in a list, where the order is the same of
the data["items"] list
'''
def commits_list_generator(list):
    list_of_commits = []
    for i in range(0, len(list)):
        commit = commits_scraper(list[i]["commits_url"])
        list_of_commits.append(commit)
    return list_of_commits

'''
It takes an url in form of a string and returns a json file in the form of a dictionary, containing the informations
regarding the commits
'''
def commits_scraper(url):
    try:
        url = url[:-6]
        commits = urlopen(url).read().decode()
        commits = json.loads(commits)[0]
        return commits
    except HTTPError:
        print("API rate limit exceeded")
        return {}


if __name__=='__main__':
    app.run(debug=True)
