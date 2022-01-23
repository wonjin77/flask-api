from flask import Flask
from flask import request, render_template
import requests
import pandas as pd
import html

app = Flask(__name__)
address = 'http://flask-rest-api-service.flask.svc.kr-central-1.c.kakaoi.io:5001/Movies/'
# address = 'http://localhost:5001/Movies/'


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/Movies')
def total():
    r = requests.get(address) 
    total_movie = eval(r.text)
    df_info = pd.DataFrame(data=total_movie['movie_info']).T
    df_info.to_html('templates/df_html.html', classes='movie_info')
    return render_template('df_html.html')

@app.route('/Raw')
def get_raw():
    r = requests.get(address) 
    total_movie = eval(r.text)
    return total_movie['movie_info']

if __name__ == "__main__":
    app.run(port=5000, debug=True)