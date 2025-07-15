"""Endpoint of the simulator for the web API"""

from Entity_class import entity as Entity
from Encounter_Simulator import full_statistical_recap
from Dm_class import DungeonMaster


def run_full_stat_recap(
    repetitions: int,
    teams: list[list[str]],
):
    """Return full statistical recap of the simulation

    Parameter
    ---------
    repetition: int
        Number of simulation repetitions
    teams: list of list of str
        Each `list of str` represents a party. Party members are given by
        file names without file extention

    Return
    ------
    str
        Statistical summary text
    """
    dm = DungeonMaster()
    dm.block_print()

    entities: list[Entity] = []
    for team, names in enumerate(teams):
        for name in names:
            entities.append(Entity(str(name), team, dm))
    return full_statistical_recap(int(repetitions), entities)
