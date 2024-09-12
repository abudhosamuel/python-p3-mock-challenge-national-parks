class NationalPark:
    all_parks = []  # Class variable to track all NationalPark instances

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise Exception("Name must be a string with at least 3 characters.")
        self._name = name
        NationalPark.all_parks.append(self)  # Add to class-level list

    @property
    def name(self):
        return self._name

    def trips(self):
        # Returns a list of all trips at this national park
        return [trip for trip in Trip.all_trips if trip.national_park == self]

    def visitors(self):
        # Returns a unique list of all visitors to this park
        return list(set([trip.visitor for trip in self.trips()]))

    def total_visits(self):
        # Returns the total number of times this park has been visited
        return len(self.trips())

    def best_visitor(self):
        # Returns the visitor who has visited this park the most
        if not self.trips():
            return None
        visitors_count = {visitor: visitor.total_visits_at_park(self) for visitor in self.visitors()}
        return max(visitors_count, key=visitors_count.get)

    @classmethod
    def most_visited(cls):
        # Returns the NationalPark instance with the most visits
        if not cls.all_parks:
            return None
        return max(cls.all_parks, key=lambda park: park.total_visits())


class Trip:
    all_trips = []  # Class variable to track all Trip instances

    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(visitor, Visitor):
            raise Exception("Invalid visitor instance.")
        if not isinstance(national_park, NationalPark):
            raise Exception("Invalid national park instance.")
        if not isinstance(start_date, str) or len(start_date) < 7:
            raise Exception("Start date must be a string with at least 7 characters.")
        if not isinstance(end_date, str) or len(end_date) < 7:
            raise Exception("End date must be a string with at least 7 characters.")
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all_trips.append(self)  # Add to class-level list

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, value):
        if not isinstance(value, Visitor):
            raise Exception("Invalid visitor instance.")
        self._visitor = value

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, value):
        if not isinstance(value, NationalPark):
            raise Exception("Invalid national park instance.")
        self._national_park = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise Exception("Start date must be a string with at least 7 characters.")
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise Exception("End date must be a string with at least 7 characters.")
        self._end_date = value


class Visitor:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise Exception("Name must be a string between 1 and 15 characters.")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise Exception("Name must be a string between 1 and 15 characters.")
        self._name = value

    def trips(self):
        # Returns a list of all trips for this visitor
        return [trip for trip in Trip.all_trips if trip.visitor == self]

    def national_parks(self):
        # Returns a unique list of all parks that this visitor has visited
        return list(set([trip.national_park for trip in self.trips()]))

    def total_visits_at_park(self, park):
        # Returns the total number of times this visitor visited the park
        return sum(1 for trip in self.trips() if trip.national_park == park)
