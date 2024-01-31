from src.person import Person, RecoveredState, SusceptibleState, NonSymptomaticState, SymptomaticState
from src.geometry import IzolationZone
from config.simulation import SimulationConfig
from src.geometry import Point
from typing import List, Tuple
from numpy.typing import ArrayLike

class PopulationBuilder:
    def __init__(self, population: ArrayLike, izolation_zones: List[IzolationZone], initial_infected: List[Tuple[int, int]]):
        self.population = population
        self.izolation_zones = izolation_zones
        self.initial_infected = initial_infected
    
    def build(self):
        """ Builds a population from the numpy array, person is created for each 1 """
        people = []
        for i, row in enumerate(self.population):
            for j, person in enumerate(row):
                if person == 1:
                    if (i, j) in self.initial_infected:
                        people.append(Person(i, j, NonSymptomaticState()))
                    else:
                        people.append(Person(i, j, SusceptibleState()))
        return Population(people, self.izolation_zones)
    



class Population:
    def __init__(self, people: List[Person], izolation_zones: List[IzolationZone]):
        self.people = people
        self.izolation_zones = izolation_zones
        self.day = 0

    def pass_day(self):
        """ Passes a day for all people """
        for person in self.people:
            person.pass_day(self.people)

        for person in self.people:
            person.travel(self.people)
        
    def set_izolation_zones(self):
        """ Sets the izolation zones of all people """
        for person in self.people:
            person.set_izolation_zone(self.izolation_zones)
    
    def count_infected(self):
        """ Counts the number of infected people """
        return sum(isinstance(person.state, NonSymptomaticState) or isinstance(person.state, SymptomaticState) for person in self.people)
    
    def count_recovered(self):
        """ Counts the number of recovered people """
        return sum(isinstance(person.state, RecoveredState) for person in self.people)
    
    def count_susceptible(self):
        """ Counts the number of susceptible people """
        return sum(isinstance(person.state, SusceptibleState) for person in self.people)
    
    def count_people(self):
        """ Counts the number of people """
        return len(self.people)
    
    def count_infected_in_zone(self, zone: IzolationZone):
        """ Counts the number of infected people in the zone """
        return sum((isinstance(person.state, NonSymptomaticState) or isinstance(person.state, SymptomaticState)) and person.izolation_zone == zone for person in self.people)
    
    def count_recovered_in_zone(self, zone: IzolationZone):
        """ Counts the number of recovered people in the zone """
        return sum(isinstance(person.state, RecoveredState) and person.izolation_zone == zone for person in self.people)
    
    def count_susceptible_in_zone(self, zone: IzolationZone):
        """ Counts the number of susceptible people in the zone """
        return sum(isinstance(person.state, SusceptibleState) and person.izolation_zone == zone for person in self.people)
    
    def count_people_in_zone(self, zone: IzolationZone):
        """ Counts the number of people in the zone """
        return sum(person.izolation_zone == zone for person in self.people)
    
    def get_stats(self):
        """ Returns the statistics of the population """
        return {
            "day": self.day,
            "infected": self.count_infected(),
            "recovered": self.count_recovered(),
            "susceptible": self.count_susceptible(),
            "people": self.count_people(),
        }
    
    def get_stats_in_zone(self, zone: IzolationZone):
        """ Returns the statistics of the population in the zone """
        return {
            "day": self.day,
            "infected": self.count_infected_in_zone(zone),
            "recovered": self.count_recovered_in_zone(zone),
            "susceptible": self.count_susceptible_in_zone(zone),
            "people": self.count_people_in_zone(zone),
        }
    
    def __repr__(self):
        return f"Population({self.get_stats()})"
    

    



