import os
from copy import copy

import pymongo
from decouple import config

mongo_conn = config('MONGO_URL')
print(mongo_conn)
mongo = pymongo.MongoClient(mongo_conn)

MyCVdb = pymongo.database.Database(mongo, 'datacv')

PersonColl = pymongo.collection.Collection(MyCVdb, 'Personne')

ObjectifColl = pymongo.collection.Collection(MyCVdb, 'Objectif')

ParcoursColl = pymongo.collection.Collection(MyCVdb, 'Parcours')

ExperienceColl = pymongo.collection.Collection(MyCVdb, 'Experience')

CompetenceColl = pymongo.collection.Collection(MyCVdb, 'Competence')

LoisirsColl = pymongo.collection.Collection(MyCVdb, 'Loisirs')