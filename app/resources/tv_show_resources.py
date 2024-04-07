from flask_restful import Resource, reqparse, fields, marshal_with
from ..models import TVShow
from app.extensions import db


# Output fields
tv_show_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'genre': fields.String
}

# Request parsers
tv_show_parser = reqparse.RequestParser()
tv_show_parser.add_argument('name', type=str, required=True, help="Name cannot be blank.")
tv_show_parser.add_argument('genre', type=str, required=True, help="Genre cannot be blank.")

class TVShowResource(Resource):
    @marshal_with(tv_show_fields)
    def get(self, id):
        tv_show = TVShow.query.get_or_404(id)
        return tv_show

    @marshal_with(tv_show_fields)
    def put(self, id):
        data = tv_show_parser.parse_args()
        tv_show = TVShow.query.get_or_404(id)
        tv_show.name = data['name']
        tv_show.genre = data['genre']
        db.session.commit()
        return tv_show

    def delete(self, id):
        tv_show = TVShow.query.get_or_404(id)
        db.session.delete(tv_show)
        db.session.commit()
        return {'message': 'TV show deleted'}

class TVShowListResource(Resource):
    @marshal_with(tv_show_fields)
    def get(self):
        tv_shows = TVShow.query.all()
        return tv_shows

    @marshal_with(tv_show_fields)
    def post(self):
        data = tv_show_parser.parse_args()
        tv_show = TVShow(name=data['name'], genre=data['genre'])
        db.session.add(tv_show)
        db.session.commit()
        return tv_show, 201

class TVShowSearchResource(Resource):
    @marshal_with(tv_show_fields)
    def get(self, genre):
        tv_shows = TVShow.query.filter_by(genre=genre).all()
        if tv_shows:
            return tv_shows
        else:
            return {'message': 'No TV shows found with that genre'}, 404
