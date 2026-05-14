from project.astronauts.base_astronaut import BaseAstronaut
from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation


class SpaceAgency:
    VALID_ASTRONAUT_TYPES = (EngineerAstronaut.__name__, ScientistAstronaut.__name__)
    VALID_STATION_TYPES = (MaintenanceStation.__name__, ResearchStation.__name__)
    def __init__(self):
        self.astronauts:list[BaseAstronaut] = []
        self.stations:list[BaseStation] = []

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        if astronaut_type not in SpaceAgency.VALID_ASTRONAUT_TYPES:
            raise ValueError("Invalid astronaut type!")
        for a in self.astronauts:
            if a.id_number == astronaut_id_number:
                raise ValueError(f"{astronaut_id_number} has been already added!")

        if astronaut_type == EngineerAstronaut.__name__:
            new_astronaut = EngineerAstronaut(astronaut_id_number, astronaut_salary)
        else:
            new_astronaut = ScientistAstronaut(astronaut_id_number, astronaut_salary)
        self.astronauts.append(new_astronaut)
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    def add_station(self, station_type: str, station_name: str):
        if station_type not in SpaceAgency.VALID_STATION_TYPES:
            raise ValueError("Invalid station type!")
        for s in self.stations:
            if s.name == station_name:
                raise ValueError(f"{station_name} has been already added!")

        if station_type == MaintenanceStation.__name__:
            new_station = MaintenanceStation(station_name)
        else:
            new_station = ResearchStation(station_name)
        self.stations.append(new_station)
        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self, station_name: str, astronaut_type: str):
        station_names = [s.name for s in self.stations]
        if station_name not in station_names:
            raise ValueError(f"Station {station_name} does not exist!")

        current_station = next((s for s in self.stations if s.name == station_name), None)

        searched_astronaut = [a for a in self.astronauts if a.specialization == astronaut_type]
        if not searched_astronaut:
            raise ValueError("No available astronauts of the type!")

        current_astronaut = searched_astronaut[0]

        if len(current_station.astronauts) == current_station.capacity:
            return "This station has no available capacity."

        self.astronauts.remove(current_astronaut)
        current_station.astronauts.append(current_astronaut)
        return f"{current_astronaut.id_number} was assigned to {station_name}."

    def train_astronauts(self, station: BaseStation, sessions_number: int):
        for _ in range(sessions_number):
            for astronaut in station.astronauts:
                astronaut.train()
        total_stamina = sum([a.stamina for a in station.astronauts])
        return f"{station.name} astronauts have {total_stamina} total stamina after {sessions_number} training session/s."

    def retire_astronaut(self, station: BaseStation, astronaut_id_number: str):
        astronaut_to_retire = next((a for a in station.astronauts if a.id_number == astronaut_id_number and a.stamina < 100), None)
        if not astronaut_to_retire:
            return f"The retirement process was canceled."
        station.astronauts.remove(astronaut_to_retire)
        return f"Retired astronaut {astronaut_id_number}."

    def agency_update(self, min_value: float):
        for station in self.stations:
            station.update_salaries(min_value)

        sorted_stations = sorted( self.stations, key=lambda s: (-len(s.astronauts), s.name))
        available_count = len(self.astronauts)
        stations_count = len(self.stations)
        total_capacity = sum([s.capacity - len(s.astronauts) for s in self.stations])
        result = []

        result.append("*Space Agency Up-to-Date Report*")
        result.append(f"Total number of available astronauts: {available_count}")
        result.append(f"**Stations count: {stations_count}; Total available capacity: {total_capacity}**")

        for s in sorted_stations:
            result.append(s.status())

        return "\n".join(result)

