import json

from flask import request, Response
from flask_restful import Resource

from controllers.parallel_universe_info import create_person, families_for_universe, \
    check_power_for_same_family_identifier, balance_families


class Person(Resource):
    def post(self):
        json_body = json.loads(request.data)
        is_created = create_person(json_body)
        if is_created:
            return Response(None, status=201, mimetype='application/json')


class Universe(Resource):
    def get(self, universe_id):
        families = families_for_universe(universe_id)
        return Response(response = json.dumps({'families':families}), status=201, mimetype='application/json')

class Powerbalance(Resource):
    def get(self):
        result = families_with_same_power = check_power_for_same_family_identifier()
        return Response(response = json.dumps({'mismatch_family_powers_across_universe':result}), status=200, mimetype='application/json')

    def post(self):
        res = balance_families()
        return Response(None, status=201, mimetype='application/json')









