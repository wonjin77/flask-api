from flask import Flask, request, Response, abort
from flask_restx import Resource, Api, fields


app = Flask(__name__)
api = Api(app)

movies = api.namespace('Movies', description='Movie Infomation APIs')

movie_model = api.model(
            'Movie Information',
            {
            "title": fields.String(description="movie title", required=True),
            "genre": fields.String(description="movie genre", required=False),
            }
        )

movie_info = {}

@movies.route('/')
class Movie(Resource):
  def get(self):
    return {
        'num_movies': len(movie_info),
        'movie_info': movie_info,
    }


@movies.route('/<int:title_id>')
class MovieTitle(Resource):
  # 영화 정보 조회
  def get(self, title_id):
    if not title_id in movie_info.keys():
      abort(404, description=f"Title ID {title_id} doesn't exist")

    return {
        'title_id': title_id,
        'data': movie_info[title_id]
    }

  # 새로운 영화 생성
  @api.expect(movie_model)
  def post(self, title_id):
    if title_id in movie_info.keys():
      abort(409, description=f"Title ID {title_id} already exists")

    params = request.get_json()
    movie_info[title_id] = params

    return Response(status=201)


  # 영화 정보 삭제
  def delete(self, title_id):
    if not title_id in movie_info.keys():
      abort(404, description=f"Title ID {title_id} doesn't exists")
      
    del movie_info[title_id]
    
    return Response(status=200)


  # 영화 정보 변경
  @api.expect(movie_model)
  def put(self, title_id):
      
    global movie_info

    if not title_id in movie_info.keys():
        abort(404, description=f"Title ID {title_id} doesn't exists")
    
    params = request.get_json()
    movie_info[title_id] = params

    return Response(status=200)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)