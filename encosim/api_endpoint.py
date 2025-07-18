"""Endpoint of the simulator for the web API"""

from .Entity_class import entity as Entity
from .Encounter_Simulator import full_statistical_recap
from .Dm_class import DungeonMaster


def run_full_stat_recap(
    repetitions: int,
    teams: list[list[str]],
):
    """Return full statistical recap of the simulation

    Parameter
    ---------
    repetition: int
        Number of simulation repetitions
    teams: list of list of json object
        Each `list of json` represents a party. Party members are given by json files, loaded by the api

    Return
    ------
    str
        Statistical summary text
    """
    dm = DungeonMaster()
    dm.block_print()

    entities: list[Entity] = []
    for team, players in enumerate(teams):
        for player in players:
            entities.append(Entity(str(player["Name"]), team, dm, external_json=player))
    return full_statistical_recap(int(repetitions), entities)
