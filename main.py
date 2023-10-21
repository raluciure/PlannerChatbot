from LuisClient import LuisClient
from ResponseHandler import ResponseHandler

query = ""
print("Calendar Chatbot Running...")
while(True):
    query = input()
    if(query == "q" or query == "quit" ):
        print("Good bye!")
        break;

    #     predict - topIntent and entities
    response = LuisClient.predict(LuisClient, query)

    # handle the response
    ResponseHandler.handle(ResponseHandler, response)