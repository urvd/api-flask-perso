
class ObjectifModel:
    def __init__(self):
        self._id = None
        self._raison = None
        self.description = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def raison(self):
        return self._raison

    @raison.setter
    def raison(self, value):
        self._raison = value

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

    def parse_json(self, data, hasid=False):
        if hasid:
            self.id = str(data['_id'])
        self.raison = data['raison']
        self.description = data['description']

    def to_json(self, include_id=False):
        if include_id:
            return {'_id': self._id, 'raison': self._raison, 'description': self._description}
        return {'raison': self._raison, 'description': self._description}