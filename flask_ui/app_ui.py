from flask import Flask
from flask import request, render_template
import requests
import pandas as pd
import html

app = Flask(__name__)

# host = 'flask-rest-api-service.flask.svc.kr-central-1.c.kakaoi.io'
host = 'flask-rest-api-service.flask.svc.cluster.local'
# host = 'localhost'
address = f'http://{host}:5001/Movies/'


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/Raw')
def get_raw():
    r = requests.get(address) 
    total_movie = eval(r.text)
    return total_movie['movie_info']

@app.route('/Movies')
def total():
    # r = requests.get(address) 
    # total_movie = eval(r.text)
    movie_dict = get_raw()
    df_info = pd.DataFrame(data=movie_dict).T
    df_info.to_html('templates/df_html.html', classes='movie_info')
    return render_template('df_html.html')

@app.route('/Movies/<int:title_id>')
def detail(title_id):
    # r = requests.get(address) 
    # total_movie = eval(r.text)
    movie_dict = get_raw()
    df_info = pd.DataFrame(data=movie_dict).T
    df_info_detail = df_info.loc[str(title_id):str(title_id)]
    df_info_detail.to_html('templates/df_detail_html.html', classes='movie_info_detail')
    return render_template('df_detail_html.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)