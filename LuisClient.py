from urllib.parse import quote
import http.client
from LuisResponse import LuisResponse


class LuisClient:
    _EndpointURL = "raluluis.cognitiveservices.azure.com"
    _PredictMask = "https://raluluis.cognitiveservices.azure.com/luis/prediction/v3.0/apps/%s/slots/staging/predict?subscription-key=%s&verbose=true&show-all-intents=true&log=true&query=%s"
    _APP_KEY = "c4407fd8-476d-4b2e-b398-fa57f8add79e"
    _SUBSCRIPTION_KEY = "ddf801cef7944e4c8175a0911a7fceae"

    def predictGenerator(self, query):
        return self._PredictMask % (self._APP_KEY, self._SUBSCRIPTION_KEY, quote(query))

    def predict(self, query):
        try:
            conn = http.client.HTTPSConnection(self._EndpointURL)
            conn.request('GET', self.predictGenerator(self, query))
            res = conn.getresponse()
            return LuisResponse(res.read().decode('UTF-8'))
        except Exception:
            raise

    def showResult(self, response):
        topIntent = response._topIntent
        entities = response._entityList
        print("topIntent: " + topIntent)
        print("entities: ")
        for entity in entities:
            print("\tentity name:" + str(entity._name) + " value:" + str(entity._value))