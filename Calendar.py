from Event import Event

class Calendar:
    events = []

    def addEvent(self, event):
        self.events.append(event)

    def deleteEvent(self, event):
        self.events.remove(event)

    def __str__(self):
        res = ""
        for event in self.events:
            res = res + str(event) + '\n'
        return res