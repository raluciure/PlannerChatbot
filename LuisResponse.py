import json
from LuisIntent import LuisIntent
from LuisEntity import LuisEntity


class LuisResponse:
    def __init__(self, JSONResponse):

        if JSONResponse is None:
            raise TypeError('NULL JSON response')
        if not JSONResponse:
            raise ValueError('Invalid _APP_KEY')

        if isinstance(JSONResponse, str):
            try:
                response = json.loads(JSONResponse)
            except Exception:
                raise Exception('Error in parsing json')

        else:
            response = JSONResponse

        if 'statusCode' in response:
            raise Exception('Invalid Subscription Key')
        elif 'error' in response:
            raise Exception(response['error']['message'])

        self._query = response['query']
        self._entities = {}
        self._prediction = {}

        if 'prediction' in response:
            self._prediction = response['prediction']

        self._topIntent = self._prediction['topIntent']
        self._intents = self._prediction['intents']
        if ('$instance' in self._prediction['entities']):
            self._entities = self._prediction['entities']['$instance']

        self._entityList = []
        if ('Activity' in self._entities):
            self._entityList.append(LuisEntity(self._entities['Activity']))
        if ('Subject' in self._entities):
            self._entityList.append(LuisEntity(self._entities['Subject']))
        if ('Date' in self._entities):
            self._entityList.append(LuisEntity(self._entities['Date']))
        if ('Day' in self._entities):
            self._entityList.append(LuisEntity(self._entities['Day']))
        if ('Hour' in self._entities):
            self._entityList.append(LuisEntity(self._entities['Hour']))
        if ('Person' in self._entities):
            self._entityList.append(LuisEntity(self._entities['Person']))