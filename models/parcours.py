class ParcoursModel:
    def __init__(self):
        self._id = None
        self._date_debut = None
        self._date_fin = None
        self._diplome = None
        self._etablissement = None
        self._logo = None
        self._ville = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def date_debut(self):
        return self._date_debut

    @date_debut.setter
    def date_debut(self, value):
        self._date_debut = value

    @property
    def date_fin(self):
        return self._date_fin

    @date_fin.setter
    def date_fin(self, value):
        self._date_fin = value

    @property
    def diplome(self):
        return self._diplome

    @diplome.setter
    def diplome(self, value):
        self._diplome = value

    @property
    def etablissement(self):
        return self._etablissement

    @etablissement.setter
    def etablissement(self, value):
        self._etablissement = value

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value

    @property
    def ville(self):
        return self._ville

    @ville.setter
    def ville(self, value):
        self._ville = value

    def parse_json(self, data, hasid=False):
        if hasid: self.id = str(data['_id'])
        self.date_debut = data['date_debut']
        self.date_fin = data['date_fin']
        self.diplome = data['diplome']
        self.etablissement = data['etablissement']
        self.logo = data['logo']
        self.ville = data['ville']
        return self

    def to_json(self, include_id=False):
        if include_id:
            return {'id': self._id, 'date_debut': self._date_debut, 'date_fin': self._date_fin, 'diplome': self._diplome,\
                    'etablissement': self._etablissement, 'logo': self._logo,\
                    'ville': self._ville}
        return {'date_debut': self._date_debut, 'date_fin': self._date_fin, 'diplome': self._diplome, \
                'etablissement': self._etablissement, 'logo': self._logo, \
                'ville': self._ville}