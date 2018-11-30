from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from services.parallel_universe_handler import Person, Universe, Powerbalance

app = Flask(__name__)
CORS(app)

api = Api(app)


#Add all routes here
api.add_resource(Person, '/person')
api.add_resource(Universe, '/universe/<universe_id>')
api.add_resource(Powerbalance, '/balancepower')



if __name__ == '__main__':
    app.run(debug=True, threaded=True)
