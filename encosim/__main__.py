import argparse
from .api_endpoint import run_full_stat_recap

parser = argparse.ArgumentParser(
    "EncoSim",
    description="Simulate a Dungeons and Dragons 5e Encounter",
)
parser.add_argument("--reps", type=int, default=10, help="Number of simulations")
parser.add_argument(
    "--team0",
    nargs="+",
    type=str,
    required=True,
    help="Characters of Team 0",
)
parser.add_argument(
    "--team1",
    nargs="+",
    type=str,
    required=True,
    help="Characters of Team 1",
)
parser.add_argument(
    "--team2",
    nargs="*",
    type=str,
    required=False,
    help="Characters of Team 2",
)

if __name__ == "__main__":
    pargs = parser.parse_args()

    if pargs.reps < 1:
        raise ValueError("Number of repetitions must be at least 1")

    res = run_full_stat_recap(pargs.reps, [pargs.team0, pargs.team1])
    print(res)
