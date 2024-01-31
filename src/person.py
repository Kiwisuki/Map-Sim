from src.virus import Virus
from src.geometry import IzolationZone
from config.simulation import SimulationConfig
import random as rng
from typing import List, Union
from src.geometry import Point

from collections import Counter
from typing import Protocol

class PersonState(Protocol):
    def pass_day(self, person: "Person", people: List["Person"]):
        ...

class SusceptibleState(PersonState):
    def pass_day(self, person: "Person", people: List["Person"]):
        if rng.random() < Virus.get_infection_proba(person.count_infected_neighbours(people)):
            person.state = NonSymptomaticState()

class NonSymptomaticState(PersonState):
    def pass_day(self, person: "Person", people: List["Person"]):
        person.days_infected += 1
        if person.days_infected > Virus.days_until_symptoms:
            person.state = SymptomaticState()
        if rng.random() < Virus.get_well_proba(person.days_infected):
            person.state = RecoveredState()

class SymptomaticState(PersonState):
    def pass_day(self, person: "Person", people: List["Person"]):
        person.days_infected += 1
        if rng.random() < Virus.get_well_proba(person.days_infected):
            person.state = RecoveredState()

class RecoveredState(PersonState):
    def pass_day(self, person: "Person", people: List["Person"]):
        pass  # Nothing happens to recovered people

class Person(Point):
    def __init__(self, x: int, y: int, state: PersonState):
        super().__init__(x, y)
        self.state = state
        self.izolation_zone = None

        self.days_infected = 0
    
    def count_infected_neighbours(self, people: List["Person"]) -> int:
        """ Searches for infected neighbours within a radius of INFECTION_RADIUS """
        infected_neighbours = Counter(
            self.get_distance(person) < SimulationConfig.infection_reach
            for person in people
            if (isinstance(person.state, NonSymptomaticState) or isinstance(person.state, SymptomaticState))
            and person.izolation_zone == self.izolation_zone
        )
        return infected_neighbours[True]

    def pass_day(self, people: List["Person"]):
        """ Passes a day for the person """
        self.state.pass_day(self, people)

    def set_izolation_zone(self, izolation_zones: List[IzolationZone]):
        """ Sets the izolation zone of the person """
        distances = [izolation_zone.get_distance(self) for izolation_zone in izolation_zones]
        self.izolation_zone = izolation_zones[distances.index(min(distances))]

    def _find_non_symptomatic_person(self, people: List["Person"]) -> Union["Person", None]:
        """Find a non-symptomatic person in the same isolation zone."""
        non_symptomatic_people = [person for person in people if not Virus.shows_symptoms(person.days_infected)]
        non_symptomatic_same_zone = [person for person in non_symptomatic_people if person.izolation_zone == self.izolation_zone]
        non_symptomatic_same_zone.remove(self)
        
        if non_symptomatic_same_zone:
            return rng.choice(non_symptomatic_same_zone)
        else:
            return None    

    def travel(self, people: List["Person"]):
        """ If person is non symptomatic, he can switch """
        if not isinstance(self.state, NonSymptomaticState):
            return

        if rng.random() < SimulationConfig.travel_proba:
            other_person = self._find_non_symptomatic_person(people)
            if other_person:
                self.x, other_person.x = other_person.x, self.x
                self.y, other_person.y = other_person.y, self.y
        
    def __repr__(self):
        return f"Person({self.x}, {self.y}, {self.state.__class__.__name__})"
        



        