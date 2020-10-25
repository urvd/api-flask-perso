import json

import pymongo

from models.objectif import ObjectifModel
from mongo.mongodb import MyCVdb, ObjectifColl
from flask import Blueprint, jsonify, request, Response

objectifRoutes = Blueprint('objectif_routes', __name__,)


API_OBJ_ENDPOINT = '/api/objectif'

# results = json.loads(json.dumps(PersonColl.find()))

def parse_obj(result):
    return {'id': result['id'], 'raison': result['raison'], 'description': result['description']}

def insert(raison, description = ""):
    ObjectifColl.insert_one({"raison": raison, "description": description})


@objectifRoutes.route(API_OBJ_ENDPOINT+'/read', methods=['GET'])
def read():
    if request.args is None:
        key = request.args.keys()
        value = request.arg[key]
        if key is not None and value is not None: #TODO: corriger la lecture filtrer
            reponse = ObjectifColl.find_one({key: value})
            print(reponse)
            model = ObjectifModel()
            model.parse_json(reponse, hasid=True)
            jsonify(model.to_json(include_id=True))
    else:
        reponse = ObjectifColl.find()
        list = []
        for result in reponse:
            model = ObjectifModel()
            model.parse_json(result, hasid=True)
            list.append(model.to_json(include_id=True))
        return jsonify(list)


@objectifRoutes.route(API_OBJ_ENDPOINT+'/insert', methods=['POST'])
def write():
    result = request.get_json()
    model = ObjectifModel()
    model.parse_json(result)
    ObjectifColl.insert_one(model.to_json())
    return Response(status=200)