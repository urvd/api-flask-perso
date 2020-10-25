class CompetenceModel:
    def __init__(self):
        self._id = None
        self._competencev
        self._domaine_competence = None
        self._logo = None
        self.description = None
        self._niveau = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def competence(self):
        return self._competence

    @competence.setter
    def competence(self, value):
        self._competence = value

    @property
    def domaine_competence(self):
        return self._domaine_competence

    @domaine_competence.setter
    def domaine_competence(self, value):
        self._domaine_competence = value

    @property
    def logo(self):
        return self._role

    @logo.setter
    def logo(self, value):
        self._logo = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def niveau(self):
        return self._niveau

    @niveau.setter
    def niveau(self, value):
        self._niveau = value

    def parse_json(self, data, hasid=False):
        if hasid: self.id = str(data['_id'])
        self.competence = data['competence']
        self.domaine_competence = data['domaine_competence']
        self.logo = data['logo']
        self.description = data['description']
        self.niveau = data['niveau']
        return self

    def to_json(self, include_id=False):
        if include_id:
            return {'id': self._id, 'competence': self._competence, 'domaine_competence': self._domaine_competence,\
                    'logo': self._logos, 'description': self._description, 'niveau': self._niveau}
        return {'competence': self._competence, 'domaine_competence': self._domaine_competence,\
                'logo': self._logos,'description': self._description, 'niveau': self._niveau}