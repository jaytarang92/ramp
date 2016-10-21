from flask_restful import Resource

class crap(Resource):

    def get(self):
        return {"route":"crap"}