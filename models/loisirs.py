
class LoisirsModel:
    def __init__(self):
        self._id = None
        self._categorie = None
        self._theme = None
        self.description = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def categorie(self):
        return self._categorie

    @categorie.setter
    def categorie(self, value):
        self._categorie = value

    @property
    def theme(self):
        return self._theme

    @theme.setter
    def theme(self, value):
        self._theme = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def parse_json(self, data, hasid=False):
        if hasid: self.id = str(data['_id'])
        self.categorie = data['categorie']
        self.theme = data['theme']
        self.description = data['description']
        return self

    def to_json(self, include_id=False):
        if include_id:
            return {'_id': self._id, 'categorie': self._categorie, 'theme': self._theme, 'description': self._description}
        return {'categorie': self._categorie, 'theme': self._theme, 'description': self._description}