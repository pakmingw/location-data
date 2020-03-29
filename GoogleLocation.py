import json

class ActivitySegment:
    def __init__(self, values: dict = None):
        self.activityType = 'NONE'
        self.confidence = ''
        self.distance = 0
        self.duration = 0
        self.startTimestampMs = 0
        self.endTimestampMs = 0

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)

class PlaceVisit:
    def __init__(self, values: dict = None):
        self.semanticType = 'NONE'
        self.name = ''
        self.latitudeE7 = 0
        self.longitudeE7 = 0
        self.startTimestampMs = 0
        self.endTimestampMs = 0
        self.duration = 0

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True)