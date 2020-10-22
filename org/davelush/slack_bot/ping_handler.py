from flask_restful import Resource


class PingHandler(Resource):

    def get(self):
        return "pong"
