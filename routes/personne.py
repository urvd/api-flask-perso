import json
from typing import Any

import pymongo
from requests import Response

from models.person import PersonModel
from mongo.mongodb import MyCVdb, PersonColl
from flask import Blueprint, jsonify, request

personRoutes = Blueprint('person_routes', __name__,)


API_PERSON_ENDPOINT = '/api/person'

#
# def parse_person(result):
#     return {'id': result['id'],'nom': result['nom'], 'prenom': result['prenom'], 'photo': result['nom'],
#                 'date_naissance':result['date_naissance'],'lieu_naissance':result['lieu_naissance'],
#                 'permis':result['permis']}
def insert():
    PersonColl.insert_one()

@personRoutes.route(API_PERSON_ENDPOINT+'/find', methods=['GET'])
def read():
    key = request.args.keys()[0]
    value = request.arg[key]
    if key is not None and value is not None:
        reponse = PersonColl.find_one({key: value})
        model = PersonModel.parse_json(reponse)
        jsonify(model.to_json())
    else:
        reponse = PersonColl.find()
        list = []
        for result in reponse:
            model = PersonModel.parse_json(result, hasid=True)
            list.append(model.to_json(include_id=True))
        return jsonify(list)

@personRoutes.route(API_PERSON_ENDPOINT+'/insert',  methods=['POST'])
def insert():
    result = request.get_json()
    model = PersonModel.parse_json(result)
    PersonColl.insert_one(model.to_json())
    return Response(status=200)

@personRoutes.route(API_PERSON_ENDPOINT + '/update')
def update():
    return Response(status=200)

@personRoutes.route(API_PERSON_ENDPOINT + '/delete')
def delete():
    return Response(status=200)