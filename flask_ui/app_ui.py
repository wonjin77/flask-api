from flask import Flask
from flask import request, render_template
import requests
import pandas as pd
import html

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/Movies')
def total():
    address = 'http://flask-rest-api-service:5001/Movies'
    # address = 'http://localhost:5001/Movies/'
    r = requests.get(address) 
    total_movie = eval(r.text)
    df_info = pd.DataFrame(data=total_movie['movie_info']).T
    df_info.to_html('templates/df_html.html', classes='movie_info')
    return render_template('df_html.html')

# @app.route('/Movies/upload')
# def create(title_id, title, genre):
#     address = f'http://flask-rest-api-service:5001/Movies/{title_id}'
#     # address = f'http://localhost:5001/Movies/{title_id}'
#     data = {
#         'title': title,
#         'genre': genre,
#     }
#     r = requests.post(address, data=data)
#     return r.content

@app.route('/Raw')
def get_raw():
    address = 'http://flask-rest-api-service:5001/Movies'
    # address = 'http://localhost:5001/Movies/'
    r = requests.get(address) 
    total_movie = eval(r.text)
    return total_movie['movie_info']

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)