class Google Maps Location History:
  class Timelineobjects(list):
    class Items:
      class Activitysegment:
        class Startlocation:
          def __init__(self, values: dict = None):
            values = values if values is not None else {}
            self.latitudeE7: int = values.get("latitudeE7", None)
            self.longitudeE7: int = values.get("longitudeE7", None)

        class Endlocation:
          def __init__(self, values: dict = None):
            values = values if values is not None else {}
            self.latitudeE7: int = values.get("latitudeE7", None)
            self.longitudeE7: int = values.get("longitudeE7", None)

        class Duration:
          def __init__(self, values: dict = None):
            values = values if values is not None else {}
            self.startTimestampMs: str = values.get("startTimestampMs", None)
            self.endTimestampMs: str = values.get("endTimestampMs", None)

        class Activities(list):
          class Items:
            def __init__(self, values: dict = None):
              values = values if values is not None else {}
              self.activityType: str = values.get("activityType", None)
              self.probability: float = values.get("probability", None)

          def __init__(self, values: list = None):
            super().__init__()
            values = values if values is not None else []
            self[:] = [self.Items(value) for value in values]

        class Waypointpath:
          class Waypoints(list):
            class Items:
              def __init__(self, values: dict = None):
                values = values if values is not None else {}
                self.latE7: int = values.get("latE7", None)
                self.lngE7: int = values.get("lngE7", None)

            def __init__(self, values: list = None):
              super().__init__()
              values = values if values is not None else []
              self[:] = [self.Items(value) for value in values]

          def __init__(self, values: dict = None):
            values = values if values is not None else {}
            self.waypoints = self.Waypoints(values=values.get("waypoints"))

        class Simplifiedrawpath:
          class Points(list):
            class Items:
              def __init__(self, values: dict = None):
                values = values if values is not None else {}
                self.latE7: int = values.get("latE7", None)
                self.lngE7: int = values.get("lngE7", None)
                self.timestampMs: str = values.get("timestampMs", None)
                self.accuracyMeters: int = values.get("accuracyMeters", None)

            def __init__(self, values: list = None):
              super().__init__()
              values = values if values is not None else []
              self[:] = [self.Items(value) for value in values]

          def __init__(self, values: dict = None):
            values = values if values is not None else {}
            self.points = self.Points(values=values.get("points"))

        class Transitpath:
          class Transitstops(list):
            class Items:
              def __init__(self, values: dict = None):
                values = values if values is not None else {}
                self.latitudeE7: int = values.get("latitudeE7", None)
                self.longitudeE7: int = values.get("longitudeE7", None)
                self.placeId: str = values.get("placeId", None)
                self.name: str = values.get("name", None)

            def __init__(self, values: list = None):
              super().__init__()
              values = values if values is not None else []
              self[:] = [self.Items(value) for value in values]

          def __init__(self, values: dict = None):
            values = values if values is not None else {}
            self.transitStops = self.Transitstops(values=values.get("transitStops"))
            self.name: str = values.get("name", None)
            self.hexRgbColor: str = values.get("hexRgbColor", None)

        def __init__(self, values: dict = None):
          values = values if values is not None else {}
          self.startLocation = self.Startlocation(values=values.get("startLocation"))
          self.endLocation = self.Endlocation(values=values.get("endLocation"))
          self.duration = self.Duration(values=values.get("duration"))
          self.distance: int = values.get("distance", None)
          self.activityType: str = values.get("activityType", None)
          self.confidence: str = values.get("confidence", None)
          self.activities = self.Activities(values=values.get("activities"))
          self.waypointPath = self.Waypointpath(values=values.get("waypointPath"))
          self.simplifiedRawPath = self.Simplifiedrawpath(values=values.get("simplifiedRawPath"))
          self.transitPath = self.Transitpath(values=values.get("transitPath"))

      class Placevisit:
        class Location:
          class Sourceinfo:
            def __init__(self, values: dict = None):
              values = values if values is not None else {}
              self.deviceTag: int = values.get("deviceTag", None)

          def __init__(self, values: dict = None):
            values = values if values is not None else {}
            self.latitudeE7: int = values.get("latitudeE7", None)
            self.longitudeE7: int = values.get("longitudeE7", None)
            self.placeId: str = values.get("placeId", None)
            self.address: str = values.get("address", None)
            self.name: str = values.get("name", None)
            self.sourceInfo = self.Sourceinfo(values=values.get("sourceInfo"))
            self.locationConfidence: float = values.get("locationConfidence", None)
            self.semanticType: str = values.get("semanticType", None)

        class Duration:
          def __init__(self, values: dict = None):
            values = values if values is not None else {}
            self.startTimestampMs: str = values.get("startTimestampMs", None)
            self.endTimestampMs: str = values.get("endTimestampMs", None)

        class Othercandidatelocations(list):
          class Items:
            def __init__(self, values: dict = None):
              values = values if values is not None else {}
              self.latitudeE7: int = values.get("latitudeE7", None)
              self.longitudeE7: int = values.get("longitudeE7", None)
              self.placeId: str = values.get("placeId", None)
              self.locationConfidence: float = values.get("locationConfidence", None)
              self.semanticType: str = values.get("semanticType", None)

          def __init__(self, values: list = None):
            super().__init__()
            values = values if values is not None else []
            self[:] = [self.Items(value) for value in values]

        class Childvisits(list):
          class Items:
            class Location:
              class Sourceinfo:
                def __init__(self, values: dict = None):
                  values = values if values is not None else {}
                  self.deviceTag: int = values.get("deviceTag", None)

              def __init__(self, values: dict = None):
                values = values if values is not None else {}
                self.latitudeE7: int = values.get("latitudeE7", None)
                self.longitudeE7: int = values.get("longitudeE7", None)
                self.placeId: str = values.get("placeId", None)
                self.address: str = values.get("address", None)
                self.name: str = values.get("name", None)
                self.sourceInfo = self.Sourceinfo(values=values.get("sourceInfo"))
                self.locationConfidence: float = values.get("locationConfidence", None)

            class Duration:
              def __init__(self, values: dict = None):
                values = values if values is not None else {}
                self.startTimestampMs: str = values.get("startTimestampMs", None)
                self.endTimestampMs: str = values.get("endTimestampMs", None)

            class Othercandidatelocations(list):
              class Items:
                def __init__(self, values: dict = None):
                  values = values if values is not None else {}
                  self.latitudeE7: int = values.get("latitudeE7", None)
                  self.longitudeE7: int = values.get("longitudeE7", None)
                  self.placeId: str = values.get("placeId", None)
                  self.locationConfidence: float = values.get("locationConfidence", None)

              def __init__(self, values: list = None):
                super().__init__()
                values = values if values is not None else []
                self[:] = [self.Items(value) for value in values]

            def __init__(self, values: dict = None):
              values = values if values is not None else {}
              self.location = self.Location(values=values.get("location"))
              self.duration = self.Duration(values=values.get("duration"))
              self.placeConfidence: str = values.get("placeConfidence", None)
              self.centerLatE7: int = values.get("centerLatE7", None)
              self.centerLngE7: int = values.get("centerLngE7", None)
              self.visitConfidence: int = values.get("visitConfidence", None)
              self.otherCandidateLocations = self.Othercandidatelocations(values=values.get("otherCandidateLocations"))
              self.editConfirmationStatus: str = values.get("editConfirmationStatus", None)

          def __init__(self, values: list = None):
            super().__init__()
            values = values if values is not None else []
            self[:] = [self.Items(value) for value in values]

        class Simplifiedrawpath:
          class Points(list):
            class Items:
              def __init__(self, values: dict = None):
                values = values if values is not None else {}
                self.latE7: int = values.get("latE7", None)
                self.lngE7: int = values.get("lngE7", None)
                self.timestampMs: str = values.get("timestampMs", None)
                self.accuracyMeters: int = values.get("accuracyMeters", None)

            def __init__(self, values: list = None):
              super().__init__()
              values = values if values is not None else []
              self[:] = [self.Items(value) for value in values]

          def __init__(self, values: dict = None):
            values = values if values is not None else {}
            self.points = self.Points(values=values.get("points"))

        def __init__(self, values: dict = None):
          values = values if values is not None else {}
          self.location = self.Location(values=values.get("location"))
          self.duration = self.Duration(values=values.get("duration"))
          self.placeConfidence: str = values.get("placeConfidence", None)
          self.centerLatE7: int = values.get("centerLatE7", None)
          self.centerLngE7: int = values.get("centerLngE7", None)
          self.visitConfidence: int = values.get("visitConfidence", None)
          self.editConfirmationStatus: str = values.get("editConfirmationStatus", None)
          self.otherCandidateLocations = self.Othercandidatelocations(values=values.get("otherCandidateLocations"))
          self.childVisits = self.Childvisits(values=values.get("childVisits"))
          self.simplifiedRawPath = self.Simplifiedrawpath(values=values.get("simplifiedRawPath"))

      def __init__(self, values: dict = None):
        values = values if values is not None else {}
        self.activitySegment = self.Activitysegment(values=values.get("activitySegment"))
        self.placeVisit = self.Placevisit(values=values.get("placeVisit"))

    def __init__(self, values: list = None):
      super().__init__()
      values = values if values is not None else []
      self[:] = [self.Items(value) for value in values]

  def __init__(self, values: dict = None):
    values = values if values is not None else {}
    self.timelineObjects = self.Timelineobjects(values=values.get("timelineObjects"))

