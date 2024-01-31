from scipy.stats import norm
from scipy.special import expit
from dataclasses import dataclass
from math import pi

from config.simulation import SimulationConfig


@dataclass
class Virus:
    """Virus configuration"""
    base_transmission_rate: float = 0.05
    variable_transmission_rate: float = 0.15

    mean_infection_duration: int = 14
    std_infection_duration: int = 3

    days_until_symptoms: int = 5

    @classmethod
    def get_well_proba(cls, days_infected: int) -> float:
        """Returns the probability of a person getting well"""
        if days_infected > 31:
            return 1
        return norm.pdf(days_infected, loc=cls.mean_infection_duration, scale=cls.std_infection_duration)
    
    @classmethod
    def get_infection_proba(cls, infected_neighbours: int) -> float:
        """Returns the probability of a person getting infected"""
        if infected_neighbours == 0:
            return 0
        x = infected_neighbours / (pi * SimulationConfig.infection_reach ** 2) * 10 - 5
        return expit(x) * cls.variable_transmission_rate + cls.base_transmission_rate
    