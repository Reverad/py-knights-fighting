from app.battles.fight import fight
from app.conquerors.conquerors import calculate_stats


def battle(stats: dict) -> dict:
    result = fight(
        calculate_stats(stats["lancelot"]),
        calculate_stats(stats["mordred"])
    )
    result.update(
        fight(calculate_stats(stats["arthur"]),
              calculate_stats(stats["red_knight"]))
    )
    return result
