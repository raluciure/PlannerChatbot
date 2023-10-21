class LuisEntity:
    def __init__(self, _entity):
        entity = _entity[0]
        self._name = entity['type']
        self._value = entity['text']

    def __str__(self):
        return "Entity: " + str(self._name) + " " + str(self._value)