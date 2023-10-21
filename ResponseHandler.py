from Event import Event
from Event import handle_month
from Event import handle_day
from Event import handle_hour

from Calendar import Calendar

class ResponseHandler:
    calendar = Calendar()

    def handle(self, response):
        entityList = response._entityList
        topIntent = response._topIntent

        if topIntent == "CreateCalendarEntry":
            #print("Is create intent")
            self.handle_CreateEntry(self, entityList)
        elif topIntent == "DeleteCalendarEntry":
            #print("Is delete intent")
            self.handle_DeleteEntry(self, entityList)
        elif topIntent == "FindCalendarEntry":
            #print("Is find intent")
            events = self.handle_FindEntry(self, entityList)
            self.printEvents(self, events)
        elif topIntent == "Greeting":
            print("Hello! What can I help you with?")
        elif topIntent == "ClearCalendarEntry":
            #print("Is clear intent")
            self.handle_ClearDay(self, entityList)
        else:
            print("I can't help you with this! Sorry!")


    def handle_CreateEntry(self, entityList):
        if(len(entityList) <= 0):
            print("No good format for the event!")
        else:
            subject = "none"
            activity = "none"
            date = "none"
            day = "none"
            hour = "none"
            person = "none"

            for entity in entityList:
                if(entity._name == "Subject"):
                    subject = entity._value
                elif(entity._name == "Activity"):
                    activity = entity._value
                elif(entity._name == "Date"):
                    date = entity._value
                elif(entity._name == "Day"):
                    day = entity._value
                elif(entity._name == "Hour"):
                    hour = entity._value
                elif(entity._name == "Person"):
                    person = entity._value

            if (date != "none"):
                event = Event(activity, date, day, hour, person, subject)
            else:
                if(day != "none"):
                    event = Event(activity, date, day, hour, person, subject)
                else:
                    string = self.handleNoDate(self)
                    if(handle_day(string) != -1):
                        day = string
                    else:
                        date = string
                    event = Event(activity, date, day, hour, person, subject)

            if(hour != "none"):
                if handle_hour(hour) == 0:
                    event = Event(activity, date, day, hour, person, subject)
            else:
                hour = self.handleNoStartTime(self)
                if handle_hour(hour) == 0:
                    event = Event(activity, date, day, hour, person, subject)

            if (activity != "none"):
                event = Event(activity, date, day, hour, person, subject)
            else:
                activity = self.handleNoSubject(self)
                event = Event(activity, date, day, hour, person, subject)

            print(str(event))

            events = self.calendar.events
            found = 0
            for e in events:
                if ((e._day == day and e._hour == hour) or (e._date == date and e._hour == hour)):
                    found = 1

            if(found == 1):
                print("There already exists an event at that time!")
            else:
                self.calendar.addEvent(event)


    def handleNoDate(self):
        print("The event doesn't have a date or a day. Please tell me a date or a day:")
        startTime = input()
        return startTime

    def handleNoStartTime(self):
        print("The event doesn't have a start time. Please tell me an hour (1-12am/pm):")
        startTime = input()
        return startTime

    def handleNoSubject(self):
        print("Please tell me the event:")
        subject = input()
        return subject

    def handle_FindEntry(self, entityList):
        if(len(entityList) <= 0):
            print("No event!")
        else:

            subject = "none"
            activity = "none"
            date = "none"
            day = "none"
            hour = "none"
            person = "none"

            for entity in entityList:

                if (entity._name == "Subject"):
                    subject = entity._value
                elif (entity._name == "Activity"):
                    activity = entity._value
                elif (entity._name == "Date"):
                    date = entity._value
                elif (entity._name == "Day"):
                    day = entity._value
                elif (entity._name == "Hour"):
                    hour = entity._value
                elif (entity._name == "Person"):
                    person = entity._value

            events = self.calendar.events

            if(subject != "none"):
                events = self.filterSubject(self, events,subject)
            if(activity != "none"):
                events = self.filterActivity(self, events, activity)
            if(date != "none"):
                events = self.filterDate(self, events, date)
            if (person != "none"):
                events = self.filterPerson(self, events, person)
            if (day != "none"):
                events = self.filterDay(self, events, day)

            return events

    def handle_DeleteEntry(self, entityList):
        events = self.handle_FindEntry(self, entityList)
        if (len(events) > 0):
            event = events[0]
        else:
            event = None

        if(event):
            self.calendar.deleteEvent(event)
            print("Event removed succesfully!")
        else:
            print("No such event found!")



    def handle_ClearDay(self, entityList):
        if (len(entityList) <= 0):
            print("No event!")
        else:
            date = "none"
            day = "none"
            for entity in entityList:
                if (entity._name == "Date"):
                    date = entity._value
                if (entity._name == "Day"):
                    day = entity._value

            events = self.calendar.events
            if (date != "none"):
                events = self.filterDate(self, events, date)
            if (day != "none"):
                events = self.filterDay(self, events, day)

            print("Deleted:")
            for event in events:
                print(event)
                self.calendar.deleteEvent(event)


    def filterSubject(self, events, subject):
        newList = []
        for event in events:
            if(str(event._subject).lower().__contains__(str(subject).lower())):
                newList.append(event)
        return newList

    def filterActivity(self, events, activity):
        newList = []
        for event in events:
            if(str(event._activity).lower().__contains__(str(activity).lower())):
                newList.append(event)
        return newList

    def filterDate(self, events, date):
        newList = []
        for event in events:
            if(str(event._date).lower().__contains__(str(date).lower())):
                newList.append(event)
        return newList

    def filterPerson(self, events, person):
        newList = []
        for event in events:
            if(str(event._person).lower().__contains__(str(person).lower())):
                newList.append(event)
        return newList

    def filterDay(self, events, day):
        newList = []
        for event in events:
            if(str(event._day).lower().__contains__(str(day).lower())):
                newList.append(event)
        return newList


    def printEvents(self, events):
        if(len(events) <= 0):
            print("No events found.")
        else:
            for event in events:
                print(event)