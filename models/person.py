class PersonModel:
    def __init__(self):
        self._id = None
        self._nom = None
        self._prenom = None
        self._photo = None
        self._date_naissance = None
        self._lieu_naissance = None
        self._permis = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, value):
        self._prenom = value

    @property
    def photo(self):
        return self._photo

    @photo.setter
    def photo(self, value):
        self._photo = value

    @property
    def date_naissance(self):
        return self._date_naissance

    @date_naissance.setter
    def date_naissance(self, value):
        self._date_naissance = value

    @property
    def lieu_naissance(self):
        return self._lieu_naissance

    @lieu_naissance.setter
    def lieu_naissance(self, value):
        self._lieu_naissance = value

    @property
    def permis(self):
        return self._permis

    @permis.setter
    def permis(self, value):
        self._permis = value

    def parse_json(self, data, hasid=False):
        if hasid: self.id = str(data['id'])
        self.nom = data['nom']
        self.prenom = data['prenom']
        self.photo = data['photo']
        self.date_naissance = data['date_naissance']
        self.lieu_naissance = data['lieu_naissance']
        self.permis = data['permis']
        return self

    def to_json(self, include_id=False):
        if include_id:
            return {'id': self._id, 'nom': self._nom, 'prenom': self._prenom, 'photo': self._photo,\
                    'date_naissance': self._date_naissance, 'lieu_naissance': self._lieu_naissance,\
                    'permis': self._permis}
        return {'nom': self._nom, 'prenom': self._prenom, 'photo': self._photo, \
                'date_naissance': self._date_naissance, 'lieu_naissance': self._lieu_naissance, \
                'permis': self._permis}