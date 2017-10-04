## SI 364
## Fall 2017
## HW 3

## This homework has 2 parts. This file is the basis for HW 3 part 1.

## Add view functions to this Flask application code below so that the routes described in the README exist 
## and render the templates they are supposed to (all templates provided inside the HW3Part1/templates directory).

##########################################

# When you are done, you should have the following four routes which render each of the corresponding templates with reasonable data:

# * `http://localhost:5000/artistform` -> `artistform.html`
# * `http://localhost:5000/artistinfo` -> `artist_info.html`
# * `http://localhost:5000/artistlinks` -> `artist_links.html`
# * `http://localhost:5000/specific/song/<artist_name>` -> `specific_artist.html`

##########################################

from flask import Flask, request, render_template
import json

import requests


app = Flask(__name__)
app.debug = True 

@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route('/artistform', methods= ['POST','GET'])
def artistform():
    return render_template('artistform.html')
##works

@app.route('/artistinfo')
def artistinfo():
    # if request.method == 'GET':
    #     result = request.args
    #     #r = result.get('artist')
     
    #     # params = {}
    #     # params['x'] = result.get('artist')
      
    #     # params = {}
    #     params = result.get('artist')

    #     # params['limit'] = result.get('num')
    #     lookup = requests.get('https://itunes.apple.com/search?', params = params)
    #     #return str(lookup
    #     data = json.loads(lookup.text)
    #     #return x
    #     #return r
    #     return render_template('artist_info.html', objects = data['results'])#, results = data['results'])




    if request.method == 'GET':
        result = request.args
        params = {}
        params['term'] = result.get('artist')
        #params['limit'] = result.get('num')
        resp = requests.get('https://itunes.apple.com/search?', params = params)
        data = json.loads(resp.text)
        return render_template('artist_info.html', objects = data['results'])


  ########

# @app.route('/itunes-result')
# def resultTunes():
#     if request.method == 'GET':
#         result = request.args
#         params = {}
#         params['term'] = result.get('artist')
#         params['limit'] = result.get('num')
#         resp = requests.get('https://itunes.apple.com/search?', params = params)
#         data = json.loads(resp.text)
#         return render_template('list.html', results = data['results'])

################

   # return render_template('artist_info.html')

#Track Name: {{ r['trackName'] }}

@app.route('/artistlinks')
def artistlinks():
	return render_template('artist_links.html')
##works

@app.route('/specific/song/<artist_name>')
def specificsong(artist_name):
    if request.method == 'GET':
        result = request.args
        params = {}
        params['term'] = artist_name
        resp = requests.get('https://itunes.apple.com/search?', params = params)
        data = json.loads(resp.text)        
        #r = result.get('artist_name')

        #return artist_name
        return render_template('specific_artist.html', results = data['results'])



@app.route('/user/<name>')
def hello_to_you():

    return '<h1>Hello {0}<h1>'.format(name)


if __name__ == '__main__':
    app.run(debug = True)
