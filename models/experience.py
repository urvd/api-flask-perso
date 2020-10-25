class ExperienceModel:
    def __init__(self):
        self._id = None
        self._date_debut = None
        self._date_fin = None
        self._entreprise_mere = None
        self._logo_mere = None
        self._entreprise = None
        self._logo = None
        self._role = None
        self.description = None
        self._lieu = None

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
    def entreprise_mere(self):
        return self._entreprise_mere

    @entreprise_mere.setter
    def entreprise_mere(self, value):
        self._entreprise_mere = value

    @property
    def logo_mere(self):
        return self._logo_mere

    @logo_mere.setter
    def logo_mere(self, value):
        self._logo_mere = value

    @property
    def entreprise(self):
        return self._entreprise

    @entreprise.setter
    def entreprise(self, value):
        self._entreprise = value

    @property
    def logo(self):
        return self._role

    @logo.setter
    def logo(self, value):
        self._logo = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def lieu(self):
        return self._lieu

    @lieu.setter
    def lieu(self, value):
        self._lieu = value

    def parse_json(self, data, hasid=False):
        if hasid: self.id = str(data['_id'])
        self.date_debut = data['date_debut']
        self.date_fin = data['date_fin']
        self.entreprise_mere = data['entreprise_mere']
        self.logo_mere = data['logo_mere']
        self.entreprise = data['entreprise']
        self.logo = data['logo']
        self.role = data['role']
        self.description = data['description']
        self.lieu = data['lieu']
        return self

    def to_json(self, include_id=False):
        if include_id:
            return {'id': self._id, 'date_debut': self._date_debut, 'date_fin': self._date_fin,
                    'entreprise_mere': self._entreprise_mere, 'logo_mere': self._logo_mere, \
                    'entreprise': self._entreprise, 'logo': self._logos, 'role': self._role,
                    'description': self._description, 'lieu': self._lieu}
        return {'date_debut': self._date_debut, 'date_fin': self._date_fin, 'entreprise_mere': self._entreprise_mere, \
                'logo_mere': self._logo_mere, 'entreprise': self._entreprise, 'logo': self._logos,
                'role': self._role, 'description': self._description, 'lieu': self._lieu}