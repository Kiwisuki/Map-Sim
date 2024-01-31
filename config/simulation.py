from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class SimulationConfig:
    """Simulation configuration constants"""
    image_path: str = "input/pop_density.png"

    resize_factor: float = 0.15
    pixel_density_threshold: int = 0.72

    infection_reach: float = 10

    travel_proba: float = 0.05

    initial_infected_coords: List[Tuple[float, float]] = field(
        default_factory=lambda: [
        (800, 1000),
        (900, 1375),
        ]
    )

    def __post_init__(self):
        """Post init processing"""
        
        self.initial_infected_coords = [
            ( int(x * self.resize_factor),
              int(y * self.resize_factor))
            for x, y in self.initial_infected_coords
        ]
        # 5 pixels ~ 1 km
        self.infection_reach = int(5 * self.infection_reach * self.resize_factor)







        









