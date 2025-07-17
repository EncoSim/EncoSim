from pathlib import Path
import sys

SRC = Path(__file__)
if getattr(sys, "frozen", False):
    SRC = Path(sys.executable)
SRC = SRC.resolve().absolute().parent

ENTITIES = SRC.parent / "Entities"
BENCHMARK_ENTITIES = SRC.parent / "BenchmarkEntities"
RESOURCES = SRC.parent / "Resources"
ARCHIVE = SRC.parent / "Archive"

# print(SRC, ENTITIES, BENCHMARK_ENTITIES, RESOURCES, ARCHIVE, sep="\n")
